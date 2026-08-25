"""Unit tests for Julia Concurrency, Tasks, and Parallelism rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.concurrency_rules import (
    AtomicMemoryOperationRule,
    ChannelCspPipelineRule,
    TaskAsyncCoroutineRule,
    ThreadsParallelLoopRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_task_async_coroutine() -> None:
    code = """
    function fetch_data_async()
        @sync begin
            @async download_part_1()
            @async download_part_2()
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("async.jl", code)])

    rule = TaskAsyncCoroutineRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TASK_ASYNC_COROUTINE
    assert detections[0].target_name == "fetch_data_async"


def test_channel_csp_pipeline() -> None:
    code = """
    function producer_consumer()
        ch = Channel{Int}(32)
        put!(ch, 42)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("channel.jl", code)])

    rule = ChannelCspPipelineRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CHANNEL_CSP_PIPELINE


def test_threads_parallel_loop() -> None:
    code = """
    function parallel_sum(arr::Vector{Float64})
        Threads.@threads for i in 1:length(arr)
            process_item(arr[i])
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("parallel.jl", code)])

    rule = ThreadsParallelLoopRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.THREADS_PARALLEL_LOOP


def test_atomic_memory_operation() -> None:
    code = """
    struct SharedCounter
        count::Threads.Atomic{Int}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("atomic.jl", code)])

    rule = AtomicMemoryOperationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ATOMIC_MEMORY_OPERATION
    assert detections[0].target_name == "SharedCounter"
