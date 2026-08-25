"""Julia Idiomatic, Holy Traits, and Metaprogramming rules."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
)


class HolyTraitsDispatchRule(BaseRule):
    """Detects Holy Traits Pattern (trait abstract types with singleton dispatch functions)."""

    TRAIT_FUNC_PATTERN = re.compile(r"^\s*([A-Za-z0-9_]+Trait|[a-z0-9_]+_trait|trait)\s*\(::(?:Type\{)?(?:\w+)?\}?\)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        trait_absts = [t for t in model.all_abstract_types if "Trait" in t.name or "Style" in t.name or "IndexStyle" in t.name]

        for t in trait_absts:
            evidences = [
                Evidence(
                    rule_code="JULIA_HOLY_TRAITS",
                    description=f"Abstract trait hierarchy '{t.name}' enables zero-cost compile-time Holy Traits dispatch",
                    weight=0.95,
                    location=t.location,
                )
            ]
            detections.append(
                Detection(
                    pattern_type=PatternType.HOLY_TRAITS_DISPATCH,
                    pattern_category=PatternCategory.JULIA_IDIOMATIC,
                    target_name=t.name,
                    target_kind="abstract_trait",
                    confidence=Confidence(score=0.95, evidences=evidences),
                    primary_location=t.location,
                    evidences=evidences,
                )
            )

        for fn in model.all_functions:
            if "trait(" in fn.signature or "Trait(" in fn.signature or "_trait(" in fn.name:
                evidences = [
                    Evidence(
                        rule_code="JULIA_HOLY_TRAITS_DISPATCHER",
                        description=f"Function '{fn.name}' implements Holy Trait mapping for trait-based method dispatch",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.HOLY_TRAITS_DISPATCH,
                        pattern_category=PatternCategory.JULIA_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="trait_function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ParametricTypeSpecializationRule(BaseRule):
    """Detects Parametric Structs ensuring concrete memory layouts and zero-overhead vectorization."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if s.is_parametric and s.type_parameters:
                evidences = [
                    Evidence(
                        rule_code="JULIA_PARAMETRIC_SPECIALIZATION",
                        description=f"Struct '{s.name}{{{', '.join(s.type_parameters)}}}' specializes concrete memory layout across type parameters",
                        weight=0.95,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PARAMETRIC_TYPE_SPECIALIZATION,
                        pattern_category=PatternCategory.JULIA_IDIOMATIC,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class MetaprogrammingMacroDslRule(BaseRule):
    """Detects Metaprogramming macros generating compile-time AST domain DSLs."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for m in model.all_macros:
            evidences = [
                Evidence(
                    rule_code="JULIA_MACRO_METAPROGRAMMING",
                    description=f"Macro '@{m.name}' transforms compile-time AST for domain-specific syntax extension",
                    weight=0.95,
                    location=m.location,
                )
            ]
            detections.append(
                Detection(
                    pattern_type=PatternType.METAPROGRAMMING_MACRO_DSL,
                    pattern_category=PatternCategory.JULIA_IDIOMATIC,
                    target_name=f"@{m.name}",
                    target_kind="macro",
                    confidence=Confidence(score=0.95, evidences=evidences),
                    primary_location=m.location,
                    evidences=evidences,
                )
            )
        return detections


class HomoiconicAstTransformRule(BaseRule):
    """Detects homoiconic code-as-data manipulation (`Expr(:call, ...)`, `Meta.parse`, `eval`)."""

    EXPR_PATTERN = re.compile(r"\b(Expr\s*\(|Meta\.parse\s*\(|esc\s*\(|quote\b)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if not fn.is_macro and self.EXPR_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="JULIA_HOMOICONIC_AST",
                        description=f"Function '{fn.name}' generates or manipulates homoiconic Julia AST expressions",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.HOMOICONIC_AST_TRANSFORM,
                        pattern_category=PatternCategory.JULIA_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class BroadcastOperatorOverloadRule(BaseRule):
    """Detects custom vectorized broadcasting protocol (`Base.broadcasted`)."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if "broadcasted" in fn.name or "Base.broadcasted" in fn.signature:
                evidences = [
                    Evidence(
                        rule_code="JULIA_BROADCAST_OVERLOAD",
                        description=f"Function '{fn.name}' overloads Julia fused broadcasting engine",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BROADCAST_OPERATOR_OVERLOAD,
                        pattern_category=PatternCategory.JULIA_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ConversionPromotionProtocolRule(BaseRule):
    """Detects type conversion and promotion protocols (`Base.convert`, `Base.promote_rule`)."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.name in ("convert", "Base.convert", "promote_rule", "Base.promote_rule"):
                evidences = [
                    Evidence(
                        rule_code="JULIA_CONVERT_PROMOTE",
                        description=f"Method '{fn.name}' hooks into Julia core numeric and type promotion engine",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.CONVERSION_PROMOTION_PROTOCOL,
                        pattern_category=PatternCategory.JULIA_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
