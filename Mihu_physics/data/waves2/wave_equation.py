from Mihu_physics.core.concept import Concept

wave_equation_derivation = Concept(

    name="Wave Equation from Discrete Chain of Oscillators",

    definition="""
A wave equation describes how local disturbances in a medium propagate through space and time.

It emerges from a system of coupled oscillators where each element interacts only with its nearest neighbours.

The key idea is: local coupling + continuity limit → wave propagation.
""",

    explanation="""
We begin with a physical model of a stretched string (or equivalently a chain of masses connected by springs).

The system is DISCRETE:
- It consists of individual masses (or particles)
- Each mass is labeled by an index r
- Each mass has displacement y_r(t) from equilibrium

Even though the system looks continuous, it is fundamentally a set of coupled oscillators.

Each mass interacts only with its nearest neighbours.
""",

    derivation="""
STEP 1: DISCRETE MODEL OF THE SYSTEM

Consider a chain of masses connected by identical springs (or equivalently a stretched string under tension).

Each mass at position r has displacement:

    y_r(t)

Now we analyze the forces acting on mass r.

---

STEP 2: FORCES FROM NEIGHBOURS

Right neighbour (r+1):

    F_right = k (y_{r+1} - y_r)

Left neighbour (r-1):

    F_left = k (y_{r-1} - y_r)

Total force on mass r:

    F = F_right + F_left

So:

    F = k[(y_{r+1} - y_r) + (y_{r-1} - y_r)]

Expanding:

    F = k (y_{r+1} + y_{r-1} - 2y_r)

---

STEP 3: NEWTON'S SECOND LAW

Apply Newton’s law:

    m d²y_r/dt² = k (y_{r+1} + y_{r-1} - 2y_r)

Divide by mass:

    d²y_r/dt² = (k/m)(y_{r+1} + y_{r-1} - 2y_r)

For a stretched string under tension T, the effective form becomes:

    d²y_r/dt² = (T/(m a)) (y_{r+1} + y_{r-1} - 2y_r)

where:
- a = distance between neighbouring masses

---

STEP 4: INTERPRETATION

This equation already shows the key physics:

- Each point accelerates depending on the difference between itself and its neighbours
- This is why disturbances propagate

A single point cannot evolve independently → coupling creates propagation.

---

STEP 5: CONTINUUM LIMIT

Now we transition from discrete to continuous description.

Define spatial coordinate:

    x = r a

So the discrete function becomes a field:

    y_r(t) → y(x,t)

Neighbour points become:

    y_{r+1}(t) = y(x + a, t)
    y_{r-1}(t) = y(x - a, t)

---

STEP 6: TIME DERIVATIVE BECOMES PARTIAL DERIVATIVE

Since y depends on both space and time:

    d²y_r/dt² → ∂²y(x,t)/∂t²

So equation becomes:

∂²y/∂t² = (T/(m a)) [y(x+a,t) + y(x-a,t) - 2y(x,t)]

---

STEP 7: TAYLOR EXPANSION

Now expand around x.

For y(x+a,t):

    y(x+a,t) = y + a ∂y/∂x + (a²/2) ∂²y/∂x² + ...

For y(x-a,t):

    y(x-a,t) = y - a ∂y/∂x + (a²/2) ∂²y/∂x² + ...

Now add them:

y(x+a,t) + y(x-a,t) - 2y(x,t) = a² ∂²y/∂x²

Higher order terms cancel or vanish in limit a → 0.

---

STEP 8: SUBSTITUTE BACK

Insert into equation:

∂²y/∂t² = (T/(m a)) * (a² ∂²y/∂x²)

Simplify:

∂²y/∂t² = (T a / m) ∂²y/∂x²

---

STEP 9: MASS DENSITY (IMPORTANT STEP)

Define linear mass density:

    μ = m / a

So:

    m = μ a

Substitute:

(T a / m) = (T a) / (μ a) = T / μ

---

STEP 10: FINAL FORM

We obtain:

∂²y/∂t² = (T/μ) ∂²y/∂x²

Define wave speed:

    v² = T/μ

FINAL RESULT:

∂²y/∂t² = v² ∂²y/∂x²

""",

    deep_dive="""
This derivation shows something very important:

A wave is NOT a substance moving through space.

It is a consequence of LOCAL INTERACTION.

Each point in the medium:
- does not know global motion
- only reacts to its immediate neighbours

That local rule creates global behaviour.

---

WHY TAYLOR EXPANSION MATTERS

The Taylor expansion is the bridge between:
- discrete physics (particles)
- continuous physics (fields)

It replaces:
    difference between neighbours
with
    spatial derivatives

This is where calculus emerges from physics.

---

PHYSICAL MEANING OF THE WAVE EQUATION

∂²y/∂t² = v² ∂²y/∂x²

Left side:
→ how fast the system accelerates in time

Right side:
→ how curved the string is in space

Meaning:

If a point is higher or lower than its surroundings,
it experiences a restoring acceleration.

---

WHY WAVES TRAVEL

Propagation happens because:
- one point pulls the next
- but response is delayed
- that delay creates motion transfer

So energy moves forward,
but matter does not.

---

WHAT IS ACTUALLY MOVING?

Not particles.
Not medium.

Only:
- disturbance pattern
- information about displacement

---

WHY THIS IS FUNDAMENTAL

This same structure appears in:
- sound waves
- waves on strings
- electromagnetic waves (with different fields)
- quantum wave functions (mathematical analogy)

So this equation is one of the deepest structures in physics.

"""
)