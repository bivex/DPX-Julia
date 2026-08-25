"""Unit tests for Julia Idiomatic, Holy Traits, and Metaprogramming rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.idiomatic_rules import (
    BroadcastOperatorOverloadRule,
    ConversionPromotionProtocolRule,
    HolyTraitsDispatchRule,
    HomoiconicAstTransformRule,
    MetaprogrammingMacroDslRule,
    ParametricTypeSpecializationRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_holy_traits_dispatch() -> None:
    code = """
    abstract type AlgorithmTrait end
    struct FastAlgorithmTrait <: AlgorithmTrait end
    struct ExactAlgorithmTrait <: AlgorithmTrait end

    algorithm_trait(::Type{MySolver}) = FastAlgorithmTrait()
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("traits.jl", code)])

    rule = HolyTraitsDispatchRule()
    detections = rule.evaluate(model)

    assert len(detections) >= 1
    assert any(d.pattern_type == PatternType.HOLY_TRAITS_DISPATCH for d in detections)


def test_parametric_type_specialization() -> None:
    code = """
    struct PointVector{T, N}
        coordinates::Vector{T}
        dimension::Int
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("point.jl", code)])

    rule = ParametricTypeSpecializationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PARAMETRIC_TYPE_SPECIALIZATION
    assert detections[0].target_name == "PointVector"


def test_metaprogramming_macro_dsl() -> None:
    code = """
    macro timed_execution(expr)
        quote
            t0 = time()
            val = $(esc(expr))
            println("Time: ", time() - t0)
            val
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("macro.jl", code)])

    rule = MetaprogrammingMacroDslRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.METAPROGRAMMING_MACRO_DSL
    assert detections[0].target_name == "@timed_execution"


def test_homoiconic_ast_transform() -> None:
    code = """
    function generate_function_ast(sym::Symbol)
        return Expr(:call, sym, 1, 2)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("ast.jl", code)])

    rule = HomoiconicAstTransformRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.HOMOICONIC_AST_TRANSFORM


def test_broadcast_operator_overload() -> None:
    code = """
    function Base.broadcasted(f, x::CustomContainer)
        return CustomContainer(f.(x.data))
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("broadcast.jl", code)])

    rule = BroadcastOperatorOverloadRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BROADCAST_OPERATOR_OVERLOAD


def test_conversion_promotion_protocol() -> None:
    code = """
    function Base.convert(::Type{CustomFloat}, x::Float64)
        return CustomFloat(x)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("convert.jl", code)])

    rule = ConversionPromotionProtocolRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CONVERSION_PROMOTION_PROTOCOL
