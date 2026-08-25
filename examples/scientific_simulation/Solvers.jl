module Solvers

using ..PhysicsTypes

export step_simulation!, PotentialFunctor

struct PotentialFunctor
    k::Float64
end

(pf::PotentialFunctor)(r::Float64) = 0.5 * pf.k * r^2

function step_simulation!(p::Particle{T}, dt::T) where {T<:Real}
    p.position .+= p.velocity .* dt
end

function compute_kinetic_energy(particles::Vector{Particle{T}}) where {T<:Real}
    v_slice = @views [p.velocity for p in particles]
    return sum(0.5 * p.mass * sum(p.velocity.^2) for p in particles)
end

end # module
