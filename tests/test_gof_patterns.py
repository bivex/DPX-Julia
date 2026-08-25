"""Unit tests for all 23 GoF Creational, Structural, and Behavioral patterns in Julia."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_julia_parser import NativeJuliaParserAdapter
from pattern_detector.domain.rules.behavioral_rules import (
    ChainOfResponsibilityPipelineRule,
    CommandCallableTaskRule,
    InterpreterAstEvalRule,
    IteratorBaseProtocolRule,
    MediatorCentralCoordinatorRule,
    MementoStateSnapshotRule,
    ObserverChannelSubscriptionRule,
    StateAbstractTypeFsmRule,
    StrategyTraitAlgorithmRule,
    TemplateMethodSkeletonRule,
    VisitorMultipleDispatchRule,
)
from pattern_detector.domain.rules.creational_rules import (
    AbstractFactoryHierarchyRule,
    BuilderFluentStructRule,
    FactoryMethodConstructorRule,
    PrototypeDeepcopyRule,
    SingletonImmutableInstanceRule,
)
from pattern_detector.domain.rules.structural_rules import (
    AdapterWrapperStructRule,
    BridgeDriverDecouplingRule,
    CompositeStructTreeRule,
    DecoratorForwardingWrapperRule,
    FacadeCoordinatorModuleRule,
    FlyweightPoolCacheRule,
    ProxyLazyOrRemoteRule,
)
from pattern_detector.domain.value_objects import PatternType


# --- Creational (5/5) ---

def test_singleton_immutable_instance() -> None:
    code = """
    struct GlobalApplicationConfig end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("singleton.jl", code)])

    rule = SingletonImmutableInstanceRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SINGLETON_IMMUTABLE_INSTANCE


def test_factory_method_constructor() -> None:
    code = """
    function create_optimizer(type::Symbol)
        if type == :adam
            return AdamOptimizer()
        end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("factory.jl", code)])

    rule = FactoryMethodConstructorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FACTORY_METHOD_CONSTRUCTOR


def test_abstract_factory_hierarchy() -> None:
    code = """
    abstract type GUIComponentFactory end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("abs_factory.jl", code)])

    rule = AbstractFactoryHierarchyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ABSTRACT_FACTORY_HIERARCHY


def test_builder_fluent_struct() -> None:
    code = """
    struct QueryBuilder
        select_fields::Vector{String}
        where_clause::String
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("builder.jl", code)])

    rule = BuilderFluentStructRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BUILDER_FLUENT_STRUCT


def test_prototype_deepcopy() -> None:
    code = """
    function Base.deepcopy(obj::CustomModel)
        return CustomModel(copy(obj.params))
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("copy.jl", code)])

    rule = PrototypeDeepcopyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PROTOTYPE_DEEPCOPY


# --- Structural (7/7) ---

def test_adapter_wrapper_struct() -> None:
    code = """
    struct LegacyStreamAdapter
        stream::IOStream
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("adapter.jl", code)])

    rule = AdapterWrapperStructRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ADAPTER_WRAPPER_STRUCT


def test_bridge_driver_decoupling() -> None:
    code = """
    struct GraphicsPipeline
        backend_driver::VulkanBackend
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("bridge.jl", code)])

    rule = BridgeDriverDecouplingRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BRIDGE_DRIVER_DECOUPLING


def test_composite_struct_tree() -> None:
    code = """
    struct ASTNode
        name::String
        children::Vector{ASTNode}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("composite.jl", code)])

    rule = CompositeStructTreeRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPOSITE_STRUCT_TREE


def test_decorator_forwarding_wrapper() -> None:
    code = """
    struct LoggingDecorator
        inner::CalculationEngine
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("decorator.jl", code)])

    rule = DecoratorForwardingWrapperRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DECORATOR_FORWARDING_WRAPPER


