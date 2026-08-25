# 🎯 DPX-Julia: Architectural Context & Pattern Report

- **Target Project:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src`
- **Scanned Files:** 26
- **Total Detections:** 456
- **Scan Time:** 0.017s

## 📊 Summary by Category

| Category | Detections |
|---|:---:|
| `multiple_dispatch` | 263 |
| `scientific_performance` | 118 |
| `julia_idiomatic` | 43 |
| `principle` | 18 |
| `creational` | 5 |
| `resilience` | 5 |
| `structural` | 4 |

## 🔍 Detailed Pattern Instances & Violations

### 1. parametric_type_specialization on `FluxEltypeAdaptor` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:120:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'FluxEltypeAdaptor{T}' specializes concrete memory layout across type parameters

### 2. parametric_type_specialization on `Conv` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:150:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'Conv{N, M, F, A, V}' specializes concrete memory layout across type parameters

### 3. parametric_type_specialization on `ConvTranspose` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:306:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'ConvTranspose{N, M, F, A, V}' specializes concrete memory layout across type parameters

### 4. parametric_type_specialization on `CrossCor` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:468:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'CrossCor{N, M, F, A, V}' specializes concrete memory layout across type parameters

### 5. parametric_type_specialization on `AdaptiveMaxPool` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:579:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'AdaptiveMaxPool{S, O}' specializes concrete memory layout across type parameters

### 6. parametric_type_specialization on `AdaptiveMeanPool` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:621:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'AdaptiveMeanPool{S, O}' specializes concrete memory layout across type parameters

### 7. parametric_type_specialization on `MaxPool` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:753:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'MaxPool{N, M}' specializes concrete memory layout across type parameters

### 8. parametric_type_specialization on `MeanPool` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:813:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'MeanPool{N, M}' specializes concrete memory layout across type parameters

### 9. parametric_type_specialization on `Chain` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:49:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'Chain{T<:Union{Tuple, NamedTuple, AbstractVector}' specializes concrete memory layout across type parameters

### 10. parametric_type_specialization on `Dropout` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:68:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'Dropout{F<:Real, D, R<:AbstractRNG}' specializes concrete memory layout across type parameters

### 11. parametric_type_specialization on `AlphaDropout` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:121:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'AlphaDropout{F, R<:AbstractRNG}' specializes concrete memory layout across type parameters

### 12. parametric_type_specialization on `LayerNorm` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:186:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'LayerNorm{F, D, T, N}' specializes concrete memory layout across type parameters

### 13. parametric_type_specialization on `BatchNorm` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:259:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'BatchNorm{F, V, N, W}' specializes concrete memory layout across type parameters

### 14. parametric_type_specialization on `Recurrence` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:61:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'Recurrence{S, M}' specializes concrete memory layout across type parameters

### 15. parametric_type_specialization on `RNNCell` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:145:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'RNNCell{F, I, H, V}' specializes concrete memory layout across type parameters

### 16. parametric_type_specialization on `RNN` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:276:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'RNN{S, M}' specializes concrete memory layout across type parameters

### 17. parametric_type_specialization on `LSTMCell` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:383:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'LSTMCell{I, H, V}' specializes concrete memory layout across type parameters

### 18. parametric_type_specialization on `LSTM` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:491:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'LSTM{S, M}' specializes concrete memory layout across type parameters

### 19. parametric_type_specialization on `GRUCell` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:586:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'GRUCell{I, H, V}' specializes concrete memory layout across type parameters

### 20. parametric_type_specialization on `GRU` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:685:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'GRU{S, M}' specializes concrete memory layout across type parameters

### 21. parametric_type_specialization on `GRUv3Cell` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:766:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'GRUv3Cell{I, H, V, HH}' specializes concrete memory layout across type parameters

### 22. parametric_type_specialization on `GRUv3` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:871:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'GRUv3{S, M}' specializes concrete memory layout across type parameters

### 23. parametric_type_specialization on `Upsample` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:33:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'Upsample{mode, S, T}' specializes concrete memory layout across type parameters

### 24. parametric_type_specialization on `MultiHeadAttention` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:68:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'MultiHeadAttention{P1, D, P2}' specializes concrete memory layout across type parameters

### 25. parametric_type_specialization on `ClipValue` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:727:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'ClipValue{T}' specializes concrete memory layout across type parameters

### 26. parametric_type_specialization on `ClipNorm` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:738:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'ClipNorm{T}' specializes concrete memory layout across type parameters

### 27. parametric_type_specialization on `FluxDistributedModel` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:192:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'FluxDistributedModel{M}' specializes concrete memory layout across type parameters

### 28. parametric_type_specialization on `DistributedOptimizer` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:286:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'DistributedOptimizer{B <: AbstractFluxDistributedBackend}' specializes concrete memory layout across type parameters

### 29. parametric_type_specialization on `MPIBackend` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/backend.jl:13:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'MPIBackend{C}' specializes concrete memory layout across type parameters

### 30. parametric_type_specialization on `NCCLBackend` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/backend.jl:30:1`
- **Summary:** Type parameterization ensuring concrete memory layout, SIMD vectorization, and zero runtime overhead.
- **Evidence Trail:**
  - `+95%` (JULIA_PARAMETRIC_SPECIALIZATION): Struct 'NCCLBackend{C, M <: Union{Nothing, MPIBackend}' specializes concrete memory layout across type parameters

### 31. metaprogramming_macro_dsl on `@autosize` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `macro`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:218:1`
- **Summary:** Compile-time AST transformation creating expressive domain-specific languages without runtime penalty.
- **Evidence Trail:**
  - `+95%` (JULIA_MACRO_METAPROGRAMMING): Macro '@autosize' transforms compile-time AST for domain-specific syntax extension

### 32. metaprogramming_macro_dsl on `@layer` (95% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `macro`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/macro.jl:57:1`
- **Summary:** Compile-time AST transformation creating expressive domain-specific languages without runtime penalty.
- **Evidence Trail:**
  - `+95%` (JULIA_MACRO_METAPROGRAMMING): Macro '@layer' transforms compile-time AST for domain-specific syntax extension

### 33. homoiconic_ast_transform on `_makelazy` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:230:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_makelazy' generates or manipulates homoiconic Julia AST expressions

### 34. homoiconic_ast_transform on `_makefun` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:248:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_makefun' generates or manipulates homoiconic Julia AST expressions

### 35. homoiconic_ast_transform on `_replaceunderscore` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:270:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_replaceunderscore' generates or manipulates homoiconic Julia AST expressions

### 36. homoiconic_ast_transform on `_layer_macro` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/macro.jl:61:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_layer_macro' generates or manipulates homoiconic Julia AST expressions

### 37. homoiconic_ast_transform on `_macro_adapt` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/macro.jl:105:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_macro_adapt' generates or manipulates homoiconic Julia AST expressions

### 38. homoiconic_ast_transform on `_macro_big_show` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:4:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_macro_big_show' generates or manipulates homoiconic Julia AST expressions

### 39. homoiconic_ast_transform on `_macro_named_show` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:23:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_macro_named_show' generates or manipulates homoiconic Julia AST expressions

### 40. homoiconic_ast_transform on `_macro_layer_show` (85% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:109:1`
- **Summary:** Code-as-data manipulation constructing or evaluating runtime Julia expressions.
- **Evidence Trail:**
  - `+85%` (JULIA_HOMOICONIC_AST): Function '_macro_layer_show' generates or manipulates homoiconic Julia AST expressions

### 41. conversion_promotion_protocol on `Base.promote_rule` (90% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:44:1`
- **Summary:** Idiomatic numeric and domain type coercion conforming to Julia's core type promotion engine.
- **Evidence Trail:**
  - `+90%` (JULIA_CONVERT_PROMOTE): Method 'Base.promote_rule' hooks into Julia core numeric and type promotion engine

### 42. conversion_promotion_protocol on `Base.convert` (90% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:19:1`
- **Summary:** Idiomatic numeric and domain type coercion conforming to Julia's core type promotion engine.
- **Evidence Trail:**
  - `+90%` (JULIA_CONVERT_PROMOTE): Method 'Base.convert' hooks into Julia core numeric and type promotion engine

### 43. conversion_promotion_protocol on `Base.convert` (90% [VERY_HIGH])
- **Category:** `julia_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:21:1`
- **Summary:** Idiomatic numeric and domain type coercion conforming to Julia's core type promotion engine.
- **Evidence Trail:**
  - `+90%` (JULIA_CONVERT_PROMOTE): Method 'Base.convert' hooks into Julia core numeric and type promotion engine

