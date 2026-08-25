"""Julia Scientific Computing and Zero-Allocation performance rules."""

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


class ZeroAllocationViewRule(BaseRule):
    """Detects zero-allocation array views (`@views`, `view(A, ...)`)."""

    VIEW_PATTERN = re.compile(r"\b(@views|view\s*\()")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.VIEW_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="SCIENTIFIC_ZERO_ALLOCATION_VIEW",
                        description=f"Function '{fn.name}' uses zero-allocation array views avoiding memory copying",
                        weight=0.92,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ZERO_ALLOCATION_VIEW,
                        pattern_category=PatternCategory.SCIENTIFIC_PERFORMANCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class InPlaceMutatingConventionRule(BaseRule):
    """Detects Julia in-place mutating functions mutating first argument (`foo!(...)`)."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.is_mutating and not fn.name.startswith("@"):
                evidences = [
                    Evidence(
                        rule_code="SCIENTIFIC_IN_PLACE_MUTATION",
                        description=f"Function '{fn.name}' follows Julia mutating convention modifying arguments in-place to avoid allocations",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.IN_PLACE_MUTATING_CONVENTION,
                        pattern_category=PatternCategory.SCIENTIFIC_PERFORMANCE,
                        target_name=fn.name,
                        target_kind="mutating_function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class CallableStructFunctorRule(BaseRule):
    """Detects callable structs acting as functors (`(obj::MyStruct)(x)`)."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.is_callable_struct:
                evidences = [
                    Evidence(
                        rule_code="SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR",
                        description=f"Callable struct functor '{fn.name}' encapsulates state and behaves as an invocable function",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.CALLABLE_STRUCT_FUNCTOR,
                        pattern_category=PatternCategory.SCIENTIFIC_PERFORMANCE,
                        target_name=fn.name,
                        target_kind="callable_struct",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
