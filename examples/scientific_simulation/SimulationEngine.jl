module SimulationEngine

using ..PhysicsTypes
using ..Solvers

export EngineBuilder, run_parallel_simulation

struct EngineBuilder
    timestep::Float64
    total_steps::Int
end

function run_parallel_simulation(particles::Vector{Particle{Float64}}, builder::EngineBuilder)
    event_channel = Channel{Int}(64)

    @sync begin
        @async begin
            for step in 1:builder.total_steps
                Threads.@threads for i in 1:length(particles)
                    step_simulation!(particles[i], builder.timestep)
                end
                put!(event_channel, step)
            end
            close(event_channel)
        end
    end
end

end # module