### 44. multiple_dispatch_polymorphism on `Base.promote_rule` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:44:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.promote_rule' performs multi-argument dynamic multiple dispatch over (x::Type{Nil}, y::Type{<:Number})

### 45. multiple_dispatch_polymorphism on `Random.rand` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:46:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Random.rand' performs multi-argument dynamic multiple dispatch over (rng::Random.AbstractRNG, ::Random.SamplerType{Nil})

### 46. multiple_dispatch_polymorphism on `nil_input` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:96:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'nil_input' performs multi-argument dynamic multiple dispatch over (pad::Bool, s::Tuple{Vararg{Integer}})

### 47. multiple_dispatch_polymorphism on `nil_input` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:97:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'nil_input' performs multi-argument dynamic multiple dispatch over (pad::Bool, multi::Tuple{Vararg{Integer}}...)

### 48. multiple_dispatch_polymorphism on `nil_input` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:98:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'nil_input' performs multi-argument dynamic multiple dispatch over (pad::Bool, tup::Tuple{Vararg{Tuple}})

### 49. multiple_dispatch_polymorphism on `outputsize` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:132:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'outputsize' performs multi-argument dynamic multiple dispatch over (m::Tuple, input::Tuple...; padbatch=false)

### 50. multiple_dispatch_polymorphism on `outputsize` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:133:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'outputsize' performs multi-argument dynamic multiple dispatch over (m::AbstractVector, input::Tuple...; padbatch=false)

### 51. multiple_dispatch_polymorphism on `autosizefor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:264:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'autosizefor' performs multi-argument dynamic multiple dispatch over (::Type, x::AbstractArray)

### 52. multiple_dispatch_polymorphism on `autosizefor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:265:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'autosizefor' performs multi-argument dynamic multiple dispatch over (::Type{<:Dense}, x::AbstractArray)

### 53. multiple_dispatch_polymorphism on `autosizefor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:266:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'autosizefor' performs multi-argument dynamic multiple dispatch over (::Type{<:Embedding}, x::AbstractArray)

### 54. multiple_dispatch_polymorphism on `autosizefor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:267:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'autosizefor' performs multi-argument dynamic multiple dispatch over (::Type{<:LayerNorm}, x::AbstractArray)

### 55. multiple_dispatch_polymorphism on `Base.convert` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:19:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.convert' performs multi-argument dynamic multiple dispatch over (::Type{Nil}, ::Number)

### 56. multiple_dispatch_polymorphism on `Base.convert` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:21:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.convert' performs multi-argument dynamic multiple dispatch over (::Type{Nil}, ::Nil)

### 57. multiple_dispatch_polymorphism on `glorot_uniform` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:81:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'glorot_uniform' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, dims::Integer...; gain::Real=1)

### 58. multiple_dispatch_polymorphism on `glorot_normal` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:124:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'glorot_normal' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, dims::Integer...; gain::Real=1)

### 59. multiple_dispatch_polymorphism on `kaiming_uniform` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:158:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'kaiming_uniform' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, dims::Integer...; gain::Real = √2)

### 60. multiple_dispatch_polymorphism on `kaiming_normal` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:195:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'kaiming_normal' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, dims::Integer...; gain::Real = √2f0)

### 61. multiple_dispatch_polymorphism on `truncated_normal` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:230:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'truncated_normal' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, dims::Integer...; mean = 0)

### 62. multiple_dispatch_polymorphism on `lecun_normal` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:283:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'lecun_normal' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, dims::Integer...; gain::Real=1)

### 63. multiple_dispatch_polymorphism on `orthogonal` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:332:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'orthogonal' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, rows::Integer, cols::Integer; gain::Real = 1)

### 64. multiple_dispatch_polymorphism on `orthogonal` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:342:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'orthogonal' performs multi-argument dynamic multiple dispatch over (rng::AbstractRNG, d1::Integer, ds::Integer...; kwargs...)

### 65. multiple_dispatch_polymorphism on `Embedding` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:10:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Embedding' performs multi-argument dynamic multiple dispatch over (in::Integer, out::Integer; kw...)

### 66. multiple_dispatch_polymorphism on `RNNCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:12:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'RNNCell' performs multi-argument dynamic multiple dispatch over (in::Integer, out::Integer)

### 67. multiple_dispatch_polymorphism on `LSTMCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:13:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'LSTMCell' performs multi-argument dynamic multiple dispatch over (in::Integer, out::Integer; kw...)

### 68. multiple_dispatch_polymorphism on `GRUCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:15:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'GRUCell' performs multi-argument dynamic multiple dispatch over (in::Integer, out::Integer; kw...)

### 69. multiple_dispatch_polymorphism on `GRUv3Cell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:16:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'GRUv3Cell' performs multi-argument dynamic multiple dispatch over (in::Integer, out::Integer; kw...)

### 70. multiple_dispatch_polymorphism on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:25:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadmodel!' performs multi-argument dynamic multiple dispatch over (dst::ConvTranspose, src::NamedTuple{(:σ)

### 71. multiple_dispatch_polymorphism on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:32:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadmodel!' performs multi-argument dynamic multiple dispatch over (dst::Conv, src::NamedTuple{(:σ)

### 72. multiple_dispatch_polymorphism on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:37:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadmodel!' performs multi-argument dynamic multiple dispatch over (dst::CrossCor, src::NamedTuple{(:σ)

### 73. multiple_dispatch_polymorphism on `get_device` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:47:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'get_device' performs multi-argument dynamic multiple dispatch over (backend::String, idx::Int = 0)

### 74. multiple_dispatch_polymorphism on `setup` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:157:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'setup' performs multi-argument dynamic multiple dispatch over (rule::Optimisers.AbstractRule, model::Duplicated)

### 75. multiple_dispatch_polymorphism on `trainstep!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:329:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'trainstep!' performs multi-argument dynamic multiple dispatch over (adtype::Union{Nothing, batch::Tuple)

### 76. multiple_dispatch_polymorphism on `_trainstep!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:335:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_trainstep!' performs multi-argument dynamic multiple dispatch over (adtype::AbstractADType, on_reactant::Bool, batch::Tuple)

### 77. multiple_dispatch_polymorphism on `trainstep_withgradient!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:360:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'trainstep_withgradient!' performs multi-argument dynamic multiple dispatch over (adtype::Union{Nothing, batch::Tuple)

### 78. multiple_dispatch_polymorphism on `_trainstep_withgradient!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:366:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_trainstep_withgradient!' performs multi-argument dynamic multiple dispatch over (adtype::AbstractADType, on_reactant::Bool, batch::Tuple)

### 79. multiple_dispatch_polymorphism on `maybe_gc!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:41:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'maybe_gc!' performs multi-argument dynamic multiple dispatch over (::NoGCPacer, i::Integer, t0::UInt64)

### 80. multiple_dispatch_polymorphism on `maybe_gc!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:47:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'maybe_gc!' performs multi-argument dynamic multiple dispatch over (p::FixedGCPacer, i::Integer, ::UInt64)

### 81. multiple_dispatch_polymorphism on `maybe_gc!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:79:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'maybe_gc!' performs multi-argument dynamic multiple dispatch over (p::AutoGCPacer, i::Integer, t0::UInt64)

### 82. multiple_dispatch_polymorphism on `ChainRulesCore.rrule` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:174:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'ChainRulesCore.rrule' performs multi-argument dynamic multiple dispatch over (::typeof(_to_bf16), x::AbstractArray)

### 83. multiple_dispatch_polymorphism on `Adapt.adapt_storage` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:180:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Adapt.adapt_storage' performs multi-argument dynamic multiple dispatch over (::FluxEltypeAdaptor{BFloat16}, x::AbstractArray{<:AbstractFloat})

### 84. multiple_dispatch_polymorphism on `Adapt.adapt_storage` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:181:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Adapt.adapt_storage' performs multi-argument dynamic multiple dispatch over (::FluxEltypeAdaptor{BFloat16}, x::AbstractArray{<:Complex{<:AbstractFloat}})

### 85. multiple_dispatch_polymorphism on `_paramtype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:182:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_paramtype' performs multi-argument dynamic multiple dispatch over (::Type{BFloat16}, x::AbstractArray{<:AbstractFloat})

### 86. multiple_dispatch_polymorphism on `_paramtype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:183:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_paramtype' performs multi-argument dynamic multiple dispatch over (::Type{BFloat16}, x::AbstractArray{<:Complex{<:AbstractFloat}})

