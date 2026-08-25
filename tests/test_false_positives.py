"""Unit tests verifying zero false positives on clean, idiomatic Julia code."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.rules.resilience_hazards_rules import (
    HotLoopArrayAllocationRule,
    SwallowedTaskExceptionRule,
    TypeInstabilityNonConcreteFieldRule,
    UnsynchronizedGlobalRaceRule,
    UntypedGlobalMutationRule,
)
from pattern_detector.domain.rules.solid_principles_rules import (
    FatAbstractTypeIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    ManualTypeBranchCascadeOcpRule,
    MonolithicStructSrpRule,
)
from pattern_detector.domain.services.rule_engine import RuleEngineService
from pattern_detector.domain.value_objects import PatternCategory


def test_clean_parametric_struct_no_type_instability_hazard() -> None:
    code = """
    struct ConcreteParticle{T<:Real}
        x::T
        y::T
        vx::T
        vy::T
        mass::Float64
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("particle.jl", code)])

    rule = TypeInstabilityNonConcreteFieldRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_clean_multiple_dispatch_no_manual_isa_hazard() -> None:
    code = """
    abstract type Shape end
    struct Circle <: Shape radius::Float64 end
    struct Rect <: Shape width::Float64 height::Float64 end

    area(s::Circle) = pi * s.radius^2
    area(s::Rect) = s.width * s.height
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("shapes.jl", code)])

    rule = ManualTypeBranchCascadeOcpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_clean_sync_task_no_swallowed_task_hazard() -> None:
    code = """
    function compute_concurrently()
        @sync begin
            @async task_a()
            @async task_b()
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("sync.jl", code)])

    rule = SwallowedTaskExceptionRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_focused_abstract_type_no_fat_isp() -> None:
    code = """
    abstract type Serializable end
    serialize(s::Serializable) = nothing
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("serial.jl", code)])

    rule = FatAbstractTypeIspRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_pure_domain_service_no_hazards() -> None:
    code = """
    struct VectorMath{T<:Real}
        scaling::T
    end

    function apply_scale(vm::VectorMath{T}, x::T)::T where {T<:Real}
        return vm.scaling * x
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("math.jl", code)])

    engine = RuleEngineService(rules=get_default_rules())
    detections = engine.evaluate(model)

    hazards = [d for d in detections if d.pattern_category in (PatternCategory.RESILIENCE, PatternCategory.PRINCIPLE)]
    assert len(hazards) == 0
