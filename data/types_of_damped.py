# data/damped_oscillations.py
from core.concept import Concept

types_damped = Concept(
    name="Damped Oscillations",
    
    definition="""
Oscillations in which the amplitude gradually decreases over time due to energy dissipation.
Common in real-world systems where friction or resistance is present.
""",
    
    explanation="""
In the real world, almost all oscillations lose energy to the environment — air resistance, friction, internal material damping, etc.
This loss is modeled as a resistive force:

F_resistive = -b * v

where b is the damping coefficient and v is the velocity.

Depending on the damping strength relative to the system's natural frequency, there are three regimes:

1. Underdamped (subcritical) – system oscillates with gradually decreasing amplitude:
   x(t) = A * exp(-γ t / 2) * cos(ω_d t + φ)
   where γ = b/m, ω_d = sqrt(ω_0^2 - (γ/2)^2)

2. Critically damped – system returns to equilibrium as fast as possible without oscillating:
   x(t) = (A + B*t) * exp(-γ t / 2)
   with γ = 2*ω_0

3. Overdamped (supercritical) – system returns to equilibrium without oscillating, but slower than critical damping:
   x(t) = C * exp(r1 * t) + D * exp(r2 * t)
   with r1,r2 = roots of the characteristic equation
""",
    
    derivation="""
Start from Newton's 2nd law with damping:

m * d²x/dt² + b * dx/dt + k * x = 0

Divide by m:

d²x/dt² + (b/m) * dx/dt + (k/m) * x = 0

Set γ = b/m, ω_0² = k/m:

d²x/dt² + γ * dx/dt + ω_0² * x = 0

Solve characteristic equation:

r² + γ r + ω_0² = 0

Discriminant Δ = γ² - 4 ω_0²

- If Δ < 0 → complex roots → underdamped (oscillatory)
  r = -γ/2 ± i ω_d, ω_d = sqrt(ω_0² - (γ/2)²)
  x(t) = A * e^(-γ t / 2) * cos(ω_d t + φ)

- If Δ = 0 → repeated root → critically damped
  r = -γ/2 = -ω_0
  x(t) = (A + B t) * e^(-ω_0 t)

- If Δ > 0 → real distinct roots → overdamped
  r1, r2 = -γ/2 ± sqrt((γ/2)² - ω_0²)
  x(t) = C * e^(r1 t) + D * e^(r2 t)
""",
    
    deep_dive="""
Key insights, Mihu style:

- Energy always decreases: E(t) = E0 * exp(-γ t) for underdamped.
- Underdamped: you still see oscillations, but amplitude shrinks exponentially.
- Critically damped: fastest non-oscillatory return to equilibrium — no overshoot.
- Overdamped: system is sluggish; equilibrium reached slower than critical.
- Quality factor Q = ω_0 / γ, measures "sharpness" of oscillation.
- Notice: period changes slightly for underdamped: T = 2π / ω_d < 2π / ω_0
- Complex plane trick: introduce z(t) = x(t) + i y(t), solve as exponential, then take Re(z(t)) → clean derivation of oscillatory behavior with damping.
- These regimes appear everywhere: car suspensions, building sway, electronics (RLC circuits), pendulums in viscous fluid.
- The formulae above let you predict exactly how quickly amplitude decays and how the system responds depending on damping.
"""
)