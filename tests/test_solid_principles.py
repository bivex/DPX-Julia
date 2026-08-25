"""Unit tests for Julia SOLID and clean code quality rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.solid_principles_rules import (
    FatAbstractTypeIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    ManualTypeBranchCascadeOcpRule,
    MonolithicStructSrpRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_monolithic_struct_srp() -> None:
    fields_code = "\n".join(f"field_{i}::Float64" for i in range(12))
    code = f"""
    struct BigDataStruct
        {fields_code}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("big.jl", code)])

    rule = MonolithicStructSrpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MONOLITHIC_STRUCT_SRP
    assert detections[0].target_name == "BigDataStruct"


def test_fat_abstract_type_isp() -> None:
    methods_code = "\n".join(f"function method_{i}(x::MegaContract) end" for i in range(10))
    code = f"""
    abstract type MegaContract end

    {methods_code}
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("mega.jl", code)])

    rule = FatAbstractTypeIspRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FAT_ABSTRACT_TYPE_ISP


def test_manual_type_branch_cascade_ocp() -> None:
    code = """
    function handle_shape(s)
        if s isa Circle
            render_circle(s)
        elseif s isa Rectangle
            render_rect(s)
        elseif s isa Triangle
            render_triangle(s)
        elseif s isa Polygon
            render_polygon(s)
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("shape.jl", code)])

    rule = ManualTypeBranchCascadeOcpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MANUAL_TYPE_BRANCH_CASCADE_OCP


def test_kiss_long_parameter_list() -> None:
    code = """
    function configure_simulation(dt, tmax, tolerance, max_iters, grid_size, verbose, log_level)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("sim.jl", code)])

    rule = KissLongParameterListRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.KISS_LONG_PARAMETER_LIST


def test_kiss_cyclomatic_complexity() -> None:
    branches = "\n".join(f"if x == {i} println({i}) end" for i in range(11))
    code = f"""
    function complex_branch(x)
        {branches}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("complex.jl", code)])

    rule = KissCyclomaticComplexityRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.KISS_CYCLOMATIC_COMPLEXITY