### 87. multiple_dispatch_polymorphism on `gradient` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/gradient.jl:140:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'gradient' performs multi-argument dynamic multiple dispatch over (args::Union{EnzymeCore.Const, EnzymeCore.Duplicated}...; zero::Bool=true)

### 88. multiple_dispatch_polymorphism on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:7:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadleaf!' performs multi-argument dynamic multiple dispatch over (dst::AbstractArray, src::Bool)

### 89. multiple_dispatch_polymorphism on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:16:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadleaf!' performs multi-argument dynamic multiple dispatch over (dst::Bool, src::AbstractArray)

### 90. multiple_dispatch_polymorphism on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:19:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadleaf!' performs multi-argument dynamic multiple dispatch over (dst::AbstractArray, src::AbstractArray)

### 91. multiple_dispatch_polymorphism on `_tie_check` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:25:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_tie_check' performs multi-argument dynamic multiple dispatch over (dst::Bool, src::AbstractArray)

### 92. multiple_dispatch_polymorphism on `_tie_check` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:27:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_tie_check' performs multi-argument dynamic multiple dispatch over (dst::AbstractArray, src::Bool)

### 93. multiple_dispatch_polymorphism on `_tie_check` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:29:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_tie_check' performs multi-argument dynamic multiple dispatch over (dst::AbstractArray, src::AbstractArray)

### 94. multiple_dispatch_polymorphism on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:188:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'loadmodel!' performs multi-argument dynamic multiple dispatch over (dst::EnzymeCore.Duplicated, src::EnzymeCore.Duplicated; kw...)

### 95. multiple_dispatch_polymorphism on `label_smoothing` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/losses/functions.jl:161:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'label_smoothing' performs multi-argument dynamic multiple dispatch over (y::Union{AbstractArray, α::Number; dims::Int = 1)

### 96. multiple_dispatch_polymorphism on `_paddims` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:3:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_paddims' performs multi-argument dynamic multiple dispatch over (x::Tuple, y::Tuple)

### 97. multiple_dispatch_polymorphism on `apply_pad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:27:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'apply_pad' performs multi-argument dynamic multiple dispatch over (pad_mode::Symbol, x::AbstractArray)

### 98. multiple_dispatch_polymorphism on `calc_padding` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:55:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'calc_padding' performs multi-argument dynamic multiple dispatch over (::Val{:same}, k::NTuple{N)

### 99. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:228:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, l::Conv)

### 100. multiple_dispatch_polymorphism on `conv_transpose_dims` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:342:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'conv_transpose_dims' performs multi-argument dynamic multiple dispatch over (c::ConvTranspose, x::AbstractArray)

### 101. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:377:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, l::ConvTranspose)

### 102. multiple_dispatch_polymorphism on `calc_padding` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:385:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'calc_padding' performs multi-argument dynamic multiple dispatch over (::Type{ConvTranspose}, ::Val{:same}, k::NTuple{N)

### 103. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:522:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, l::CrossCor)

### 104. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:595:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, a::AdaptiveMaxPool)

### 105. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:637:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, a::AdaptiveMeanPool)

### 106. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:676:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, g::GlobalMaxPool)

### 107. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:710:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, g::GlobalMeanPool)

### 108. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:771:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::MaxPool)

### 109. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:831:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::MeanPool)

### 110. multiple_dispatch_polymorphism on `_pool_size_check` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:838:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_pool_size_check' performs multi-argument dynamic multiple dispatch over (tup::Tuple, x::AbstractArray)

### 111. multiple_dispatch_polymorphism on `Dropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:76:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Dropout' performs multi-argument dynamic multiple dispatch over (p::Real; dims=:, active::Union{Bool)

### 112. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:88:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, d::Dropout)

### 113. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:152:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, d::AlphaDropout)

### 114. multiple_dispatch_polymorphism on `LayerNorm` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:194:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'LayerNorm' performs multi-argument dynamic multiple dispatch over (size::Tuple{Vararg{Int}}, λ=identity; affine::Bool=true, eps::Real=1f-5)

### 115. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:212:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, l::LayerNorm)

### 116. multiple_dispatch_polymorphism on `RNNCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:193:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'RNNCell' performs multi-argument dynamic multiple dispatch over (x::AbstractVecOrMat, h::AbstractVecOrMat)

### 117. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:200:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::RNNCell)

### 118. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:315:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::RNN)

### 119. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:526:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::LSTM)

### 120. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:720:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::GRU)

### 121. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:906:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, m::GRUv3)

### 122. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:70:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, u::Upsample{mode})

### 123. multiple_dispatch_polymorphism on `_big_show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:39:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_big_show' performs multi-argument dynamic multiple dispatch over (io::IO, indent::Int=0)

### 124. multiple_dispatch_polymorphism on `_layer_show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:125:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_layer_show' performs multi-argument dynamic multiple dispatch over (io::IO, indent::Int=0)

### 125. multiple_dispatch_polymorphism on `_layer_string` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:144:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_layer_string' performs multi-argument dynamic multiple dispatch over (::IO, a::AbstractArray)

### 126. multiple_dispatch_polymorphism on `Base.show` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:135:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.show' performs multi-argument dynamic multiple dispatch over (io::IO, mha::MultiHeadAttention)

### 127. multiple_dispatch_polymorphism on `_match_eltype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:16:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_match_eltype' performs multi-argument dynamic multiple dispatch over (::Type{Float32}, x::AbstractArray{Float64})

### 128. multiple_dispatch_polymorphism on `_match_eltype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:24:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_match_eltype' performs multi-argument dynamic multiple dispatch over (::Type{Float16}, x::AbstractArray{Float32})

### 129. multiple_dispatch_polymorphism on `_match_eltype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:31:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_match_eltype' performs multi-argument dynamic multiple dispatch over (::Type, x::OneHotLike)

### 130. multiple_dispatch_polymorphism on `_match_eltype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:34:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_match_eltype' performs multi-argument dynamic multiple dispatch over (::Type{T}, x::AbstractArray{<:Union{AbstractFloat)

### 131. multiple_dispatch_polymorphism on `_match_eltype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:40:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_match_eltype' performs multi-argument dynamic multiple dispatch over (::Type{BFloat16}, x::AbstractArray{<:Union{AbstractFloat)

### 132. multiple_dispatch_polymorphism on `_match_eltype` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:43:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function '_match_eltype' performs multi-argument dynamic multiple dispatch over (::Type, x::AbstractArray)

### 133. multiple_dispatch_polymorphism on `ChainRulesCore.rrule` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:50:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'ChainRulesCore.rrule' performs multi-argument dynamic multiple dispatch over (::typeof(_match_eltype), ::Type{T}, x::AbstractArray)

### 134. multiple_dispatch_polymorphism on `ChainRulesCore.rrule` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:53:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'ChainRulesCore.rrule' performs multi-argument dynamic multiple dispatch over (::typeof(_match_eltype), x::AbstractArray)

### 135. multiple_dispatch_polymorphism on `update!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:105:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'update!' performs multi-argument dynamic multiple dispatch over (opt::AbstractOptimiser, model::Chain, grads::Tuple)

### 136. multiple_dispatch_polymorphism on `update!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:111:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'update!' performs multi-argument dynamic multiple dispatch over (opt::AbstractOptimiser, ::Params, grads::Union{Tuple)

### 137. multiple_dispatch_polymorphism on `train!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:46:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'train!' performs multi-argument dynamic multiple dispatch over (ps::Params, opt::Optimisers.AbstractRule; cb=nothing)

### 138. multiple_dispatch_polymorphism on `update!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/train.jl:1:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'update!' performs multi-argument dynamic multiple dispatch over (opt::AbstractOptimiser, x::AbstractArray)

### 139. multiple_dispatch_polymorphism on `update!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/train.jl:7:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'update!' performs multi-argument dynamic multiple dispatch over (opt::AbstractOptimiser, xs::Params)

### 140. multiple_dispatch_polymorphism on `train!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/train.jl:27:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'train!' performs multi-argument dynamic multiple dispatch over (ps::Params, opt::AbstractOptimiser; cb = () -> ())

### 141. multiple_dispatch_polymorphism on `RMSProp` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:134:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'RMSProp' performs multi-argument dynamic multiple dispatch over (η::Real = 0.001, ρ::Real = 0.9, ϵ::Real = EPS)

