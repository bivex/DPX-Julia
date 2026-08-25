"""Resilience, Type Stability & Performance Hazards rules for Julia."""

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
    SourceLocation,
)


class TypeInstabilityNonConcreteFieldRule(BaseRule):
    """Detects struct fields defined with abstract types (`Any`, `Real`, `Number`, `AbstractArray`) causing boxing."""

    ABSTRACT_FIELD_TYPES = {"Any", "Real", "Number", "AbstractArray", "AbstractVector", "AbstractMatrix", "AbstractString", "Function"}

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if not s.is_parametric:
                untyped_fields = [
                    f for f in s.fields
                    if f.type_name in self.ABSTRACT_FIELD_TYPES or (f.type_name == "Any" and not f.raw_text.endswith("::Any"))
                ]
                if untyped_fields:
                    loc = untyped_fields[0].location or s.location
                    evidences = [
                        Evidence(
                            rule_code="HAZARD_TYPE_INSTABILITY_FIELD",
                            description=f"Struct '{s.name}' has non-concrete field(s) ({', '.join(f'{f.name}::{f.type_name}' for f in untyped_fields[:2])}) causing runtime boxing; parameterize type (e.g. struct {s.name}{{T}} ... end)",
                            weight=0.92,
                            location=loc,
                        )
                    ]
                    detections.append(
                        Detection(
                            pattern_type=PatternType.TYPE_INSTABILITY_NON_CONCRETE_FIELD,
                            pattern_category=PatternCategory.RESILIENCE,
                            target_name=s.name,
                            target_kind="struct",
                            confidence=Confidence(score=0.92, evidences=evidences),
                            primary_location=loc,
                            evidences=evidences,
                        )
                    )
        return detections


class UntypedGlobalMutationRule(BaseRule):
    """Detects mutation of non-const global variables in functions."""

    GLOBAL_VAR_PATTERN = re.compile(r"^\s*global\s+([A-Za-z0-9_]+)\s*=")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            match = self.GLOBAL_VAR_PATTERN.search(fn.body or "")
            if match:
                evidences = [
                    Evidence(
                        rule_code="HAZARD_UNTYPED_GLOBAL_MUTATION",
                        description=f"Function '{fn.name}' mutates global variable '{match.group(1)}' risking compiler de-optimization and race conditions",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.UNTYPED_GLOBAL_MUTATION,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class HotLoopArrayAllocationRule(BaseRule):
    """Detects array allocations (slicing without `@views` / `zeros(...)`) inside loops."""

    LOOP_ALLOC_PATTERN = re.compile(r"for\s+.*\n(?:[^\n]*\n)*?\s*(?:zeros|ones|rand|\[[^\]]+\])\s*\(")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if "for " in fn.body and ("zeros(" in fn.body or "ones(" in fn.body or "rand(" in fn.body):
                evidences = [
                    Evidence(
                        rule_code="HAZARD_HOT_LOOP_ARRAY_ALLOCATION",
                        description=f"Function '{fn.name}' allocates heap arrays inside loop; preallocate buffers or use mutating in-place functions ('!')",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.HOT_LOOP_ARRAY_ALLOCATION,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class SwallowedTaskExceptionRule(BaseRule):
    """Detects `@async` tasks launched without enclosing `@sync` or `wait(task)`."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if "@async" in fn.body and "@sync" not in fn.body and "wait(" not in fn.body and "fetch(" not in fn.body:
                evidences = [
                    Evidence(
                        rule_code="HAZARD_SWALLOWED_TASK_EXCEPTION",
                        description=f"Function '{fn.name}' launches unconfined @async task without @sync or wait(); uncaught task exceptions will be lost",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SWALLOWED_TASK_EXCEPTION,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class UnsynchronizedGlobalRaceRule(BaseRule):
    """Detects concurrent mutations of shared collections inside `Threads.@threads`."""

    RACE_PATTERN = re.compile(r"Threads\.@threads\s+for.*\n(?:[^\n]*\n)*?\s*push!\s*\(")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.RACE_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="HAZARD_UNSYNCHRONIZED_CONCURRENT_RACE",
                        description=f"Function '{fn.name}' mutates shared array with push! inside Threads.@threads without locks, causing data races",
                        weight=0.92,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.UNSYNCHRONIZED_GLOBAL_RACE,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
