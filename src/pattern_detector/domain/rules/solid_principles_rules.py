"""SOLID principles and clean code quality rules for Julia."""

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


class MonolithicStructSrpRule(BaseRule):
    """Detects monolithic structs / God Objects with excessive fields violating SRP."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if len(s.fields) >= 10 or s.line_count >= 60:
                score = 0.90 if len(s.fields) >= 12 else 0.82
                evidences = [
                    Evidence(
                        rule_code="SRP_MONOLITHIC_STRUCT",
                        description=f"Struct '{s.name}' is a Monolithic Struct declaring {len(s.fields)} fields; consider decomposing into cohesive sub-structs",
                        weight=score,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MONOLITHIC_STRUCT_SRP,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections


class FatAbstractTypeIspRule(BaseRule):
    """Detects fat abstract types requiring too many method implementations."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for abst in model.all_abstract_types:
            related_methods = [
                fn for fn in model.all_functions
                if any(p[1] == abst.name or abst.name in p[1] for p in fn.parameters)
            ]
            if len(related_methods) >= 9:
                evidences = [
                    Evidence(
                        rule_code="ISP_FAT_ABSTRACT_TYPE",
                        description=f"Abstract type '{abst.name}' enforces {len(related_methods)} required methods; consider decomposing into Holy Traits or smaller contracts",
                        weight=0.85,
                        location=abst.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FAT_ABSTRACT_TYPE_ISP,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=abst.name,
                        target_kind="abstract_type",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=abst.location,
                        evidences=evidences,
                    )
                )
        return detections


class ManualTypeBranchCascadeOcpRule(BaseRule):
    """Detects manual `if x isa ... elseif x isa ...` cascades violating Multiple Dispatch & OCP."""

    ISA_CASCADE_PATTERN = re.compile(r"\b(?:if|elseif)\s+[A-Za-z0-9_.]+\s+isa\s+[A-Za-z0-9_.]+")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = len(self.ISA_CASCADE_PATTERN.findall(fn.body or ""))
            if matches >= 3:
                evidences = [
                    Evidence(
                        rule_code="OCP_MANUAL_ISA_CASCADE",
                        description=f"Function '{fn.name}' uses {matches} manual 'isa' type checks; replace with idiomatic Julia Multiple Dispatch to satisfy OCP",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MANUAL_TYPE_BRANCH_CASCADE_OCP,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class KissCyclomaticComplexityRule(BaseRule):
    """Detects functions with excessive cyclomatic complexity."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.branch_count >= 9:
                evidences = [
                    Evidence(
                        rule_code="KISS_CYCLOMATIC_COMPLEXITY",
                        description=f"Function '{fn.name}' has high cyclomatic complexity ({fn.branch_count} branch points), violating KISS",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.KISS_CYCLOMATIC_COMPLEXITY,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class KissLongParameterListRule(BaseRule):
    """Detects functions accepting excessive parameters."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if len(fn.parameters) >= 6:
                evidences = [
                    Evidence(
                        rule_code="KISS_LONG_PARAMETER_LIST",
                        description=f"Function '{fn.name}' accepts {len(fn.parameters)} parameters; consider bundling into a configuration struct",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.KISS_LONG_PARAMETER_LIST,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class DryDuplicateLogicRule(BaseRule):
    """Detects identical duplicated code blocks across functions."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        body_map: dict[str, list[str]] = {}
        for fn in model.all_functions:
            cleaned = re.sub(r"\s+", " ", fn.body).strip()
            if len(cleaned) >= 50:
                body_map.setdefault(cleaned, []).append(fn.name)

        for body, names in body_map.items():
            if len(names) >= 2:
                evidences = [
                    Evidence(
                        rule_code="DRY_DUPLICATE_CODE",
                        description=f"Identical logic duplicated across {len(names)} function(s): {', '.join(names[:3])}",
                        weight=0.80,
                        location=None,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DRY_DUPLICATE_LOGIC,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=names[0],
                        target_kind="function",
                        confidence=Confidence(score=0.80, evidences=evidences),
                        primary_location=None,
                        evidences=evidences,
                    )
                )
        return detections


class DemeterLawTrainWreckRule(BaseRule):
    """Detects Law of Demeter violations (deep field navigation `a.b.c.d.e`)."""

    DOT_CHAIN_PATTERN = re.compile(r"\b[a-zA-Z_]\w*\.[a-zA-Z_]\w*\.[a-zA-Z_]\w*\.[a-zA-Z_]\w*\.[a-zA-Z_]\w*\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = self.DOT_CHAIN_PATTERN.findall(fn.body or "")
            if matches:
                evidences = [
                    Evidence(
                        rule_code="DEMETER_LAW_TRAIN_WRECK",
                        description=f"Function '{fn.name}' violates Law of Demeter with deep field access chain: '{matches[0]}'",
                        weight=0.80,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DEMETER_LAW_TRAIN_WRECK,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.80, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