### 142. multiple_dispatch_polymorphism on `RMSProp` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:135:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'RMSProp' performs multi-argument dynamic multiple dispatch over (η::Real, ρ::Real, acc::IdDict)

### 143. multiple_dispatch_polymorphism on `Adam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:169:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Adam' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 144. multiple_dispatch_polymorphism on `RAdam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:211:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'RAdam' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 145. multiple_dispatch_polymorphism on `AdaMax` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:261:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AdaMax' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 146. multiple_dispatch_polymorphism on `OAdam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:304:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'OAdam' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 147. multiple_dispatch_polymorphism on `AdaGrad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:346:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AdaGrad' performs multi-argument dynamic multiple dispatch over (η::Real = 0.1, ϵ::Real = EPS)

### 148. multiple_dispatch_polymorphism on `AdaGrad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:347:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AdaGrad' performs multi-argument dynamic multiple dispatch over (η::Real, state::IdDict)

### 149. multiple_dispatch_polymorphism on `AdaDelta` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:378:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AdaDelta' performs multi-argument dynamic multiple dispatch over (ρ::Real = 0.9, ϵ::Real = EPS)

### 150. multiple_dispatch_polymorphism on `AdaDelta` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:379:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AdaDelta' performs multi-argument dynamic multiple dispatch over (ρ::Real, state::IdDict)

### 151. multiple_dispatch_polymorphism on `AMSGrad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:418:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AMSGrad' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 152. multiple_dispatch_polymorphism on `NAdam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:459:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'NAdam' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 153. multiple_dispatch_polymorphism on `AdaBelief` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:526:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'AdaBelief' performs multi-argument dynamic multiple dispatch over (η::Real, β::Tuple, state::IdDict)

### 154. multiple_dispatch_polymorphism on `Base.getindex` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:575:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Base.getindex' performs multi-argument dynamic multiple dispatch over (c::Optimiser, i::AbstractArray)

### 155. multiple_dispatch_polymorphism on `bcast!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:102:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'bcast!' performs multi-argument dynamic multiple dispatch over (backend::AbstractFluxDistributedBackend, sendrecvbuf; root::Int=0)

### 156. multiple_dispatch_polymorphism on `bcast!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:106:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'bcast!' performs multi-argument dynamic multiple dispatch over (backend::AbstractFluxDistributedBackend, recvbuf; root::Int=0)

### 157. multiple_dispatch_polymorphism on `allreduce!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:134:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'allreduce!' performs multi-argument dynamic multiple dispatch over (backend::AbstractFluxDistributedBackend, op::F)

### 158. multiple_dispatch_polymorphism on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:203:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'synchronize!!' performs multi-argument dynamic multiple dispatch over (backend::AbstractFluxDistributedBackend, model::FluxDistributedModel; root::Int=0)

### 159. multiple_dispatch_polymorphism on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:207:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'synchronize!!' performs multi-argument dynamic multiple dispatch over (backend::AbstractFluxDistributedBackend, ps::Tuple; root::Int=0)

### 160. multiple_dispatch_polymorphism on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:228:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'synchronize!!' performs multi-argument dynamic multiple dispatch over (backend::AbstractFluxDistributedBackend, ps::T; root::Int=0)

### 161. multiple_dispatch_polymorphism on `Optimisers.init` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:296:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Optimisers.init' performs multi-argument dynamic multiple dispatch over (opt::DistributedOptimizer, x::AbstractArray)

### 162. multiple_dispatch_polymorphism on `Optimisers._adjust` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:298:1`
- **Summary:** Multi-argument dynamic dispatch resolving specialized method bodies based on all operand types.
- **Evidence Trail:**
  - `+90%` (JULIA_MULTIPLE_DISPATCH): Function 'Optimisers._adjust' performs multi-argument dynamic multiple dispatch over (opt::DistributedOptimizer, nt::NamedTuple)

### 163. outer_constructor_dispatch on `RNNCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:12:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNNCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 164. outer_constructor_dispatch on `LSTMCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:13:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTMCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 165. outer_constructor_dispatch on `GRUCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:15:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 166. outer_constructor_dispatch on `GRUv3Cell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:16:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3Cell' acts as polymorphic Outer Constructor specializing struct instantiation

### 167. outer_constructor_dispatch on `AutoGCPacer` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:75:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AutoGCPacer' acts as polymorphic Outer Constructor specializing struct instantiation

### 168. outer_constructor_dispatch on `Conv` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:161:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Conv' acts as polymorphic Outer Constructor specializing struct instantiation

### 169. outer_constructor_dispatch on `Conv` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:172:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Conv' acts as polymorphic Outer Constructor specializing struct instantiation

### 170. outer_constructor_dispatch on `Conv` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:210:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Conv' acts as polymorphic Outer Constructor specializing struct instantiation

### 171. outer_constructor_dispatch on `ConvTranspose` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:320:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'ConvTranspose' acts as polymorphic Outer Constructor specializing struct instantiation

### 172. outer_constructor_dispatch on `ConvTranspose` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:330:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'ConvTranspose' acts as polymorphic Outer Constructor specializing struct instantiation

### 173. outer_constructor_dispatch on `ConvTranspose` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:370:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'ConvTranspose' acts as polymorphic Outer Constructor specializing struct instantiation

### 174. outer_constructor_dispatch on `CrossCor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:480:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'CrossCor' acts as polymorphic Outer Constructor specializing struct instantiation

### 175. outer_constructor_dispatch on `CrossCor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:489:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'CrossCor' acts as polymorphic Outer Constructor specializing struct instantiation

### 176. outer_constructor_dispatch on `CrossCor` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:510:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'CrossCor' acts as polymorphic Outer Constructor specializing struct instantiation

### 177. outer_constructor_dispatch on `GlobalMaxPool` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:665:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GlobalMaxPool' acts as polymorphic Outer Constructor specializing struct instantiation

### 178. outer_constructor_dispatch on `GlobalMeanPool` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:699:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GlobalMeanPool' acts as polymorphic Outer Constructor specializing struct instantiation

### 179. outer_constructor_dispatch on `MaxPool` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:759:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MaxPool' acts as polymorphic Outer Constructor specializing struct instantiation

### 180. outer_constructor_dispatch on `MaxPool` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:765:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MaxPool' acts as polymorphic Outer Constructor specializing struct instantiation

### 181. outer_constructor_dispatch on `MeanPool` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:819:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MeanPool' acts as polymorphic Outer Constructor specializing struct instantiation

### 182. outer_constructor_dispatch on `MeanPool` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:825:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MeanPool' acts as polymorphic Outer Constructor specializing struct instantiation

### 183. outer_constructor_dispatch on `Chain` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:53:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Chain' acts as polymorphic Outer Constructor specializing struct instantiation

### 184. outer_constructor_dispatch on `Chain` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:54:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Chain' acts as polymorphic Outer Constructor specializing struct instantiation

### 185. outer_constructor_dispatch on `Chain` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:65:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Chain' acts as polymorphic Outer Constructor specializing struct instantiation

### 186. outer_constructor_dispatch on `Chain` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:66:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Chain' acts as polymorphic Outer Constructor specializing struct instantiation

### 187. outer_constructor_dispatch on `Dropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:74:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Dropout' acts as polymorphic Outer Constructor specializing struct instantiation

### 188. outer_constructor_dispatch on `Dropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:76:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Dropout' acts as polymorphic Outer Constructor specializing struct instantiation

### 189. outer_constructor_dispatch on `Dropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:83:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Dropout' acts as polymorphic Outer Constructor specializing struct instantiation

### 190. outer_constructor_dispatch on `AlphaDropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:127:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AlphaDropout' acts as polymorphic Outer Constructor specializing struct instantiation

### 191. outer_constructor_dispatch on `AlphaDropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:128:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AlphaDropout' acts as polymorphic Outer Constructor specializing struct instantiation

### 192. outer_constructor_dispatch on `AlphaDropout` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:135:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AlphaDropout' acts as polymorphic Outer Constructor specializing struct instantiation

### 193. outer_constructor_dispatch on `LayerNorm` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:194:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LayerNorm' acts as polymorphic Outer Constructor specializing struct instantiation

### 194. outer_constructor_dispatch on `LayerNorm` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:198:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LayerNorm' acts as polymorphic Outer Constructor specializing struct instantiation

### 195. outer_constructor_dispatch on `LayerNorm` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:199:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LayerNorm' acts as polymorphic Outer Constructor specializing struct instantiation

### 196. outer_constructor_dispatch on `LayerNorm` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:203:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LayerNorm' acts as polymorphic Outer Constructor specializing struct instantiation

