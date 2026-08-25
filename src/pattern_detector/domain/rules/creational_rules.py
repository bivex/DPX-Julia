"""GoF Creational design pattern detection rules for Julia (5/5)."""

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


class SingletonImmutableInstanceRule(BaseRule):
    """Detects Singleton instances represented as zero-field immutable structs or constant instances."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if s.is_singleton and ("Singleton" in s.name or "Config" in s.name or "Context" in s.name or not s.fields):
                score = 0.90 if "Singleton" in s.name else 0.85
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_SINGLETON_STRUCT",
                        description=f"Zero-field immutable struct '{s.name}' serves as a unique type-level Singleton instance",
                        weight=score,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SINGLETON_IMMUTABLE_INSTANCE,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class FactoryMethodConstructorRule(BaseRule):
    """Detects Factory Method pattern instantiating polymorphic subtypes."""

    FACTORY_NAME_PATTERN = re.compile(r"\b(create_[a-zA-Z0-9_]+|make_[a-zA-Z0-9_]+|build_[a-zA-Z0-9_]+)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.FACTORY_NAME_PATTERN.search(fn.name) or ("Factory" in fn.name):
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_FACTORY_METHOD",
                        description=f"Function '{fn.name}' encapsulates instance creation as a Factory Method",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FACTORY_METHOD_CONSTRUCTOR,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class AbstractFactoryHierarchyRule(BaseRule):
    """Detects Abstract Factory hierarchy grouping families of related constructors."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for abst in model.all_abstract_types:
            if "Factory" in abst.name or "Provider" in abst.name or "Builder" in abst.name:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_ABSTRACT_FACTORY",
                        description=f"Abstract type '{abst.name}' defines Abstract Factory contract for component families",
                        weight=0.90,
                        location=abst.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ABSTRACT_FACTORY_HIERARCHY,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=abst.name,
                        target_kind="abstract_type",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=abst.location,
                        evidences=evidences,
                    )
                )
        return detections


class BuilderFluentStructRule(BaseRule):
    """Detects Builder pattern structs with step-by-step parameter accumulation."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Builder" in s.name:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_BUILDER_STRUCT",
                        description=f"Struct '{s.name}' implements Builder pattern accumulating configuration parameters",
                        weight=0.90,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BUILDER_FLUENT_STRUCT,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class PrototypeDeepcopyRule(BaseRule):
    """Detects Prototype pattern cloning via `deepcopy` or custom copy constructors."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.name in ("copy", "Base.copy", "deepcopy", "Base.deepcopy") or ("clone" in fn.name):
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_PROTOTYPE_COPY",
                        description=f"Method '{fn.name}' implements Prototype pattern for object cloning and duplication",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PROTOTYPE_DEEPCOPY,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
