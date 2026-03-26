from core.concept import Concept

damped_oscillations = Concept(

    name="Damped Oscillations",

    definition="""
Oscillatory motion in which the system loses energy over time due to dissipative forces.
Unlike ideal oscillators (like a perfect spring or pendulum), energy is not perfectly conserved.
This dissipation can arise from friction, air resistance, viscosity, or any form of energy transfer to the surroundings.
The motion gradually slows down, with amplitude decreasing over time.
""",

    explanation="""
In classical mechanics, we often start with idealizations: a mass on a spring, a pendulum, or a floating body.
These ideal systems ignore friction, air resistance, and any other source of energy loss.
They are convenient for deriving exact formulas, understanding concepts, and practicing calculations.

But real-world systems are never ideal.

Energy leaks out of the system into the environment — we call this dissipation.
It is always opposed to the motion. The resisting force F_resistive can be generally written as:

    F_resistive = -C1 * v - C2 * |v| * v

- The first term is linear in velocity (viscous damping)
- The second term is quadratic in velocity (air drag at higher speeds)

The linear term allows an analytical solution; the quadratic term usually requires numerical methods.
In practical physics, we often neglect the quadratic term to preserve solvability, unless precision matters.

---

There are two main ways to solve damped oscillations:

1. **Analytical solution**: Solve the differential equation and get x(t) as a formula.
   Example: x(t) = A * cos(ω t + φ) * e^{-γ t/2}
   You can analyze, differentiate, integrate, and evaluate this formula at any time.

2. **Numerical solution**: Calculate x(t) at discrete points.
   Useful if the equation is nonlinear or too complex for a closed form.
   You start with initial conditions x(0), dx/dt(0), then step forward in time.
   You end up with a table or graph instead of a formula.
""",

    derivation="""
Let's derive the damped oscillator equation, step by step.

1. **Start from Newton's second law:**
    m * d²x/dt² = -k * x - b * dx/dt

    - m: mass of the body
    - k: spring constant
    - b: damping coefficient
    - x: displacement
    - dx/dt: velocity

The damping force is assumed proportional to velocity and acts opposite to motion.
We divide through by m to write in standard form:

    d²x/dt² + γ * dx/dt + ω₀² * x = 0

Where:

    γ = b/m   (damping factor)
    ω₀² = k/m (natural frequency of the undamped system)

2. **Expected behavior:**
   - The amplitude decays over time because energy is lost.
   - The observed frequency ω is slightly less than ω₀.
   - The period remains roughly constant (unless damping is very strong).

3. **Move to the complex plane for elegant solution:**
   Introduce complex variable z(t) such that x(t) = Re(z(t)).
   The equation becomes:

       d²z/dt² + γ dz/dt + ω₀² z = 0

   Assume a solution of the form:

       z(t) = A * e^{λ t}

   Plug into the equation:

       λ² + γ λ + ω₀² = 0

   Solve the quadratic:

       λ = -γ/2 ± i * sqrt(ω₀² - (γ/2)²) = -γ/2 ± iω

   So the general solution is:

       z(t) = A * e^{-γ/2 t} * e^{i(ω t + φ)}

   Take the real part to get physical displacement:

       x(t) = A * e^{-γ/2 t} * cos(ω t + φ)

4. **Interpretation:**
   - Exponential term e^{-γ/2 t} → amplitude decays exponentially
   - Cosine term → oscillates with damped frequency ω
   - A, φ → determined by initial conditions x(0) and dx/dt(0)
   - γ → controls how fast energy dissipates

5. **Special cases:**
   - Underdamped: γ < 2ω₀ → oscillatory decay
   - Critically damped: γ = 2ω₀ → returns to equilibrium fastest without oscillating
   - Overdamped: γ > 2ω₀ → returns to equilibrium slowly without oscillations
""",

    deep_dive="""
We could also add some deeper insights...

First and foremost, real oscillators always leak energy into surroundings; ideal models are just approximations.
Secondly, linear damping leads to analytically solvable equations; quadratic damping usually requires numerical simulations.
Thirdly, moving to the complex plane simplifies solving, because derivatives of exponentials are trivial.
To be precise, exponential decay factor e^{-γ/2 t} naturally separates damping from oscillation. The damped frequency ω = sqrt(ω₀² - (γ/2)²) is always less than the undamped frequency ω₀.

- Factor of quality (Q):

      Q = ω₀ / γ

  - High Q → weak damping, slow decay
  - Low Q → strong damping, fast decay

Understanding initial conditions (x0, v0) is crucial: they set amplitude and phase exactly. This approach can be generalized to other systems: electrical circuits, pendulums in air, floating bodies with drag.

The beauty of physics: not just what exists, but what actually participates in motion and energy exchange.
"""
)