### 197. outer_constructor_dispatch on `BatchNorm` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:273:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'BatchNorm' acts as polymorphic Outer Constructor specializing struct instantiation

### 198. outer_constructor_dispatch on `Recurrence` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:69:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Recurrence' acts as polymorphic Outer Constructor specializing struct instantiation

### 199. outer_constructor_dispatch on `Recurrence` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:73:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Recurrence' acts as polymorphic Outer Constructor specializing struct instantiation

### 200. outer_constructor_dispatch on `RNNCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:178:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNNCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 201. outer_constructor_dispatch on `RNNCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:191:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNNCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 202. outer_constructor_dispatch on `RNNCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:193:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNNCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 203. outer_constructor_dispatch on `Model` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:271:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Model' acts as polymorphic Outer Constructor specializing struct instantiation

### 204. outer_constructor_dispatch on `RNN` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:284:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNN' acts as polymorphic Outer Constructor specializing struct instantiation

### 205. outer_constructor_dispatch on `RNN` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:289:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNN' acts as polymorphic Outer Constructor specializing struct instantiation

### 206. outer_constructor_dispatch on `RNN` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:293:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RNN' acts as polymorphic Outer Constructor specializing struct instantiation

### 207. outer_constructor_dispatch on `LSTMCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:395:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTMCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 208. outer_constructor_dispatch on `LSTMCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:409:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTMCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 209. outer_constructor_dispatch on `LSTMCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:411:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTMCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 210. outer_constructor_dispatch on `Model` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:482:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Model' acts as polymorphic Outer Constructor specializing struct instantiation

### 211. outer_constructor_dispatch on `LSTM` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:499:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTM' acts as polymorphic Outer Constructor specializing struct instantiation

### 212. outer_constructor_dispatch on `LSTM` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:504:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTM' acts as polymorphic Outer Constructor specializing struct instantiation

### 213. outer_constructor_dispatch on `LSTM` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:508:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'LSTM' acts as polymorphic Outer Constructor specializing struct instantiation

### 214. outer_constructor_dispatch on `GRUCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:596:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 215. outer_constructor_dispatch on `GRUCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:609:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 216. outer_constructor_dispatch on `GRUCell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:614:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUCell' acts as polymorphic Outer Constructor specializing struct instantiation

### 217. outer_constructor_dispatch on `GRU` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:693:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRU' acts as polymorphic Outer Constructor specializing struct instantiation

### 218. outer_constructor_dispatch on `GRU` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:698:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRU' acts as polymorphic Outer Constructor specializing struct instantiation

### 219. outer_constructor_dispatch on `GRU` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:702:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRU' acts as polymorphic Outer Constructor specializing struct instantiation

### 220. outer_constructor_dispatch on `GRUv3Cell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:777:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3Cell' acts as polymorphic Outer Constructor specializing struct instantiation

### 221. outer_constructor_dispatch on `GRUv3Cell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:790:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3Cell' acts as polymorphic Outer Constructor specializing struct instantiation

### 222. outer_constructor_dispatch on `GRUv3Cell` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:795:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3Cell' acts as polymorphic Outer Constructor specializing struct instantiation

### 223. outer_constructor_dispatch on `GRUv3` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:879:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3' acts as polymorphic Outer Constructor specializing struct instantiation

### 224. outer_constructor_dispatch on `GRUv3` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:884:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3' acts as polymorphic Outer Constructor specializing struct instantiation

### 225. outer_constructor_dispatch on `GRUv3` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:888:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'GRUv3' acts as polymorphic Outer Constructor specializing struct instantiation

### 226. outer_constructor_dispatch on `Upsample` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:41:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Upsample' acts as polymorphic Outer Constructor specializing struct instantiation

### 227. outer_constructor_dispatch on `Upsample` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:50:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Upsample' acts as polymorphic Outer Constructor specializing struct instantiation

### 228. outer_constructor_dispatch on `PixelShuffle` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:147:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'PixelShuffle' acts as polymorphic Outer Constructor specializing struct instantiation

### 229. outer_constructor_dispatch on `MultiHeadAttention` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:79:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MultiHeadAttention' acts as polymorphic Outer Constructor specializing struct instantiation

### 230. outer_constructor_dispatch on `MultiHeadAttention` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:115:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MultiHeadAttention' acts as polymorphic Outer Constructor specializing struct instantiation

### 231. outer_constructor_dispatch on `MultiHeadAttention` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:118:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MultiHeadAttention' acts as polymorphic Outer Constructor specializing struct instantiation

### 232. outer_constructor_dispatch on `MultiHeadAttention` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:120:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MultiHeadAttention' acts as polymorphic Outer Constructor specializing struct instantiation

### 233. outer_constructor_dispatch on `MultiHeadAttention` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:166:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MultiHeadAttention' acts as polymorphic Outer Constructor specializing struct instantiation

### 234. outer_constructor_dispatch on `MultiHeadAttention` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:167:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MultiHeadAttention' acts as polymorphic Outer Constructor specializing struct instantiation

### 235. outer_constructor_dispatch on `Descent` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:34:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Descent' acts as polymorphic Outer Constructor specializing struct instantiation

### 236. outer_constructor_dispatch on `Momentum` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:64:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Momentum' acts as polymorphic Outer Constructor specializing struct instantiation

### 237. outer_constructor_dispatch on `Nesterov` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:97:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Nesterov' acts as polymorphic Outer Constructor specializing struct instantiation

### 238. outer_constructor_dispatch on `RMSProp` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:134:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RMSProp' acts as polymorphic Outer Constructor specializing struct instantiation

### 239. outer_constructor_dispatch on `RMSProp` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:135:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RMSProp' acts as polymorphic Outer Constructor specializing struct instantiation

### 240. outer_constructor_dispatch on `Adam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:169:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Adam' acts as polymorphic Outer Constructor specializing struct instantiation

### 241. outer_constructor_dispatch on `RAdam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:211:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'RAdam' acts as polymorphic Outer Constructor specializing struct instantiation

### 242. outer_constructor_dispatch on `AdaMax` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:261:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AdaMax' acts as polymorphic Outer Constructor specializing struct instantiation

### 243. outer_constructor_dispatch on `OAdam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:304:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'OAdam' acts as polymorphic Outer Constructor specializing struct instantiation

### 244. outer_constructor_dispatch on `AdaGrad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:346:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AdaGrad' acts as polymorphic Outer Constructor specializing struct instantiation

### 245. outer_constructor_dispatch on `AdaGrad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:347:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AdaGrad' acts as polymorphic Outer Constructor specializing struct instantiation

### 246. outer_constructor_dispatch on `AdaDelta` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:378:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AdaDelta' acts as polymorphic Outer Constructor specializing struct instantiation

### 247. outer_constructor_dispatch on `AdaDelta` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:379:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AdaDelta' acts as polymorphic Outer Constructor specializing struct instantiation

### 248. outer_constructor_dispatch on `AMSGrad` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:418:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AMSGrad' acts as polymorphic Outer Constructor specializing struct instantiation

### 249. outer_constructor_dispatch on `NAdam` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:459:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'NAdam' acts as polymorphic Outer Constructor specializing struct instantiation

### 250. outer_constructor_dispatch on `AdaBelief` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:526:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'AdaBelief' acts as polymorphic Outer Constructor specializing struct instantiation

### 251. outer_constructor_dispatch on `Optimiser` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:570:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'Optimiser' acts as polymorphic Outer Constructor specializing struct instantiation

### 252. outer_constructor_dispatch on `InvDecay` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:610:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'InvDecay' acts as polymorphic Outer Constructor specializing struct instantiation

### 253. outer_constructor_dispatch on `WeightDecay` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:689:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'WeightDecay' acts as polymorphic Outer Constructor specializing struct instantiation

### 254. outer_constructor_dispatch on `SignDecay` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:712:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'SignDecay' acts as polymorphic Outer Constructor specializing struct instantiation

### 255. outer_constructor_dispatch on `DistributedDataContainer` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:250:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'DistributedDataContainer' acts as polymorphic Outer Constructor specializing struct instantiation

### 256. outer_constructor_dispatch on `MPIBackend` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/backend.jl:16:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'MPIBackend' acts as polymorphic Outer Constructor specializing struct instantiation

