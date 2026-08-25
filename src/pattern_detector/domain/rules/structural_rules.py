"""GoF Structural design pattern detection rules for Julia (7/7)."""

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


class AdapterWrapperStructRule(BaseRule):
    """Detects Adapter pattern wrapping third-party or foreign types."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Adapter" in s.name or "Wrapper" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_ADAPTER_WRAPPER",
                        description=f"Struct '{s.name}' adapts target type to domain contracts",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ADAPTER_WRAPPER_STRUCT,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class BridgeDriverDecouplingRule(BaseRule):
    """Detects Bridge pattern decoupling domain abstraction from implementor drivers."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            driver_fields = [
                f for f in s.fields
                if any(suffix in f.type_name for suffix in ("Driver", "Backend", "Engine", "Renderer", "Implementor"))
            ]
            if driver_fields or "Bridge" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_BRIDGE_DRIVER",
                        description=f"Struct '{s.name}' decouples abstraction from implementor driver via '{driver_fields[0].name if driver_fields else 'driver'}'",
                        weight=0.85,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BRIDGE_DRIVER_DECOUPLING,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class CompositeStructTreeRule(BaseRule):
    """Detects Composite pattern with recursive child node collections."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_children = any(
                f.type_name in (f"Vector{{{s.name}}}", f"Array{{{s.name}}}", "Vector{Any}", "Vector{Node}")
                or f.name in ("children", "nodes", "elements")
                for f in s.fields
            )
            if has_children or "Composite" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_COMPOSITE_TREE",
                        description=f"Struct '{s.name}' implements Composite pattern holding recursive tree collections",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPOSITE_STRUCT_TREE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class DecoratorForwardingWrapperRule(BaseRule):
    """Detects Decorator pattern wrapping an inner struct and augmenting behavior."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_inner = any(f.name in ("inner", "wrapped", "parent", "base") for f in s.fields)
            if (has_inner and len(s.fields) <= 3) or "Decorator" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_DECORATOR_WRAPPER",
                        description=f"Struct '{s.name}' decorates and augments an underlying instance",
                        weight=0.85,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DECORATOR_FORWARDING_WRAPPER,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class FacadeCoordinatorModuleRule(BaseRule):
    """Detects Facade Coordinator module orchestrating multiple subsystems."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for m in model.all_modules:
            if "Facade" in m.name or (len(m.structs) >= 3 and len(m.functions) >= 5):
                score = 0.90 if "Facade" in m.name else 0.80
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_FACADE_MODULE",
                        description=f"Module '{m.name}' acts as unified Facade coordinating multiple subsystem components",
                        weight=score,
                        location=m.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FACADE_COORDINATOR_MODULE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=m.name,
                        target_kind="module",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=m.location,
                        evidences=evidences,
                    )
                )
        return detections


class FlyweightPoolCacheRule(BaseRule):
    """Detects Flyweight pattern sharing instances via dictionary pool or memoization."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            has_cache = any("cache" in f.name.lower() or "pool" in f.name.lower() for f in s.fields)
            if has_cache or "Flyweight" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_FLYWEIGHT_CACHE",
                        description=f"Struct '{s.name}' shares fine-grained instances via Flyweight dictionary cache",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FLYWEIGHT_POOL_CACHE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class ProxyLazyOrRemoteRule(BaseRule):
    """Detects Proxy pattern controlling access to deferred or remote resources."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if "Proxy" in s.name or "Lazy" in s.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_PROXY_SURROGATE",
                        description=f"Struct '{s.name}' acts as Proxy surrogate controlling access to target service",
                        weight=0.88,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PROXY_LAZY_OR_REMOTE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections
