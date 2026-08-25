module PhysicsTypes

export AbstractSimulationEngine, IntegrationTrait, RK4Trait, EulerTrait, Particle, SimulationState

abstract type IntegrationTrait end
struct RK4Trait <: IntegrationTrait end
struct EulerTrait <: IntegrationTrait end

integration_trait(::Type) = RK4Trait()

struct Particle{T<:Real}
    position::Vector{T}
    velocity::Vector{T}
    mass::Float64
end

abstract type SimulationState end
struct RunningState <: SimulationState end
struct PausedState <: SimulationState end
struct TerminatedState <: SimulationState end

end # module
