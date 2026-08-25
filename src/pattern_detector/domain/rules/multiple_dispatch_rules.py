"""Multiple Dispatch core paradigm rules for Julia."""

from __future__ import annotations

from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
)


class MultipleDispatchPolymorphismRule(BaseRule):
    """Detects multi-argument type-specialized multiple dispatch."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            typed_params = [p for p in fn.parameters if p[1] and p[1] != "Any"]
            if len(typed_params) >= 2 and not fn.is_macro:
                evidences = [
                    Evidence(
                        rule_code="JULIA_MULTIPLE_DISPATCH",
                        description=f"Function '{fn.name}' performs multi-argument dynamic multiple dispatch over ({', '.join(f'{p[0]}::{p[1]}' for p in typed_params)})",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MULTIPLE_DISPATCH_POLYMORPHISM,
                        pattern_category=PatternCategory.MULTIPLE_DISPATCH,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class OuterConstructorDispatchRule(BaseRule):
    """Detects Outer Constructor method specialization."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        struct_names = {s.name for s in model.all_structs}
        for fn in model.all_functions:
            if fn.name in struct_names:
                evidences = [
                    Evidence(
                        rule_code="JULIA_OUTER_CONSTRUCTOR",
                        description=f"Function '{fn.name}' acts as polymorphic Outer Constructor specializing struct instantiation",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.OUTER_CONSTRUCTOR_DISPATCH,
                        pattern_category=PatternCategory.MULTIPLE_DISPATCH,
                        target_name=fn.name,
                        target_kind="outer_constructor",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class MethodSpecializationTableRule(BaseRule):
    """Detects generic functions with multiple overloaded method signatures."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        func_map: dict[str, list] = {}
        for fn in model.all_functions:
            if not fn.is_macro:
                func_map.setdefault(fn.name, []).append(fn)

        for name, methods in func_map.items():
            if len(methods) >= 3:
                loc = methods[0].location
                evidences = [
                    Evidence(
                        rule_code="JULIA_METHOD_SPECIALIZATION_TABLE",
                        description=f"Generic function '{name}' defines {len(methods)} specialized dispatch methods forming an open polymorphic protocol",
                        weight=0.92,
                        location=loc,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.METHOD_SPECIALIZATION_TABLE,
                        pattern_category=PatternCategory.MULTIPLE_DISPATCH,
                        target_name=name,
                        target_kind="generic_function",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=loc,
                        related_locations=[m.location for m in methods[1:] if m.location],
                        evidences=evidences,
                    )
                )
        return detections