def test_facade_coordinator_module() -> None:
    code = """
    module DatabaseFacade
        struct Connection end
        struct Pool end
        struct Query end

        function connect() end
        function execute() end
        function close() end
        function ping() end
        function status() end
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("facade.jl", code)])

    rule = FacadeCoordinatorModuleRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FACADE_COORDINATOR_MODULE


def test_flyweight_pool_cache() -> None:
    code = """
    struct GlyphPool
        cache::Dict{Char, Glyph}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("flyweight.jl", code)])

    rule = FlyweightPoolCacheRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FLYWEIGHT_POOL_CACHE


def test_proxy_lazy_or_remote() -> None:
    code = """
    struct LazyDatasetProxy
        url::String
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("proxy.jl", code)])

    rule = ProxyLazyOrRemoteRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PROXY_LAZY_OR_REMOTE


# --- Behavioral (11/11) ---

def test_chain_of_responsibility() -> None:
    code = """
    struct AuthHandler
        next_handler::AuthHandler
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("chain.jl", code)])

    rule = ChainOfResponsibilityPipelineRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CHAIN_OF_RESPONSIBILITY_PIPELINE


def test_command_callable_task() -> None:
    code = """
    struct SaveFileCommand
        path::String
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("command.jl", code)])

    rule = CommandCallableTaskRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMMAND_CALLABLE_TASK


def test_interpreter_ast_eval() -> None:
    code = """
    function interpret(node::ASTNode)
        return 42
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("eval.jl", code)])

    rule = InterpreterAstEvalRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.INTERPRETER_AST_EVAL


def test_iterator_base_protocol() -> None:
    code = """
    function Base.iterate(iter::CustomSequence, state=1)
        if state > length(iter)
            return nothing
        end
        return (iter[state], state + 1)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("iter.jl", code)])

    rule = IteratorBaseProtocolRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ITERATOR_BASE_PROTOCOL


def test_mediator_central_coordinator() -> None:
    code = """
    struct EventCoordinator
        listeners::Vector{Function}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("mediator.jl", code)])

    rule = MediatorCentralCoordinatorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MEDIATOR_CENTRAL_COORDINATOR


def test_memento_state_snapshot() -> None:
    code = """
    struct SimulationStateSnapshot
        timestep::Int
        energy::Float64
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("memento.jl", code)])

    rule = MementoStateSnapshotRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MEMENTO_STATE_SNAPSHOT


def test_observer_channel_subscription() -> None:
    code = """
    struct NewsPublisher
        subscribers::Vector{Channel{String}}
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("observer.jl", code)])

    rule = ObserverChannelSubscriptionRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.OBSERVER_CHANNEL_SUBSCRIPTION


def test_state_abstract_type_fsm() -> None:
    code = """
    abstract type ConnectionState end
    struct ConnectedState <: ConnectionState end
    struct DisconnectedState <: ConnectionState end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("state.jl", code)])

    rule = StateAbstractTypeFsmRule()
    detections = rule.evaluate(model)

    assert len(detections) >= 1
    assert detections[0].pattern_type == PatternType.STATE_ABSTRACT_TYPE_FSM


def test_strategy_trait_algorithm() -> None:
    code = """
    struct OptimizationContext
        solver_strategy::GradientDescentStrategy
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("strategy.jl", code)])

    rule = StrategyTraitAlgorithmRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STRATEGY_TRAIT_ALGORITHM


def test_template_method_skeleton() -> None:
    code = """
    function process_pipeline(data)
        step1_validate(data)
        step2_transform(data)
        step3_save(data)
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("template.jl", code)])

    rule = TemplateMethodSkeletonRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TEMPLATE_METHOD_SKELETON


def test_visitor_multiple_dispatch() -> None:
    code = """
    function visit(node::ASTNode, context::VisitorContext)
        println("Visiting node")
    end
    """
    parser = NativeJuliaParserAdapter()
    model = parser.parse_codebase([("visitor.jl", code)])

    rule = VisitorMultipleDispatchRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.VISITOR_MULTIPLE_DISPATCH