### 257. outer_constructor_dispatch on `NCCLBackend` (90% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `outer_constructor`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/backend.jl:34:1`
- **Summary:** Polymorphic constructors defined outside struct definition specializing instantiation protocols.
- **Evidence Trail:**
  - `+90%` (JULIA_OUTER_CONSTRUCTOR): Function 'NCCLBackend' acts as polymorphic Outer Constructor specializing struct instantiation

### 258. method_specialization_table on `outputsize` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:91:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'outputsize' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 259. method_specialization_table on `nil_input` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:96:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'nil_input' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 260. method_specialization_table on `NNlib.` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:148:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'NNlib.' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 261. method_specialization_table on `autosizefor` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:264:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'autosizefor' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 262. method_specialization_table on `get_device` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/devices.jl:1:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'get_device' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 263. method_specialization_table on `nfan` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:27:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'nfan' defines 5 specialized dispatch methods forming an open polymorphic protocol

### 264. method_specialization_table on `kaiming_normal` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:195:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'kaiming_normal' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 265. method_specialization_table on `orthogonal` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/utils.jl:332:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'orthogonal' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 266. method_specialization_table on `RNNCell` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:12:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'RNNCell' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 267. method_specialization_table on `LSTMCell` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:13:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'LSTMCell' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 268. method_specialization_table on `GRUCell` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:15:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'GRUCell' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 269. method_specialization_table on `GRUv3Cell` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:16:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'GRUv3Cell' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 270. method_specialization_table on `loadmodel!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:25:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'loadmodel!' defines 6 specialized dispatch methods forming an open polymorphic protocol

### 271. method_specialization_table on `setup` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:142:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'setup' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 272. method_specialization_table on `train!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:198:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'train!' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 273. method_specialization_table on `_first_param` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:391:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_first_param' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 274. method_specialization_table on `maybe_gc!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:41:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'maybe_gc!' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 275. method_specialization_table on `trainmode!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:52:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'trainmode!' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 276. method_specialization_table on `_ishalfprec` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:129:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_ishalfprec' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 277. method_specialization_table on `_paramtype` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:137:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_paramtype' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 278. method_specialization_table on `_to_bf16` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:167:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_to_bf16' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 279. method_specialization_table on `ChainRulesCore.rrule` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:174:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'ChainRulesCore.rrule' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 280. method_specialization_table on `loadleaf!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:1:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'loadleaf!' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 281. method_specialization_table on `_tie_check` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:25:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_tie_check' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 282. method_specialization_table on `Conv` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:161:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'Conv' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 283. method_specialization_table on `_channels_in` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:225:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_channels_in' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 284. method_specialization_table on `Base.show` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:228:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'Base.show' defines 19 specialized dispatch methods forming an open polymorphic protocol

### 285. method_specialization_table on `ConvTranspose` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:320:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'ConvTranspose' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 286. method_specialization_table on `CrossCor` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:480:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'CrossCor' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 287. method_specialization_table on `Chain` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:53:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'Chain' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 288. method_specialization_table on `_tidy_active` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:5:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_tidy_active' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 289. method_specialization_table on `Dropout` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:74:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'Dropout' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 290. method_specialization_table on `AlphaDropout` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:127:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'AlphaDropout' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 291. method_specialization_table on `LayerNorm` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:194:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'LayerNorm' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 292. method_specialization_table on `initialstates` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:67:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'initialstates' defines 9 specialized dispatch methods forming an open polymorphic protocol

### 293. method_specialization_table on `RNN` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:284:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'RNN' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 294. method_specialization_table on `Functors.functor` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:309:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'Functors.functor' defines 4 specialized dispatch methods forming an open polymorphic protocol

### 295. method_specialization_table on `LSTM` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:499:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'LSTM' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 296. method_specialization_table on `GRU` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:693:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'GRU' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 297. method_specialization_table on `GRUv3` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:879:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'GRUv3' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 298. method_specialization_table on `_show_pre_post` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:86:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_show_pre_post' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 299. method_specialization_table on `_show_leaflike` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:90:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_show_leaflike' defines 5 specialized dispatch methods forming an open polymorphic protocol

### 300. method_specialization_table on `_any` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:191:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_any' defines 3 specialized dispatch methods forming an open polymorphic protocol

### 301. method_specialization_table on `MultiHeadAttention` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:79:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'MultiHeadAttention' defines 6 specialized dispatch methods forming an open polymorphic protocol

### 302. method_specialization_table on `_match_eltype` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/stateless.jl:16:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_match_eltype' defines 7 specialized dispatch methods forming an open polymorphic protocol

### 303. method_specialization_table on `_old_to_new` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:77:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function '_old_to_new' defines 7 specialized dispatch methods forming an open polymorphic protocol

### 304. method_specialization_table on `update!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:95:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'update!' defines 5 specialized dispatch methods forming an open polymorphic protocol

### 305. method_specialization_table on `apply!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:36:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'apply!' defines 20 specialized dispatch methods forming an open polymorphic protocol

### 306. method_specialization_table on `synchronize!!` (92% [VERY_HIGH])
- **Category:** `multiple_dispatch`
- **Target Kind:** `generic_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:203:1`
- **Summary:** Extending generic functions across multiple concrete types forming open polymorphic protocols.
- **Evidence Trail:**
  - `+92%` (JULIA_METHOD_SPECIALIZATION_TABLE): Generic function 'synchronize!!' defines 5 specialized dispatch methods forming an open polymorphic protocol

### 307. in_place_mutating_convention on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:25:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadmodel!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 308. in_place_mutating_convention on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:32:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadmodel!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 309. in_place_mutating_convention on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:37:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadmodel!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 310. in_place_mutating_convention on `reset!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:77:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'reset!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 311. in_place_mutating_convention on `params!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:82:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'params!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 312. in_place_mutating_convention on `train!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:198:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'train!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 313. in_place_mutating_convention on `trainstep!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:329:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'trainstep!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 314. in_place_mutating_convention on `_trainstep!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:335:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_trainstep!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 315. in_place_mutating_convention on `trainstep_withgradient!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:360:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'trainstep_withgradient!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 316. in_place_mutating_convention on `_trainstep_withgradient!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:366:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_trainstep_withgradient!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 317. in_place_mutating_convention on `_eager_step!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:375:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_eager_step!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 318. in_place_mutating_convention on `_update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:425:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 319. in_place_mutating_convention on `_update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:427:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 320. in_place_mutating_convention on `_reactant_trainstep!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:20:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_reactant_trainstep!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 321. in_place_mutating_convention on `_reactant_trainstep_withgradient!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:21:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '_reactant_trainstep_withgradient!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 322. in_place_mutating_convention on `maybe_gc!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:41:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'maybe_gc!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 323. in_place_mutating_convention on `maybe_gc!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:47:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'maybe_gc!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 324. in_place_mutating_convention on `maybe_gc!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:79:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'maybe_gc!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 325. in_place_mutating_convention on `testmode!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:30:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'testmode!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 326. in_place_mutating_convention on `testmode!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:33:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'testmode!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 327. in_place_mutating_convention on `trainmode!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:52:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'trainmode!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 328. in_place_mutating_convention on `trainmode!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:53:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'trainmode!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 329. in_place_mutating_convention on `trainmode!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:54:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'trainmode!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 330. in_place_mutating_convention on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:1:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadleaf!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 331. in_place_mutating_convention on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:7:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadleaf!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 332. in_place_mutating_convention on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:16:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadleaf!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 333. in_place_mutating_convention on `loadleaf!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:19:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadleaf!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 334. in_place_mutating_convention on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:90:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadmodel!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 335. in_place_mutating_convention on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:188:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadmodel!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 336. in_place_mutating_convention on `loadmodel!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/loading.jl:189:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'loadmodel!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 337. in_place_mutating_convention on `update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:95:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 338. in_place_mutating_convention on `update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:105:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 339. in_place_mutating_convention on `update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:111:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 340. in_place_mutating_convention on `train!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:40:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'train!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 341. in_place_mutating_convention on `train!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/Optimise.jl:46:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'train!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 342. in_place_mutating_convention on `update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/train.jl:1:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 343. in_place_mutating_convention on `update!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/train.jl:7:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'update!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 344. in_place_mutating_convention on `train!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/train.jl:27:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'train!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 345. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:36:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 346. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:66:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 347. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:99:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 348. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:137:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 349. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:171:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 350. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:213:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 351. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:263:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 352. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:306:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 353. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:349:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 354. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:381:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 355. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:420:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 356. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:461:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 357. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:528:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 358. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:577:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 359. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:612:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 360. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:661:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 361. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:691:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 362. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:714:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 363. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:731:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 364. in_place_mutating_convention on `apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:742:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 365. in_place_mutating_convention on `bcast!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:102:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'bcast!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 366. in_place_mutating_convention on `bcast!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:106:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'bcast!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 367. in_place_mutating_convention on `__bcast!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:118:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '__bcast!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 368. in_place_mutating_convention on `allreduce!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:134:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'allreduce!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 369. in_place_mutating_convention on `allreduce!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:138:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'allreduce!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 370. in_place_mutating_convention on `__allreduce!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:152:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '__allreduce!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 371. in_place_mutating_convention on `reduce!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:166:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'reduce!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 372. in_place_mutating_convention on `reduce!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:171:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'reduce!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 373. in_place_mutating_convention on `__reduce!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:185:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function '__reduce!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 374. in_place_mutating_convention on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:203:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'synchronize!!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 375. in_place_mutating_convention on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:207:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'synchronize!!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 376. in_place_mutating_convention on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:212:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'synchronize!!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 377. in_place_mutating_convention on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:218:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'synchronize!!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 378. in_place_mutating_convention on `synchronize!!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:228:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'synchronize!!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 379. in_place_mutating_convention on `Optimisers.apply!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:291:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'Optimisers.apply!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 380. in_place_mutating_convention on `DistributedUtils.synchronize!!` (90% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `mutating_function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:302:1`
- **Summary:** Idiomatic Julia mutation updating the first argument in-place to avoid temporary heap allocations.
- **Evidence Trail:**
  - `+90%` (SCIENTIFIC_IN_PLACE_MUTATION): Function 'DistributedUtils.synchronize!!' follows Julia mutating convention modifying arguments in-place to avoid allocations

