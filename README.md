# 🎯 DPX-Julia: Multiple Dispatch, Holy Traits, Metaprogramming, Tasks, GoF & High-Performance Architectural Pattern Detector

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Julia Version](https://img.shields.io/badge/Julia-1.6%20--%201.11+-9558B2?logo=julia&logoColor=white)](https://julialang.org/)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Architecture: Hexagonal DDD](https://img.shields.io/badge/Architecture-Hexagonal%20DDD-blueviolet)](https://alistair.cockburn.us/hexagonal-architecture/)
[![CLI: Typer & Rich](https://img.shields.io/badge/CLI-Typer%20%26%20Rich-009688)](https://typer.tiangolo.com)
[![SARIF OASIS v2.1.0](https://img.shields.io/badge/SARIF-OASIS%20v2.1.0-blue)](https://sarifweb.azurewebsites.net)

**DPX-Julia** is an enterprise-grade static analysis engine and architectural pattern detector for Julia codebases. Designed for **Scientific Computing, Machine Learning (Flux/SciML), High-Performance Numerical Systems, Distributed Computing, and Package Development**, it analyzes **Multiple Dispatch Polymorphism, Holy Traits Pattern, Parametric Type Layouts, Metaprogramming Macros, Tasks & Channel Concurrency, all 23 GoF Design Patterns**, and **Julia Performance & Type Instability Hazards (Abstract struct fields, non-const global mutations, hot loop heap allocations, unconfined tasks)**.

[Features](#-key-features) • [Installation](#-installation) • [CLI Usage](#-cli-usage) • [Supported Rules](#-supported-pattern-rules--checks) • [The DPX Suite Family](#-the-dpx-suite-family)

</div>

---

## 🌟 Key Features

- 🧬 **Multiple Dispatch & Julia Idioms:** Analyzes multi-argument dynamic method specialization, outer constructors, Holy Traits pattern (compile-time trait dispatch), parametric type layouts (`struct Foo{T} ... end`), and conversion/promotion protocols.
- ⚡ **Metaprogramming & Macros:** Inspects homoiconic code-as-data manipulation (`Expr(:call, ...)`, `Meta.parse`), domain DSL macros (`macro ... end`), and broadcast fusion protocols (`Base.broadcasted`).
- 🌊 **Concurrency & Parallelism:** Audits lightweight asynchronous tasks (`@async`, `@sync`), CSP pipeline channels (`Channel{T}`), multithreaded loop parallelization (`Threads.@threads`), and lock-free atomic memory operations (`Threads.Atomic`).
- 🔬 **Scientific Performance & Zero-Allocation:** Detects `@views` / `view()` sub-arrays, in-place mutating conventions (`foo!(...)`), and callable struct functors (`(obj::MyStruct)(x)`).
- 🏛️ **100% Complete Gang of Four (GoF 23/23):** Comprehensive detection of all 23 classic Creational, Structural, and Behavioral patterns adapted for Julia's functional-multiple-dispatch paradigm.
- 🛡️ **Type Instability & Performance Hazard Detection:** Identifies non-concrete abstract fields in structs, non-`const` global variable mutations, array allocations inside hot numerical loops, swallowed task exceptions, and unsynchronized concurrent data races.
- 📊 **Interactive Architecture Observability HUD:** Zero-dependency interactive HTML dashboard with instant search, KPI breakdown, and built-in **`🤖 Copy AI Context Prompt`** generator for LLMs (Claude, GPT-4, Gemini).
- 🔒 **CI/CD & GitHub Security Ready:** Standardized **OASIS SARIF v2.1.0**, JSON, and Markdown reports.

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/bivex/DPX-Julia.git
cd DPX-Julia

# Install dependencies using uv or pip
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

---

## 💻 CLI Usage

### 1. Scan a Julia Project or Scientific Package
```bash
# Terminal scan with Rich formatting
dpx-julia scan /path/to/julia/package

# Generate interactive HTML HUD Dashboard
dpx-julia scan /path/to/julia/package -H reports/julia_hud.html

# Generate AI Context Prompt for LLMs
dpx-julia scan /path/to/julia/package --llm

# Filter for specific Holy Traits or Type Instability patterns
dpx-julia scan /path/to/julia/package -p holy_traits_dispatch -p type_instability_non_concrete_field

# Export SARIF for GitHub Code Scanning
dpx-julia scan /path/to/julia/package -S reports/results.sarif
```

### 2. Inspect Supported Architectural Rules
```bash
dpx-julia rules
```

### 3. Query Deep Pattern Documentation
```bash
dpx-julia info holy_traits_dispatch
dpx-julia info type_instability_non_concrete_field
```

---

## 📋 Supported Pattern Rules & Checks

### 1. 🧬 Julia Idiomatic Patterns
- `holy_traits_dispatch`: Compile-time trait dispatch over singleton trait types.
- `parametric_type_specialization`: Parametric struct specialization ensuring concrete memory layouts.
- `metaprogramming_macro_dsl`: Compile-time AST domain DSL generation.
- `homoiconic_ast_transform`: Homoiconic code-as-data manipulation (`Expr`, `Meta.parse`).
- `broadcast_operator_overload`: Custom vectorized broadcasting protocol (`Base.broadcasted`).
- `conversion_promotion_protocol`: Standard conversion and promotion hooks (`Base.convert`).

### 2. ⚡ Multiple Dispatch Core Paradigms
- `multiple_dispatch_polymorphism`: Multi-argument dynamic method dispatch over operand types.
- `outer_constructor_dispatch`: Outer constructor method specialization.
- `method_specialization_table`: Generic functions extended across multiple method signatures.

### 3. 🌊 Concurrency & Parallelism
- `task_async_coroutine`: Lightweight cooperative green threads (`@async` / `@sync`).
- `channel_csp_pipeline`: Thread-safe CSP communicating sequential processes (`Channel{T}`).
- `threads_parallel_loop`: Shared-memory loop parallelization (`Threads.@threads for`).
- `atomic_memory_operation`: Lock-free atomic synchronization (`Threads.Atomic` / `@atomic`).

### 4. 🔬 Scientific Performance
- `zero_allocation_view`: Zero-allocation array slicing views (`@views` / `view()`).
- `in_place_mutating_convention`: In-place mutating functions modifying arguments (`foo!(...)`).
- `callable_struct_functor`: Struct instance acting as an invocable function (`(obj::Type)(x)`).

### 5. 🏛️ GoF Creational Patterns (5/5)
- `singleton_immutable_instance`: Type-level zero-field immutable Singleton or const instance.
- `factory_method_constructor`: Factory Method constructor instantiating polymorphic subtypes.
- `abstract_factory_hierarchy`: Abstract type hierarchy grouping constructor families.
- `builder_fluent_struct`: Step-by-step struct parameter accumulation builder.
- `prototype_deepcopy`: Prototype cloning via `deepcopy()` or copy constructors.

### 6. 🧱 GoF Structural Patterns (7/7)
- `adapter_wrapper_struct`: Struct adapting foreign types to domain abstract contracts.
- `bridge_driver_decoupling`: Decoupling abstraction from implementor execution drivers.
- `composite_struct_tree`: Recursive component and node tree hierarchies.
- `decorator_forwarding_wrapper`: Struct forwarding inner calls and layering behavior.
- `facade_coordinator_module`: Unified module API coordinating multiple subsystems.
- `flyweight_pool_cache`: Fine-grained instance sharing via dictionary cache.
- `proxy_lazy_or_remote`: Surrogate struct controlling access or delaying evaluation.

### 7. 🎯 GoF Behavioral Patterns (11/11)
- `chain_of_responsibility_pipeline`: Middleware/handler structs passing requests along a chain.
- `command_callable_task`: Command objects encapsulated as callable structs/tasks.
- `interpreter_ast_eval`: Domain expression AST evaluation via multiple dispatch.
- `iterator_base_protocol`: Julia collection traversal protocol (`Base.iterate`).
- `mediator_central_coordinator`: Central event coordinator mediating subsystem interaction.
- `memento_state_snapshot`: Internal state capture and restoration snapshot.
- `observer_channel_subscription`: Event broadcasting to subscribed channels or callback registries.
- `state_abstract_type_fsm`: State machine dispatching over abstract state type hierarchies.
- `strategy_trait_algorithm`: Interchangeable strategy algorithm selection via traits.
- `template_method_skeleton`: Algorithm skeleton coordinating overridable step hooks.
- `visitor_multiple_dispatch`: Double-dispatch operations over AST node hierarchies.

### 8. 🛡️ Resilience, Type Stability & Performance Hazards
- `type_instability_non_concrete_field`: Abstract/untyped field in struct causing runtime boxing.
- `untyped_global_mutation`: Non-const global variable mutation causing de-optimization.
- `hot_loop_array_allocation`: Allocating new arrays inside hot loops instead of `@views`.
- `swallowed_task_exception`: Unconfined `@async` tasks without `@sync` or `wait()`.
- `unsynchronized_global_race`: Mutating shared arrays in `Threads.@threads` without locks.

### 9. 📐 SOLID & Code Quality Principles
- `monolithic_struct_srp`: Struct declaring too many fields, violating SRP.
- `fat_abstract_type_isp`: Abstract type expecting too many mandatory method implementations.
- `manual_type_branch_cascade_ocp`: Manual `if x isa TypeA ... elseif` violating Multiple Dispatch.
- `kiss_cyclomatic_complexity`: High cyclomatic complexity (> 8 branch points).
- `kiss_long_parameter_list`: Functions with excessive parameters (>= 6).
- `dry_duplicate_logic`: Duplicated algorithmic sequences across functions.
- `demeter_law_train_wreck`: Law of Demeter deep field access chains (`a.b.c.d.e`).

---

---

## 🌐 The DPX Multi-Language Static Analysis Family (33 Languages)

| # | Language | Repository | Ecosystem & Focus |
|:---:|---|---|---|
| 1 | **Ada** | [`bivex/DPX-Ada`](https://github.com/bivex/DPX-Ada) | Ada 2012/2022, SPARK Contracts, Ravenscar Tasking, DO-178C Safety |
| 2 | **Clojure** | [`bivex/DPX`](https://github.com/bivex/DPX) | Lisp S-Expressions, Protocols, Multimethods |
| 3 | **C** | [`bivex/DPX-C`](https://github.com/bivex/DPX-C) | Memory Safety, Struct VTables, Idiomatic C11/C23 |
| 4 | **Cairo** | [`bivex/DPX-Cairo`](https://github.com/bivex/DPX-Cairo) | Starknet Smart Contracts, ZK-Rollup Invariants |
| 5 | **C++** | [`bivex/DPX-Cpp`](https://github.com/bivex/DPX-Cpp) | RAII, CRTP, Concepts, Modern C++20/23 |
| 6 | **C#** | [`bivex/DPX-CSharp`](https://github.com/bivex/DPX-CSharp) | .NET 9, Roslyn AST, Linq, Records |
| 7 | **Dart** | [`bivex/DPX-Dart`](https://github.com/bivex/DPX-Dart) | Dart 3.x, Flutter, BLoC, Riverpod, Isolates |
| 8 | **Elixir** | [`bivex/DPX-Elixir`](https://github.com/bivex/DPX-Elixir) | BEAM OTP, GenServer, Supervisors |
| 9 | **Erlang** | [`bivex/DPX-Erlang`](https://github.com/bivex/DPX-Erlang) | Fault Tolerance, Actor Model, OTP Behaviors |
| 10 | **Gleam** | [`bivex/DPX-Gleam`](https://github.com/bivex/DPX-Gleam) | Type-Safe BEAM, Actor Concurrency |
| 11 | **Go** | [`bivex/DPX-Go`](https://github.com/bivex/DPX-Go) | Goroutines, Channels, Composition, Interfaces |
| 12 | **Haskell** | [`bivex/DPX-Haskell`](https://github.com/bivex/DPX-Haskell) | Pure Functional, Monads, Typeclasses, Arrows |
| 13 | **Huff** | [`bivex/DPX-Huff`](https://github.com/bivex/DPX-Huff) | Low-Level EVM Bytecode & Opcodes |
| 14 | **Idris 2** | [`bivex/DPX-Idris2`](https://github.com/bivex/DPX-Idris2) | Dependent Types, QTT Linear Protocols, Totality, Proofs |
| 15 | **Java** | [`bivex/DPX-Java`](https://github.com/bivex/DPX-Java) | Spring Boot, Enterprise Java, JVM Invariants |
| 16 | **Julia** | [`bivex/DPX-Julia`](https://github.com/bivex/DPX-Julia) | Multiple Dispatch, Scientific Computing |
| 17 | **Kotlin** | [`bivex/DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin) | Coroutines, Multiplatform, Functional DSLs |
| 18 | **Lua** | [`bivex/DPX-Lua`](https://github.com/bivex/DPX-Lua) | Metatables, Coroutines, LuaJIT, Neovim |
| 19 | **Mojo** | [`bivex/DPX-Mojo`](https://github.com/bivex/DPX-Mojo) | SIMD Hardware, Memory Lifetimes, AI Systems |
| 20 | **Move** | [`bivex/DPX-Move`](https://github.com/bivex/DPX-Move) | Aptos & Sui Resource Safety, Linear Types |
| 21 | **OCaml** | [`bivex/DPX-OCaml`](https://github.com/bivex/DPX-OCaml) | Algebraic Data Types, Functors, Polymorphism |
| 22 | **PHP** | [`bivex/DPX-Php`](https://github.com/bivex/DPX-Php) | Modern PHP 8.4, Attributes, Traits, Laravel |
| 23 | **Prolog** | [`bivex/DPX-Prolog`](https://github.com/bivex/DPX-Prolog) | ISO Prolog, SWI-Prolog, DCG, CLP(FD/R/Q), CHR, Meta-Interpreters |
| 24 | **Puppet** | [`bivex/DPX-Puppet`](https://github.com/bivex/DPX-Puppet) | Puppet DSL, Roles/Profiles, IaC Security, Hiera |
| 25 | **Python** | [`bivex/DPX-Py`](https://github.com/bivex/DPX-Py) | Metaprogramming, Protocols, Hexagonal DDD |
| 26 | **Ruby** | [`bivex/DPX-Ruby`](https://github.com/bivex/DPX-Ruby) | Ruby 3.x, Rails, Metaprogramming, Dry-RB, Security |
| 27 | **Rust** | [`bivex/DPX-Rust`](https://github.com/bivex/DPX-Rust) | Zero-Cost Abstractions, Borrow Checker, Traits |
| 28 | **Solidity** | [`bivex/DPX-Solidity`](https://github.com/bivex/DPX-Solidity) | DeFi Security, Reentrancy, EVM Yul/Assembly |
| 29 | **SQL** | [`bivex/DPX-SQL`](https://github.com/bivex/DPX-SQL) | PostgreSQL, MySQL, SQLite, T-SQL, PL/SQL |
| 30 | **Swift** | [`bivex/DPX-Swift`](https://github.com/bivex/DPX-Swift) | Protocol-Oriented Programming, Actors |
| 31 | **TypeScript** | [`bivex/DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript) | Generics, Conditional Types, Clean Architecture |
| 32 | **Yul** | [`bivex/DPX-Yul`](https://github.com/bivex/DPX-Yul) | EVM Intermediate Representation Optimization |
| 33 | **Zig** | [`bivex/DPX-Zig`](https://github.com/bivex/DPX-Zig) | Comptime, Manual Memory Allocators, C ABI |

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
