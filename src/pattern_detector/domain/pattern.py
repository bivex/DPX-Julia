"""Julia architectural patterns catalog with descriptions and GoF equivalents."""

from __future__ import annotations

from dataclasses import dataclass
from pattern_detector.domain.value_objects import PatternCategory, PatternType


@dataclass(frozen=True)
class PatternDefinition:
    """Catalog entry describing a Julia architectural pattern."""

    type: PatternType
    category: PatternCategory
    name: str
    description: str
    gof_equivalent: str | None = None
    julia_version: str = "1.6 - 1.11+"
    recommendation: str | None = None


PATTERN_CATALOG: dict[PatternType, PatternDefinition] = {
    # 1. Julia Idiomatic Patterns
    PatternType.HOLY_TRAITS_DISPATCH: PatternDefinition(
        type=PatternType.HOLY_TRAITS_DISPATCH,
        category=PatternCategory.JULIA_IDIOMATIC,
        name="Holy Traits Pattern",
        description="Compile-time trait dispatch over singleton trait types enabling orthogonal interface specialization.",
        gof_equivalent="Strategy / Adapter",
    ),
    PatternType.PARAMETRIC_TYPE_SPECIALIZATION: PatternDefinition(
        type=PatternType.PARAMETRIC_TYPE_SPECIALIZATION,
        category=PatternCategory.JULIA_IDIOMATIC,
        name="Parametric Type Specialization (`struct Foo{T} ... end`)",
        description="Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.",
        gof_equivalent="Generics / Template",
    ),
    PatternType.METAPROGRAMMING_MACRO_DSL: PatternDefinition(
        type=PatternType.METAPROGRAMMING_MACRO_DSL,
        category=PatternCategory.JULIA_IDIOMATIC,
        name="Metaprogramming Macro DSL (`macro ...`)",
        description="Compile-time AST transformation creating expressive domain-specific languages without runtime penalty.",
        gof_equivalent="Interpreter / Compiler",
    ),
    PatternType.HOMOICONIC_AST_TRANSFORM: PatternDefinition(
        type=PatternType.HOMOICONIC_AST_TRANSFORM,
        category=PatternCategory.JULIA_IDIOMATIC,
        name="Homoiconic AST Transformation (`Expr(:call, ...)`)",
        description="Code-as-data manipulation constructing or evaluating runtime Julia expressions.",
        gof_equivalent="Interpreter / Code Generator",
    ),
    PatternType.BROADCAST_OPERATOR_OVERLOAD: PatternDefinition(
        type=PatternType.BROADCAST_OPERATOR_OVERLOAD,
        category=PatternCategory.JULIA_IDIOMATIC,
        name="Broadcast Operator Protocol (`Base.broadcasted`)",
        description="Custom vectorized broadcasting protocol fusing array and container operations.",
        gof_equivalent="Iterator / Composite",
    ),
    PatternType.CONVERSION_PROMOTION_PROTOCOL: PatternDefinition(
        type=PatternType.CONVERSION_PROMOTION_PROTOCOL,
        category=PatternCategory.JULIA_IDIOMATIC,
        name="Conversion & Promotion Protocol (`Base.convert` / `Base.promote_rule`)",
        description="Idiomatic numeric and domain type coercion conforming to Julia's core type promotion engine.",
        gof_equivalent="Adapter",
    ),

    # 2. Multiple Dispatch Core Paradigms
    PatternType.MULTIPLE_DISPATCH_POLYMORPHISM: PatternDefinition(
        type=PatternType.MULTIPLE_DISPATCH_POLYMORPHISM,
        category=PatternCategory.MULTIPLE_DISPATCH,
        name="Multiple Dispatch Polymorphism",
        description="Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.",
        gof_equivalent="Visitor / Strategy",
    ),
    PatternType.OUTER_CONSTRUCTOR_DISPATCH: PatternDefinition(
        type=PatternType.OUTER_CONSTRUCTOR_DISPATCH,
        category=PatternCategory.MULTIPLE_DISPATCH,
        name="Outer Constructor Method Dispatch",
        description="Polymorphic constructors defined outside struct definition specializing instantiation protocols.",
        gof_equivalent="Factory Method",
    ),
    PatternType.METHOD_SPECIALIZATION_TABLE: PatternDefinition(
        type=PatternType.METHOD_SPECIALIZATION_TABLE,
        category=PatternCategory.MULTIPLE_DISPATCH,
        name="Method Specialization Table (Generic Function Extension)",
        description="Extending generic functions across multiple concrete types forming open polymorphic protocols.",
        gof_equivalent="Open Multi-Methods",
    ),

    # 3. Concurrency & Parallelism
    PatternType.TASK_ASYNC_COROUTINE: PatternDefinition(
        type=PatternType.TASK_ASYNC_COROUTINE,
        category=PatternCategory.CONCURRENCY_PARALLELISM,
        name="Task Asynchronous Coroutine (`@async` / `@sync`)",
        description="Lightweight cooperative green threads yielding cooperatively without blocking the OS thread.",
        gof_equivalent="Async Continuation",
    ),
    PatternType.CHANNEL_CSP_PIPELINE: PatternDefinition(
        type=PatternType.CHANNEL_CSP_PIPELINE,
        category=PatternCategory.CONCURRENCY_PARALLELISM,
        name="Channel CSP Pipeline (`Channel{T}`)",
        description="Thread-safe communicating sequential processes pipeline passing messages between tasks.",
        gof_equivalent="Producer-Consumer / Pipeline",
    ),
    PatternType.THREADS_PARALLEL_LOOP: PatternDefinition(
        type=PatternType.THREADS_PARALLEL_LOOP,
        category=PatternCategory.CONCURRENCY_PARALLELISM,
        name="Multithreading Parallel Loop (`Threads.@threads`)",
        description="Work-stealing shared-memory parallel computing over thread pools.",
        gof_equivalent="Fork-Join Parallelism",
    ),
    PatternType.ATOMIC_MEMORY_OPERATION: PatternDefinition(
        type=PatternType.ATOMIC_MEMORY_OPERATION,
        category=PatternCategory.CONCURRENCY_PARALLELISM,
        name="Atomic Memory Synchronization (`Threads.Atomic` / `@atomic`)",
        description="Lock-free thread-safe primitives coordinating shared state mutations.",
        gof_equivalent="Lock-Free State",
    ),

    # 4. Scientific & High-Performance Patterns
    PatternType.ZERO_ALLOCATION_VIEW: PatternDefinition(
        type=PatternType.ZERO_ALLOCATION_VIEW,
        category=PatternCategory.SCIENTIFIC_PERFORMANCE,
        name="Zero-Allocation Array View (`@views` / `view()`)",
        description="Array slicing without memory allocation, eliminating GC pressure in numerical workloads.",
        gof_equivalent="Flyweight / Sub-Array",
    ),
    PatternType.IN_PLACE_MUTATING_CONVENTION: PatternDefinition(
        type=PatternType.IN_PLACE_MUTATING_CONVENTION,
        category=PatternCategory.SCIENTIFIC_PERFORMANCE,
        name="In-Place Mutating Convention (`foo!(...)`)",
        description="Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.",
        gof_equivalent="Memory Buffer Reuse",
    ),
    PatternType.CALLABLE_STRUCT_FUNCTOR: PatternDefinition(
        type=PatternType.CALLABLE_STRUCT_FUNCTOR,
        category=PatternCategory.SCIENTIFIC_PERFORMANCE,
        name="Callable Struct Functor (`(obj::Type)(x)`)",
        description="Struct instance acting as an invokable function encapsulating parameters or precomputed state.",
        gof_equivalent="Function Object / Command",
    ),

    # 5. GoF Creational Patterns
    PatternType.SINGLETON_IMMUTABLE_INSTANCE: PatternDefinition(
        type=PatternType.SINGLETON_IMMUTABLE_INSTANCE,
        category=PatternCategory.CREATIONAL,
        name="Immutable Singleton Instance (`struct Singleton end` / `const instance`)",
        description="Singleton instance represented as zero-field immutable struct or constant reference.",
        gof_equivalent="Singleton",
    ),
    PatternType.FACTORY_METHOD_CONSTRUCTOR: PatternDefinition(
        type=PatternType.FACTORY_METHOD_CONSTRUCTOR,
        category=PatternCategory.CREATIONAL,
        name="Factory Method Constructor",
        description="Parametric outer constructor function selecting and instantiating appropriate subtype.",
        gof_equivalent="Factory Method",
    ),
    PatternType.ABSTRACT_FACTORY_HIERARCHY: PatternDefinition(
        type=PatternType.ABSTRACT_FACTORY_HIERARCHY,
        category=PatternCategory.CREATIONAL,
        name="Abstract Factory Hierarchy",
        description="Abstract type hierarchy grouping constructor families for related components.",
        gof_equivalent="Abstract Factory",
    ),
    PatternType.BUILDER_FLUENT_STRUCT: PatternDefinition(
        type=PatternType.BUILDER_FLUENT_STRUCT,
        category=PatternCategory.CREATIONAL,
        name="Fluent Struct Builder",
        description="Step-by-step struct constructor chaining parameters prior to final instantiation.",
        gof_equivalent="Builder",
    ),
    PatternType.PROTOTYPE_DEEPCOPY: PatternDefinition(
        type=PatternType.PROTOTYPE_DEEPCOPY,
        category=PatternCategory.CREATIONAL,
        name="Prototype Deepcopy (`deepcopy()` / Copy Constructor)",
        description="Object duplication creating isolated clones with identical state.",
        gof_equivalent="Prototype",
    ),

    # 6. GoF Structural Patterns
    PatternType.ADAPTER_WRAPPER_STRUCT: PatternDefinition(
        type=PatternType.ADAPTER_WRAPPER_STRUCT,
        category=PatternCategory.STRUCTURAL,
        name="Adapter via Wrapper Struct",
        description="Wrapper struct adapting an external or foreign type to domain abstract contracts.",
        gof_equivalent="Adapter",
    ),
    PatternType.BRIDGE_DRIVER_DECOUPLING: PatternDefinition(
        type=PatternType.BRIDGE_DRIVER_DECOUPLING,
        category=PatternCategory.STRUCTURAL,
        name="Bridge Driver Decoupling",
        description="Decouples high-level domain abstraction from low-level execution driver / renderer.",
        gof_equivalent="Bridge",
    ),
    PatternType.COMPOSITE_STRUCT_TREE: PatternDefinition(
        type=PatternType.COMPOSITE_STRUCT_TREE,
        category=PatternCategory.STRUCTURAL,
        name="Composite Struct Tree",
        description="Recursive tree structure treating individual leaf nodes and composite groups uniformly.",
        gof_equivalent="Composite",
    ),
    PatternType.DECORATOR_FORWARDING_WRAPPER: PatternDefinition(
        type=PatternType.DECORATOR_FORWARDING_WRAPPER,
        category=PatternCategory.STRUCTURAL,
        name="Decorator Forwarding Wrapper",
        description="Augments behavior of an inner struct by forwarding core calls and layering additional logic.",
        gof_equivalent="Decorator",
    ),
    PatternType.FACADE_COORDINATOR_MODULE: PatternDefinition(
        type=PatternType.FACADE_COORDINATOR_MODULE,
        category=PatternCategory.STRUCTURAL,
        name="Facade Coordinator Module",
        description="Unified module API orchestrating multiple underlying subsystems, solvers, or data sources.",
        gof_equivalent="Facade",
    ),
    PatternType.FLYWEIGHT_POOL_CACHE: PatternDefinition(
        type=PatternType.FLYWEIGHT_POOL_CACHE,
        category=PatternCategory.STRUCTURAL,
        name="Flyweight Pooling Cache",
        description="Sharing immutable instances via dictionary cache or memoization to save memory.",
        gof_equivalent="Flyweight",
    ),
    PatternType.PROXY_LAZY_OR_REMOTE: PatternDefinition(
        type=PatternType.PROXY_LAZY_OR_REMOTE,
        category=PatternCategory.STRUCTURAL,
        name="Proxy Lazy / Remote Surrogate",
        description="Surrogate struct controlling access or delaying evaluation of expensive target resources.",
        gof_equivalent="Proxy",
    ),

    # 7. GoF Behavioral Patterns
    PatternType.CHAIN_OF_RESPONSIBILITY_PIPELINE: PatternDefinition(
        type=PatternType.CHAIN_OF_RESPONSIBILITY_PIPELINE,
        category=PatternCategory.BEHAVIORAL,
        name="Chain of Responsibility Pipeline",
        description="Sequence of middleware/handler structs passing requests along an execution chain.",
        gof_equivalent="Chain of Responsibility",
    ),
    PatternType.COMMAND_CALLABLE_TASK: PatternDefinition(
        type=PatternType.COMMAND_CALLABLE_TASK,
        category=PatternCategory.BEHAVIORAL,
        name="Command Callable Task",
        description="Encapsulates an operation and its execution arguments into an invokable struct.",
        gof_equivalent="Command",
    ),
    PatternType.INTERPRETER_AST_EVAL: PatternDefinition(
        type=PatternType.INTERPRETER_AST_EVAL,
        category=PatternCategory.BEHAVIORAL,
        name="Interpreter Pattern (AST Evaluator)",
        description="Evaluates domain expressions or grammars through recursive multiple dispatch over AST types.",
        gof_equivalent="Interpreter",
    ),
    PatternType.ITERATOR_BASE_PROTOCOL: PatternDefinition(
        type=PatternType.ITERATOR_BASE_PROTOCOL,
        category=PatternCategory.BEHAVIORAL,
        name="Iterator Protocol (`Base.iterate`)",
        description="Julia collection traversal protocol implementing `Base.iterate(iter, state)`.",
        gof_equivalent="Iterator",
    ),
    PatternType.MEDIATOR_CENTRAL_COORDINATOR: PatternDefinition(
        type=PatternType.MEDIATOR_CENTRAL_COORDINATOR,
        category=PatternCategory.BEHAVIORAL,
        name="Mediator Coordinator",
        description="Central coordinator mediating interaction and event dispatching between decoupled components.",
        gof_equivalent="Mediator",
    ),
    PatternType.MEMENTO_STATE_SNAPSHOT: PatternDefinition(
        type=PatternType.MEMENTO_STATE_SNAPSHOT,
        category=PatternCategory.BEHAVIORAL,
        name="Memento State Snapshot",
        description="Captures and restores internal state snapshots without violating encapsulation.",
        gof_equivalent="Memento",
    ),
    PatternType.OBSERVER_CHANNEL_SUBSCRIPTION: PatternDefinition(
        type=PatternType.OBSERVER_CHANNEL_SUBSCRIPTION,
        category=PatternCategory.BEHAVIORAL,
        name="Observer Channel Subscription",
        description="Event broadcasting mechanism publishing updates to subscribed channels or callback registries.",
        gof_equivalent="Observer",
    ),
    PatternType.STATE_ABSTRACT_TYPE_FSM: PatternDefinition(
        type=PatternType.STATE_ABSTRACT_TYPE_FSM,
        category=PatternCategory.BEHAVIORAL,
        name="Abstract Type State Machine",
        description="Finite state machine where state transitions dispatch over an abstract state type hierarchy.",
        gof_equivalent="State",
    ),
    PatternType.STRATEGY_TRAIT_ALGORITHM: PatternDefinition(
        type=PatternType.STRATEGY_TRAIT_ALGORITHM,
        category=PatternCategory.BEHAVIORAL,
        name="Strategy Trait / Function Injection",
        description="Interchangeable algorithm strategies selected via trait dispatch or higher-order function arguments.",
        gof_equivalent="Strategy",
    ),
    PatternType.TEMPLATE_METHOD_SKELETON: PatternDefinition(
        type=PatternType.TEMPLATE_METHOD_SKELETON,
        category=PatternCategory.BEHAVIORAL,
        name="Template Method Skeleton",
        description="Generic algorithm skeleton orchestrating overridable step hooks resolved via dispatch.",
        gof_equivalent="Template Method",
    ),
    PatternType.VISITOR_MULTIPLE_DISPATCH: PatternDefinition(
        type=PatternType.VISITOR_MULTIPLE_DISPATCH,
        category=PatternCategory.BEHAVIORAL,
        name="Visitor Multiple Dispatch",
        description="Multiple dispatch double-dispatching operations across AST or type node hierarchies.",
        gof_equivalent="Visitor",
    ),

    # 8. Resilience, Type Stability & Performance Hazards
    PatternType.TYPE_INSTABILITY_NON_CONCRETE_FIELD: PatternDefinition(
        type=PatternType.TYPE_INSTABILITY_NON_CONCRETE_FIELD,
        category=PatternCategory.RESILIENCE,
        name="Type Instability: Non-Concrete Field in Struct",
        description="Struct field defined with abstract type or untyped `Any`, causing boxing and runtime dispatch.",
        recommendation="Use parametric type parameterization: `struct Foo{T} x::T end`.",
    ),
    PatternType.UNTYPED_GLOBAL_MUTATION: PatternDefinition(
        type=PatternType.UNTYPED_GLOBAL_MUTATION,
        category=PatternCategory.RESILIENCE,
        name="Non-Const Global Variable Mutation Hazard",
        description="Mutating non-`const` global variables causing compiler de-optimization and data races.",
        recommendation="Declare constants with `const` or encapsulate in a state struct.",
    ),
    PatternType.HOT_LOOP_ARRAY_ALLOCATION: PatternDefinition(
        type=PatternType.HOT_LOOP_ARRAY_ALLOCATION,
        category=PatternCategory.RESILIENCE,
        name="Hot Loop Array Allocation Hazard",
        description="Allocating new array slices in hot numerical loops instead of `@views` or mutating in-place (`!`).",
        recommendation="Use `@views` for slicing or preallocate output buffers.",
    ),
    PatternType.SWALLOWED_TASK_EXCEPTION: PatternDefinition(
        type=PatternType.SWALLOWED_TASK_EXCEPTION,
        category=PatternCategory.RESILIENCE,
        name="Unsynchronized Background Task Hazard",
        description="Launching `@async` tasks without enclosing `@sync` or `wait()`, causing unhandled exceptions to be lost.",
        recommendation="Wrap concurrent tasks in `@sync begin ... end` or explicitly `wait(task)`.",
    ),
    PatternType.UNSYNCHRONIZED_GLOBAL_RACE: PatternDefinition(
        type=PatternType.UNSYNCHRONIZED_GLOBAL_RACE,
        category=PatternCategory.RESILIENCE,
        name="Unsynchronized Concurrent Mutation Race",
        description="Modifying shared arrays or variables inside `Threads.@threads` without locks or atomic operations.",
        recommendation="Use `Threads.Atomic` or thread-local accumulator buffers.",
    ),

    # 9. SOLID & Quality Principles
    PatternType.MONOLITHIC_STRUCT_SRP: PatternDefinition(
        type=PatternType.MONOLITHIC_STRUCT_SRP,
        category=PatternCategory.PRINCIPLE,
        name="SRP Violation: Monolithic Struct / God Object",
        description="Struct containing excessive fields or responsibilities, violating Single Responsibility Principle.",
        recommendation="Decompose into cohesive domain sub-structs.",
    ),
    PatternType.FAT_ABSTRACT_TYPE_ISP: PatternDefinition(
        type=PatternType.FAT_ABSTRACT_TYPE_ISP,
        category=PatternCategory.PRINCIPLE,
        name="ISP Violation: Fat Abstract Type Contract",
        description="Abstract type expecting too many mandatory method implementations.",
        recommendation="Decompose into Holy Traits or smaller abstract hierarchies.",
    ),
    PatternType.MANUAL_TYPE_BRANCH_CASCADE_OCP: PatternDefinition(
        type=PatternType.MANUAL_TYPE_BRANCH_CASCADE_OCP,
        category=PatternCategory.PRINCIPLE,
        name="OCP Violation: Manual `isa` / `typeof` Branching Cascade",
        description="Using repeated `if x isa TypeA ... elseif x isa TypeB` instead of Multiple Dispatch.",
        recommendation="Replace manual `isa` cascades with multiple dispatch method definitions.",
    ),
    PatternType.KISS_CYCLOMATIC_COMPLEXITY: PatternDefinition(
        type=PatternType.KISS_CYCLOMATIC_COMPLEXITY,
        category=PatternCategory.PRINCIPLE,
        name="KISS Violation: High Cyclomatic Complexity",
        description="Function containing excessive branching logic (> 8 decision branches).",
        recommendation="Refactor into smaller helper functions or dispatch methods.",
    ),
    PatternType.KISS_LONG_PARAMETER_LIST: PatternDefinition(
        type=PatternType.KISS_LONG_PARAMETER_LIST,
        category=PatternCategory.PRINCIPLE,
        name="KISS Violation: Long Parameter List",
        description="Function accepting >= 6 positional parameters.",
        recommendation="Group related arguments into a configuration struct.",
    ),
    PatternType.DRY_DUPLICATE_LOGIC: PatternDefinition(
        type=PatternType.DRY_DUPLICATE_LOGIC,
        category=PatternCategory.PRINCIPLE,
        name="DRY Violation: Duplicate Code Logic",
        description="Duplicated algorithmic blocks across multiple functions.",
        recommendation="Extract common logic into reusable generic function.",
    ),
    PatternType.DEMETER_LAW_TRAIN_WRECK: PatternDefinition(
        type=PatternType.DEMETER_LAW_TRAIN_WRECK,
        category=PatternCategory.PRINCIPLE,
        name="Law of Demeter Violation (Deep Field Navigation)",
        description="Deeply nested field access chains (`a.b.c.d.e`), violating encapsulation.",
        recommendation="Provide direct accessor methods following 'Tell, Don't Ask'.",
    ),
}
