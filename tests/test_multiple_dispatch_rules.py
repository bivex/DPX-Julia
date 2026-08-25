"""Unit tests for Julia Multiple Dispatch rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.multiple_dispatch_rules import (
    MethodSpecializationTableRule,
    MultipleDispatchPolymorphismRule,
    OuterConstructorDispatchRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_multiple_dispatch_polymorphism() -> None:
    code = """
    function collide(a::Asteroid, b::Spaceship)
        println("Asteroid hit Spaceship")
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("dispatch.jl", code)])

    rule = MultipleDispatchPolymorphismRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MULTIPLE_DISPATCH_POLYMORPHISM
    assert detections[0].target_name == "collide"


def test_outer_constructor_dispatch() -> None:
    code = """
    struct ComplexMatrix
        data::Matrix{Float64}
    end

    function ComplexMatrix(dims::Tuple{Int, Int})
        return ComplexMatrix(zeros(Float64, dims))
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("matrix.jl", code)])

    rule = OuterConstructorDispatchRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.OUTER_CONSTRUCTOR_DISPATCH
    assert detections[0].target_name == "ComplexMatrix"


def test_method_specialization_table() -> None:
    code = """
    function render(x::Int)
        println("Int: ", x)
    end

    function render(x::String)
        println("String: ", x)
    end

    function render(x::Float64)
        println("Float: ", x)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("render.jl", code)])

    rule = MethodSpecializationTableRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.METHOD_SPECIALIZATION_TABLE
    assert detections[0].target_name == "render"
