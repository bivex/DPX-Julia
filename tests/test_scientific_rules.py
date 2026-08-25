"""Unit tests for Julia Scientific Computing and Zero-Allocation rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.scientific_rules import (
    CallableStructFunctorRule,
    InPlaceMutatingConventionRule,
    ZeroAllocationViewRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_zero_allocation_view() -> None:
    code = """
    function compute_slice_mean(A::Matrix{Float64})
        v = view(A, 1:10, 1:10)
        return sum(v)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("view.jl", code)])

    rule = ZeroAllocationViewRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ZERO_ALLOCATION_VIEW


def test_in_place_mutating_convention() -> None:
    code = """
    function normalize_matrix!(A::Matrix{Float64})
        A ./= sum(A)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("mutate.jl", code)])

    rule = InPlaceMutatingConventionRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.IN_PLACE_MUTATING_CONVENTION
    assert detections[0].target_name == "normalize_matrix!"


def test_callable_struct_functor() -> None:
    code = """
    struct Polynomial
        coeffs::Vector{Float64}
    end

    (p::Polynomial)(x::Float64) = sum(c * x^(i-1) for (i, c) in enumerate(p.coeffs))
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("functor.jl", code)])

    rule = CallableStructFunctorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CALLABLE_STRUCT_FUNCTOR
