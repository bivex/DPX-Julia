"""Unit tests for Julia Resilience, Type Stability, and Performance Hazards."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.resilience_hazards_rules import (
    HotLoopArrayAllocationRule,
    SwallowedTaskExceptionRule,
    TypeInstabilityNonConcreteFieldRule,
    UnsynchronizedGlobalRaceRule,
    UntypedGlobalMutationRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_type_instability_non_concrete_field() -> None:
    code = """
    struct BadDataModel
        name::String
        score::Real
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("bad_struct.jl", code)])

    rule = TypeInstabilityNonConcreteFieldRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TYPE_INSTABILITY_NON_CONCRETE_FIELD
    assert detections[0].target_name == "BadDataModel"


def test_untyped_global_mutation() -> None:
    code = """
    function update_counter()
        global counter = counter + 1
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("global.jl", code)])

    rule = UntypedGlobalMutationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.UNTYPED_GLOBAL_MUTATION


def test_hot_loop_array_allocation() -> None:
    code = """
    function compute_matrix_loop(n::Int)
        for i in 1:n
            temp = zeros(Float64, 100, 100)
            work(temp)
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("loop.jl", code)])

    rule = HotLoopArrayAllocationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.HOT_LOOP_ARRAY_ALLOCATION


def test_swallowed_task_exception() -> None:
    code = """
    function fire_and_forget()
        @async background_heavy_computation()
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("async.jl", code)])

    rule = SwallowedTaskExceptionRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SWALLOWED_TASK_EXCEPTION


def test_unsynchronized_global_race() -> None:
    code = """
    function race_condition_loop(items)
        results = []
        Threads.@threads for x in items
            push!(results, x)
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("race.jl", code)])

    rule = UnsynchronizedGlobalRaceRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.UNSYNCHRONIZED_GLOBAL_RACE