### 381. callable_struct_functor on `Conv` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:210:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Conv' encapsulates state and behaves as an invocable function

### 382. callable_struct_functor on `ConvTranspose` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:370:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'ConvTranspose' encapsulates state and behaves as an invocable function

### 383. callable_struct_functor on `CrossCor` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:510:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'CrossCor' encapsulates state and behaves as an invocable function

### 384. callable_struct_functor on `AdaptiveMaxPool{S}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:584:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'AdaptiveMaxPool{S}' encapsulates state and behaves as an invocable function

### 385. callable_struct_functor on `AdaptiveMeanPool{S}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:626:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'AdaptiveMeanPool{S}' encapsulates state and behaves as an invocable function

### 386. callable_struct_functor on `GlobalMaxPool` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:665:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GlobalMaxPool' encapsulates state and behaves as an invocable function

### 387. callable_struct_functor on `GlobalMeanPool` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:699:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GlobalMeanPool' encapsulates state and behaves as an invocable function

### 388. callable_struct_functor on `MaxPool` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:765:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'MaxPool' encapsulates state and behaves as an invocable function

### 389. callable_struct_functor on `MeanPool` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:825:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'MeanPool' encapsulates state and behaves as an invocable function

### 390. callable_struct_functor on `Chain` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:65:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Chain' encapsulates state and behaves as an invocable function

### 391. callable_struct_functor on `Chain` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/basic.jl:66:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Chain' encapsulates state and behaves as an invocable function

### 392. callable_struct_functor on `Dropout` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:83:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Dropout' encapsulates state and behaves as an invocable function

### 393. callable_struct_functor on `AlphaDropout` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:135:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'AlphaDropout' encapsulates state and behaves as an invocable function

### 394. callable_struct_functor on `LayerNorm` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/normalise.jl:203:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'LayerNorm' encapsulates state and behaves as an invocable function

### 395. callable_struct_functor on `Recurrence` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:73:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Recurrence' encapsulates state and behaves as an invocable function

### 396. callable_struct_functor on `Recurrence{false}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:75:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Recurrence{false}' encapsulates state and behaves as an invocable function

### 397. callable_struct_functor on `Recurrence{true}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:79:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Recurrence{true}' encapsulates state and behaves as an invocable function

### 398. callable_struct_functor on `RNNCell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:191:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'RNNCell' encapsulates state and behaves as an invocable function

### 399. callable_struct_functor on `RNNCell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:193:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'RNNCell' encapsulates state and behaves as an invocable function

### 400. callable_struct_functor on `Model` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:271:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Model' encapsulates state and behaves as an invocable function

### 401. callable_struct_functor on `RNN` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:293:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'RNN' encapsulates state and behaves as an invocable function

### 402. callable_struct_functor on `RNN{false}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:295:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'RNN{false}' encapsulates state and behaves as an invocable function

### 403. callable_struct_functor on `RNN{true}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:302:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'RNN{true}' encapsulates state and behaves as an invocable function

### 404. callable_struct_functor on `LSTMCell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:409:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'LSTMCell' encapsulates state and behaves as an invocable function

### 405. callable_struct_functor on `LSTMCell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:411:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'LSTMCell' encapsulates state and behaves as an invocable function

### 406. callable_struct_functor on `Model` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:482:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Model' encapsulates state and behaves as an invocable function

### 407. callable_struct_functor on `LSTM` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:508:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'LSTM' encapsulates state and behaves as an invocable function

### 408. callable_struct_functor on `LSTM{false}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:510:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'LSTM{false}' encapsulates state and behaves as an invocable function

### 409. callable_struct_functor on `LSTM{true}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:515:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'LSTM{true}' encapsulates state and behaves as an invocable function

### 410. callable_struct_functor on `GRUCell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:609:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUCell' encapsulates state and behaves as an invocable function

### 411. callable_struct_functor on `GRUCell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:614:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUCell' encapsulates state and behaves as an invocable function

### 412. callable_struct_functor on `GRU` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:702:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRU' encapsulates state and behaves as an invocable function

### 413. callable_struct_functor on `GRU{false}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:704:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRU{false}' encapsulates state and behaves as an invocable function

### 414. callable_struct_functor on `GRU{true}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:709:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRU{true}' encapsulates state and behaves as an invocable function

### 415. callable_struct_functor on `GRUv3Cell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:790:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUv3Cell' encapsulates state and behaves as an invocable function

### 416. callable_struct_functor on `GRUv3Cell` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:795:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUv3Cell' encapsulates state and behaves as an invocable function

### 417. callable_struct_functor on `GRUv3` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:888:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUv3' encapsulates state and behaves as an invocable function

### 418. callable_struct_functor on `GRUv3{false}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:890:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUv3{false}' encapsulates state and behaves as an invocable function

### 419. callable_struct_functor on `GRUv3{true}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:895:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'GRUv3{true}' encapsulates state and behaves as an invocable function

### 420. callable_struct_functor on `Upsample{:nearest, Int}` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:54:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'Upsample{:nearest, Int}' encapsulates state and behaves as an invocable function

### 421. callable_struct_functor on `PixelShuffle` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/upsample.jl:147:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'PixelShuffle' encapsulates state and behaves as an invocable function

### 422. callable_struct_functor on `MultiHeadAttention` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:115:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'MultiHeadAttention' encapsulates state and behaves as an invocable function

### 423. callable_struct_functor on `MultiHeadAttention` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:118:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'MultiHeadAttention' encapsulates state and behaves as an invocable function

### 424. callable_struct_functor on `MultiHeadAttention` (95% [VERY_HIGH])
- **Category:** `scientific_performance`
- **Target Kind:** `callable_struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/attention.jl:120:1`
- **Summary:** Struct instance acting as an invokable function encapsulating parameters or precomputed state.
- **Evidence Trail:**
  - `+95%` (SCIENTIFIC_CALLABLE_STRUCT_FUNCTOR): Callable struct functor 'MultiHeadAttention' encapsulates state and behaves as an invocable function

### 425. singleton_immutable_instance on `Nil` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:12:1`
- **Summary:** Singleton instance represented as zero-field immutable struct or constant reference.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Zero-field immutable struct 'Nil' serves as a unique type-level Singleton instance

### 426. singleton_immutable_instance on `NoGCPacer` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:40:1`
- **Summary:** Singleton instance represented as zero-field immutable struct or constant reference.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Zero-field immutable struct 'NoGCPacer' serves as a unique type-level Singleton instance

### 427. singleton_immutable_instance on `FluxEltypeAdaptor` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/functor.jl:120:1`
- **Summary:** Singleton instance represented as zero-field immutable struct or constant reference.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Zero-field immutable struct 'FluxEltypeAdaptor' serves as a unique type-level Singleton instance

