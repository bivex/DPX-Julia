"""Julia Concurrency, Tasks, and Parallel Computing rules."""

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


class TaskAsyncCoroutineRule(BaseRule):
    """Detects Julia lightweight asynchronous tasks and coroutines (`@async`, `@sync`, `schedule`)."""

    ASYNC_PATTERN = re.compile(r"(@async\b|@sync\b|schedule\s*\(|Task\s*\()")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.ASYNC_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="CONCURRENCY_TASK_ASYNC",
                        description=f"Function '{fn.name}' coordinates cooperative asynchronous tasks via @async / @sync",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.TASK_ASYNC_COROUTINE,
                        pattern_category=PatternCategory.CONCURRENCY_PARALLELISM,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ChannelCspPipelineRule(BaseRule):
    """Detects Channel CSP communication pipelines (`Channel{T}`, `put!`, `take!`)."""

    CHANNEL_PATTERN = re.compile(r"\bChannel(?:\{[^}]+\})?\s*\(")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.CHANNEL_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="CONCURRENCY_CHANNEL_CSP",
                        description=f"Function '{fn.name}' implements CSP message-passing pipeline via Channel{{T}}",
                        weight=0.92,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.CHANNEL_CSP_PIPELINE,
                        pattern_category=PatternCategory.CONCURRENCY_PARALLELISM,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.92, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ThreadsParallelLoopRule(BaseRule):
    """Detects multithreaded loop parallelization (`Threads.@threads for`)."""

    THREADS_PATTERN = re.compile(r"\b(Threads\.@threads|@threads)\s+for\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.THREADS_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="CONCURRENCY_THREADS_PARALLEL",
                        description=f"Function '{fn.name}' executes multithreaded parallel loop via Threads.@threads",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.THREADS_PARALLEL_LOOP,
                        pattern_category=PatternCategory.CONCURRENCY_PARALLELISM,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class AtomicMemoryOperationRule(BaseRule):
    """Detects atomic lock-free shared-memory operations (`Threads.Atomic` / `@atomic`)."""

    ATOMIC_PATTERN = re.compile(r"\b(Threads\.Atomic|@atomic|atomic_add!|atomic_xchg!)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for s in model.all_structs:
            if any(self.ATOMIC_PATTERN.search(f.type_name) for f in s.fields):
                evidences = [
                    Evidence(
                        rule_code="CONCURRENCY_ATOMIC_MEMORY",
                        description=f"Struct '{s.name}' coordinates thread safety via lock-free Atomic primitives",
                        weight=0.90,
                        location=s.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ATOMIC_MEMORY_OPERATION,
                        pattern_category=PatternCategory.CONCURRENCY_PARALLELISM,
                        target_name=s.name,
                        target_kind="struct",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=s.location,
                        evidences=evidences,
                    )
                )
        return detections
