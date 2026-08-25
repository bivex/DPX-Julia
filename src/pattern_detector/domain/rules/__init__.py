"""Rules registry and aggregation factory for Julia pattern detector."""

from __future__ import annotations

from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.rules.idiomatic_rules import (
    BroadcastOperatorOverloadRule,
    ConversionPromotionProtocolRule,
    HolyTraitsDispatchRule,
    HomoiconicAstTransformRule,
    MetaprogrammingMacroDslRule,
    ParametricTypeSpecializationRule,
)
from pattern_detector.domain.rules.multiple_dispatch_rules import (
    MethodSpecializationTableRule,
    MultipleDispatchPolymorphismRule,
    OuterConstructorDispatchRule,
)
from pattern_detector.domain.rules.concurrency_rules import (
    AtomicMemoryOperationRule,
    ChannelCspPipelineRule,
    TaskAsyncCoroutineRule,
    ThreadsParallelLoopRule,
)
from pattern_detector.domain.rules.scientific_rules import (
    CallableStructFunctorRule,
    InPlaceMutatingConventionRule,
    ZeroAllocationViewRule,
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
from pattern_detector.domain.rules.resilience_hazards_rules import (
    HotLoopArrayAllocationRule,
    SwallowedTaskExceptionRule,
    TypeInstabilityNonConcreteFieldRule,
    UnsynchronizedGlobalRaceRule,
    UntypedGlobalMutationRule,
)
from pattern_detector.domain.rules.solid_principles_rules import (
    DemeterLawTrainWreckRule,
    DryDuplicateLogicRule,
    FatAbstractTypeIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    ManualTypeBranchCascadeOcpRule,
    MonolithicStructSrpRule,
)

DEFAULT_RULES: list[type[BaseRule]] = [
    # 1. Julia Idiomatic
    HolyTraitsDispatchRule,
    ParametricTypeSpecializationRule,
    MetaprogrammingMacroDslRule,
    HomoiconicAstTransformRule,
    BroadcastOperatorOverloadRule,
    ConversionPromotionProtocolRule,

    # 2. Multiple Dispatch
    MultipleDispatchPolymorphismRule,
    OuterConstructorDispatchRule,
    MethodSpecializationTableRule,

    # 3. Concurrency
    TaskAsyncCoroutineRule,
    ChannelCspPipelineRule,
    ThreadsParallelLoopRule,
    AtomicMemoryOperationRule,

    # 4. Scientific
    ZeroAllocationViewRule,
    InPlaceMutatingConventionRule,
    CallableStructFunctorRule,

    # 5. Creational GoF (5/5)
    SingletonImmutableInstanceRule,
    FactoryMethodConstructorRule,
    AbstractFactoryHierarchyRule,
    BuilderFluentStructRule,
    PrototypeDeepcopyRule,

    # 6. Structural GoF (7/7)
    AdapterWrapperStructRule,
    BridgeDriverDecouplingRule,
    CompositeStructTreeRule,
    DecoratorForwardingWrapperRule,
    FacadeCoordinatorModuleRule,
    FlyweightPoolCacheRule,
    ProxyLazyOrRemoteRule,

    # 7. Behavioral GoF (11/11)
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

    # 8. Resilience & Hazards
    TypeInstabilityNonConcreteFieldRule,
    UntypedGlobalMutationRule,
    HotLoopArrayAllocationRule,
    SwallowedTaskExceptionRule,
    UnsynchronizedGlobalRaceRule,

    # 9. SOLID & Quality
    MonolithicStructSrpRule,
    FatAbstractTypeIspRule,
    ManualTypeBranchCascadeOcpRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    DryDuplicateLogicRule,
    DemeterLawTrainWreckRule,
]


def get_default_rules() -> list[BaseRule]:
    """Instantiate and return full suite of default Julia rules."""
    return [
        # 1. Idiomatic
        HolyTraitsDispatchRule(),
        ParametricTypeSpecializationRule(),
        MetaprogrammingMacroDslRule(),
        HomoiconicAstTransformRule(),
        BroadcastOperatorOverloadRule(),
        ConversionPromotionProtocolRule(),

        # 2. Multiple Dispatch
        MultipleDispatchPolymorphismRule(),
        OuterConstructorDispatchRule(),
        MethodSpecializationTableRule(),

        # 3. Concurrency
        TaskAsyncCoroutineRule(),
        ChannelCspPipelineRule(),
        ThreadsParallelLoopRule(),
        AtomicMemoryOperationRule(),

        # 4. Scientific
        ZeroAllocationViewRule(),
        InPlaceMutatingConventionRule(),
        CallableStructFunctorRule(),

        # 5. Creational (5/5)
        SingletonImmutableInstanceRule(),
        FactoryMethodConstructorRule(),
        AbstractFactoryHierarchyRule(),
        BuilderFluentStructRule(),
        PrototypeDeepcopyRule(),

        # 6. Structural (7/7)
        AdapterWrapperStructRule(),
        BridgeDriverDecouplingRule(),
        CompositeStructTreeRule(),
        DecoratorForwardingWrapperRule(),
        FacadeCoordinatorModuleRule(),
        FlyweightPoolCacheRule(),
        ProxyLazyOrRemoteRule(),

        # 7. Behavioral (11/11)
        ChainOfResponsibilityPipelineRule(),
        CommandCallableTaskRule(),
        InterpreterAstEvalRule(),
        IteratorBaseProtocolRule(),
        MediatorCentralCoordinatorRule(),
        MementoStateSnapshotRule(),
        ObserverChannelSubscriptionRule(),
        StateAbstractTypeFsmRule(),
        StrategyTraitAlgorithmRule(),
        TemplateMethodSkeletonRule(),
        VisitorMultipleDispatchRule(),

        # 8. Resilience & Hazards
        TypeInstabilityNonConcreteFieldRule(),
        UntypedGlobalMutationRule(),
        HotLoopArrayAllocationRule(),
        SwallowedTaskExceptionRule(),
        UnsynchronizedGlobalRaceRule(),

        # 9. SOLID & Quality
        MonolithicStructSrpRule(),
        FatAbstractTypeIspRule(),
        ManualTypeBranchCascadeOcpRule(),
        KissCyclomaticComplexityRule(),
        KissLongParameterListRule(),
        DryDuplicateLogicRule(),
        DemeterLawTrainWreckRule(),
    ]
