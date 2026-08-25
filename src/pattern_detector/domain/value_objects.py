"""Value objects and domain enumerations for Julia Pattern Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class PatternCategory(str, Enum):
    """Categorization of Julia architectural patterns and quality rules."""

    JULIA_IDIOMATIC = "julia_idiomatic"
    MULTIPLE_DISPATCH = "multiple_dispatch"
    CONCURRENCY_PARALLELISM = "concurrency_parallelism"
    SCIENTIFIC_PERFORMANCE = "scientific_performance"
    CREATIONAL = "creational"
    STRUCTURAL = "structural"
    BEHAVIORAL = "behavioral"
    RESILIENCE = "resilience"
    PRINCIPLE = "principle"


class PatternType(str, Enum):
    """Specific pattern types, idioms, and performance hazards in Julia codebases."""

    # 1. Julia Idiomatic & Metaprogramming
    HOLY_TRAITS_DISPATCH = "holy_traits_dispatch"
    PARAMETRIC_TYPE_SPECIALIZATION = "parametric_type_specialization"
    METAPROGRAMMING_MACRO_DSL = "metaprogramming_macro_dsl"
    HOMOICONIC_AST_TRANSFORM = "homoiconic_ast_transform"
    BROADCAST_OPERATOR_OVERLOAD = "broadcast_operator_overload"
    CONVERSION_PROMOTION_PROTOCOL = "conversion_promotion_protocol"

    # 2. Multiple Dispatch Core Paradigms
    MULTIPLE_DISPATCH_POLYMORPHISM = "multiple_dispatch_polymorphism"
    OUTER_CONSTRUCTOR_DISPATCH = "outer_constructor_dispatch"
    METHOD_SPECIALIZATION_TABLE = "method_specialization_table"

    # 3. Concurrency & Parallelism
    TASK_ASYNC_COROUTINE = "task_async_coroutine"
    CHANNEL_CSP_PIPELINE = "channel_csp_pipeline"
    THREADS_PARALLEL_LOOP = "threads_parallel_loop"
    ATOMIC_MEMORY_OPERATION = "atomic_memory_operation"

    # 4. Scientific & High-Performance Patterns
    ZERO_ALLOCATION_VIEW = "zero_allocation_view"
    IN_PLACE_MUTATING_CONVENTION = "in_place_mutating_convention"
    CALLABLE_STRUCT_FUNCTOR = "callable_struct_functor"

    # 5. GoF Creational Patterns (5/5)
    SINGLETON_IMMUTABLE_INSTANCE = "singleton_immutable_instance"
    FACTORY_METHOD_CONSTRUCTOR = "factory_method_constructor"
    ABSTRACT_FACTORY_HIERARCHY = "abstract_factory_hierarchy"
    BUILDER_FLUENT_STRUCT = "builder_fluent_struct"
    PROTOTYPE_DEEPCOPY = "prototype_deepcopy"

    # 6. GoF Structural Patterns (7/7)
    ADAPTER_WRAPPER_STRUCT = "adapter_wrapper_struct"
    BRIDGE_DRIVER_DECOUPLING = "bridge_driver_decoupling"
    COMPOSITE_STRUCT_TREE = "composite_struct_tree"
    DECORATOR_FORWARDING_WRAPPER = "decorator_forwarding_wrapper"
    FACADE_COORDINATOR_MODULE = "facade_coordinator_module"
    FLYWEIGHT_POOL_CACHE = "flyweight_pool_cache"
    PROXY_LAZY_OR_REMOTE = "proxy_lazy_or_remote"

    # 7. GoF Behavioral Patterns (11/11)
    CHAIN_OF_RESPONSIBILITY_PIPELINE = "chain_of_responsibility_pipeline"
    COMMAND_CALLABLE_TASK = "command_callable_task"
    INTERPRETER_AST_EVAL = "interpreter_ast_eval"
    ITERATOR_BASE_PROTOCOL = "iterator_base_protocol"
    MEDIATOR_CENTRAL_COORDINATOR = "mediator_central_coordinator"
    MEMENTO_STATE_SNAPSHOT = "memento_state_snapshot"
    OBSERVER_CHANNEL_SUBSCRIPTION = "observer_channel_subscription"
    STATE_ABSTRACT_TYPE_FSM = "state_abstract_type_fsm"
    STRATEGY_TRAIT_ALGORITHM = "strategy_trait_algorithm"
    TEMPLATE_METHOD_SKELETON = "template_method_skeleton"
    VISITOR_MULTIPLE_DISPATCH = "visitor_multiple_dispatch"

    # 8. Resilience, Type Stability & Performance Hazards
    TYPE_INSTABILITY_NON_CONCRETE_FIELD = "type_instability_non_concrete_field"
    UNTYPED_GLOBAL_MUTATION = "untyped_global_mutation"
    HOT_LOOP_ARRAY_ALLOCATION = "hot_loop_array_allocation"
    SWALLOWED_TASK_EXCEPTION = "swallowed_task_exception"
    UNSYNCHRONIZED_GLOBAL_RACE = "unsynchronized_global_race"

    # 9. SOLID & Quality Principles
    MONOLITHIC_STRUCT_SRP = "monolithic_struct_srp"
    FAT_ABSTRACT_TYPE_ISP = "fat_abstract_type_isp"
    MANUAL_TYPE_BRANCH_CASCADE_OCP = "manual_type_branch_cascade_ocp"
    KISS_CYCLOMATIC_COMPLEXITY = "kiss_cyclomatic_complexity"
    KISS_LONG_PARAMETER_LIST = "kiss_long_parameter_list"
    DRY_DUPLICATE_LOGIC = "dry_duplicate_logic"
    DEMETER_LAW_TRAIN_WRECK = "demeter_law_train_wreck"


class ConfidenceLevel(str, Enum):
    """Normalized confidence tiers for detection ranking."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"


@dataclass(frozen=True)
class SourceLocation:
    """Precise source code location in a Julia file (.jl)."""

    file_path: str
    line: int
    column: int = 1

    def __str__(self) -> str:
        return f"{self.file_path}:{self.line}:{self.column}"


@dataclass(frozen=True)
class Evidence:
    """Individual heuristic signal contributing to pattern confidence."""

    rule_code: str
    description: str
    weight: float
    location: SourceLocation | None = None


@dataclass
class Confidence:
    """Calculated confidence rating aggregating evidence items."""

    score: float
    evidences: list[Evidence] = field(default_factory=list)

    @property
    def level(self) -> ConfidenceLevel:
        if self.score >= 0.85:
            return ConfidenceLevel.VERY_HIGH
        if self.score >= 0.70:
            return ConfidenceLevel.HIGH
        if self.score >= 0.50:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    @property
    def percentage(self) -> int:
        return int(round(self.score * 100))

    @property
    def percentage_str(self) -> str:
        return f"{self.percentage}%"