### 428. singleton_immutable_instance on `GlobalMaxPool` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:663:1`
- **Summary:** Singleton instance represented as zero-field immutable struct or constant reference.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Zero-field immutable struct 'GlobalMaxPool' serves as a unique type-level Singleton instance

### 429. singleton_immutable_instance on `GlobalMeanPool` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:697:1`
- **Summary:** Singleton instance represented as zero-field immutable struct or constant reference.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_SINGLETON_STRUCT): Zero-field immutable struct 'GlobalMeanPool' serves as a unique type-level Singleton instance

### 430. composite_struct_tree on `Optimiser` (88% [VERY_HIGH])
- **Category:** `structural`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:566:1`
- **Summary:** Recursive tree structure treating individual leaf nodes and composite groups uniformly.
- **Evidence Trail:**
  - `+88%` (STRUCTURAL_COMPOSITE_TREE): Struct 'Optimiser' implements Composite pattern holding recursive tree collections

### 431. facade_coordinator_module on `Train` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `module`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:1:1`
- **Summary:** Unified module API orchestrating multiple underlying subsystems, solvers, or data sources.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_MODULE): Module 'Train' acts as unified Facade coordinating multiple subsystem components

### 432. facade_coordinator_module on `DistributedUtils` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `module`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:5:1`
- **Summary:** Unified module API orchestrating multiple underlying subsystems, solvers, or data sources.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_MODULE): Module 'DistributedUtils' acts as unified Facade coordinating multiple subsystem components

### 433. proxy_lazy_or_remote on `LazyLayer` (88% [VERY_HIGH])
- **Category:** `structural`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:272:1`
- **Summary:** Surrogate struct controlling access or delaying evaluation of expensive target resources.
- **Evidence Trail:**
  - `+88%` (STRUCTURAL_PROXY_SURROGATE): Struct 'LazyLayer' acts as Proxy surrogate controlling access to target service

### 434. type_instability_non_concrete_field on `LazyLayer` (92% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/outputsize.jl:274:1`
- **Summary:** Struct field defined with abstract type or untyped `Any`, causing boxing and runtime dispatch.
- **Evidence Trail:**
  - `+92%` (HAZARD_TYPE_INSTABILITY_FIELD): Struct 'LazyLayer' has non-concrete field(s) (make::Function, layer::Any) causing runtime boxing; parameterize type (e.g. struct LazyLayer{T} ... end)

### 435. type_instability_non_concrete_field on `Model` (92% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:266:1`
- **Summary:** Struct field defined with abstract type or untyped `Any`, causing boxing and runtime dispatch.
- **Evidence Trail:**
  - `+92%` (HAZARD_TYPE_INSTABILITY_FIELD): Struct 'Model' has non-concrete field(s) (h0::AbstractVector) causing runtime boxing; parameterize type (e.g. struct Model{T} ... end)

### 436. type_instability_non_concrete_field on `Model` (92% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/recurrent.jl:477:1`
- **Summary:** Struct field defined with abstract type or untyped `Any`, causing boxing and runtime dispatch.
- **Evidence Trail:**
  - `+92%` (HAZARD_TYPE_INSTABILITY_FIELD): Struct 'Model' has non-concrete field(s) (c0::AbstractVector) causing runtime boxing; parameterize type (e.g. struct Model{T} ... end)

### 437. type_instability_non_concrete_field on `WeightDecay` (92% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:686:1`
- **Summary:** Struct field defined with abstract type or untyped `Any`, causing boxing and runtime dispatch.
- **Evidence Trail:**
  - `+92%` (HAZARD_TYPE_INSTABILITY_FIELD): Struct 'WeightDecay' has non-concrete field(s) (wd::Real) causing runtime boxing; parameterize type (e.g. struct WeightDecay{T} ... end)

### 438. type_instability_non_concrete_field on `DistributedDataContainer` (92% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `struct`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/public_api.jl:246:1`
- **Summary:** Struct field defined with abstract type or untyped `Any`, causing boxing and runtime dispatch.
- **Evidence Trail:**
  - `+92%` (HAZARD_TYPE_INSTABILITY_FIELD): Struct 'DistributedDataContainer' has non-concrete field(s) (data::Any, idxs::Any) causing runtime boxing; parameterize type (e.g. struct DistributedDataContainer{T} ... end)

### 439. fat_abstract_type_isp on `AbstractOptimiser` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `abstract_type`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/optimise/optimisers.jl:1:1`
- **Summary:** Abstract type expecting too many mandatory method implementations.
- **Evidence Trail:**
  - `+85%` (ISP_FAT_ABSTRACT_TYPE): Abstract type 'AbstractOptimiser' enforces 9 required methods; consider decomposing into Holy Traits or smaller contracts

### 440. fat_abstract_type_isp on `AbstractFluxDistributedBackend` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `abstract_type`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/distributed/backend.jl:5:1`
- **Summary:** Abstract type expecting too many mandatory method implementations.
- **Evidence Trail:**
  - `+85%` (ISP_FAT_ABSTRACT_TYPE): Abstract type 'AbstractFluxDistributedBackend' enforces 9 required methods; consider decomposing into Holy Traits or smaller contracts

### 441. manual_type_branch_cascade_ocp on `_big_show` (90% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:39:1`
- **Summary:** Using repeated `if x isa TypeA ... elseif x isa TypeB` instead of Multiple Dispatch.
- **Evidence Trail:**
  - `+90%` (OCP_MANUAL_ISA_CASCADE): Function '_big_show' uses 3 manual 'isa' type checks; replace with idiomatic Julia Multiple Dispatch to satisfy OCP

### 442. kiss_cyclomatic_complexity on `train!` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:198:1`
- **Summary:** Function containing excessive branching logic (> 8 decision branches).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function 'train!' has high cyclomatic complexity (13 branch points), violating KISS

### 443. kiss_cyclomatic_complexity on `maybe_gc!` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:79:1`
- **Summary:** Function containing excessive branching logic (> 8 decision branches).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function 'maybe_gc!' has high cyclomatic complexity (9 branch points), violating KISS

### 444. kiss_cyclomatic_complexity on `_print_conv_opt` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:235:1`
- **Summary:** Function containing excessive branching logic (> 8 decision branches).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function '_print_conv_opt' has high cyclomatic complexity (10 branch points), violating KISS

### 445. kiss_cyclomatic_complexity on `_big_show` (88% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/show.jl:39:1`
- **Summary:** Function containing excessive branching logic (> 8 decision branches).
- **Evidence Trail:**
  - `+88%` (KISS_CYCLOMATIC_COMPLEXITY): Function '_big_show' has high cyclomatic complexity (13 branch points), violating KISS

### 446. kiss_long_parameter_list on `loadmodel!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:25:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'loadmodel!' accepts 8 parameters; consider bundling into a configuration struct

### 447. kiss_long_parameter_list on `loadmodel!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:32:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'loadmodel!' accepts 8 parameters; consider bundling into a configuration struct

### 448. kiss_long_parameter_list on `loadmodel!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/deprecations.jl:37:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'loadmodel!' accepts 7 parameters; consider bundling into a configuration struct

### 449. kiss_long_parameter_list on `trainstep!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:329:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'trainstep!' accepts 6 parameters; consider bundling into a configuration struct

### 450. kiss_long_parameter_list on `_trainstep!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:335:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function '_trainstep!' accepts 6 parameters; consider bundling into a configuration struct

### 451. kiss_long_parameter_list on `trainstep_withgradient!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:360:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'trainstep_withgradient!' accepts 6 parameters; consider bundling into a configuration struct

### 452. kiss_long_parameter_list on `_trainstep_withgradient!` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/train.jl:366:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function '_trainstep_withgradient!' accepts 6 parameters; consider bundling into a configuration struct

### 453. kiss_long_parameter_list on `focal_loss` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/losses/functions.jl:610:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'focal_loss' accepts 7 parameters; consider bundling into a configuration struct

### 454. kiss_long_parameter_list on `calc_padding` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:55:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'calc_padding' accepts 6 parameters; consider bundling into a configuration struct

### 455. kiss_long_parameter_list on `calc_padding` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Julia/benchmark_repos/Flux.jl/src/layers/conv.jl:385:1`
- **Summary:** Function accepting >= 6 positional parameters.
- **Evidence Trail:**
  - `+85%` (KISS_LONG_PARAMETER_LIST): Function 'calc_padding' accepts 6 parameters; consider bundling into a configuration struct

### 456. dry_duplicate_logic on `outputsize` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic blocks across multiple functions.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 2 function(s): outputsize, outputsize
