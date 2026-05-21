from Mihu_physics.core.concept import Concept

normal_modes = Concept(

    name="Normal Modes",

    definition="""
A normal mode is a special type of motion in a coupled system where all parts oscillate with the same angular frequency and fixed amplitude relationships.
In this motion, the system behaves as if it were a single oscillator.
""",

    explanation="""
Normal modes describe the organized motion of coupled oscillators.

Instead of chaotic energy exchange between components, the system can move in very specific patterns where everything stays synchronized.

In these special cases:
- every part oscillates with the same frequency
- the ratio of amplitudes between oscillators stays constant
- the motion becomes fully predictable and structured

Even though the system contains multiple interacting parts, in a normal mode it behaves as a single effective oscillator.

---


Consider two coupled pendulums of mass m and length l connected by a spring of constant k.

Each pendulum pulls on the other.
Energy is exchanged through the spring.

If one moves, it influences the other immediately.

This is why the system is coupled — the equations are linked.
""",

    derivation="""
Let’s begin carefully.

We consider two identical pendulums of mass m and length l, connected by a spring with constant k.

For small angles, we use the approximation:
sin(θ) ≈ θ

So the equations of motion become:

m d²x₁/dt² = -m (g/l) x₁ + k(x₂ - x₁)

m d²x₂/dt² = -m (g/l) x₂ - k(x₂ - x₁)

Divide both equations by m:

d²x₁/dt² + (g/l)x₁ = (k/m)(x₂ - x₁)

d²x₂/dt² + (g/l)x₂ = -(k/m)(x₂ - x₁)

Introduce definitions:

ω₀² = g/l
ω_s² = k/m

So we rewrite:

d²x₁/dt² + ω₀² x₁ = ω_s² (x₂ - x₁)

d²x₂/dt² + ω₀² x₂ = -ω_s² (x₂ - x₁)

---

Now comes the key problem:

The equations are coupled.

x₁ depends on x₂, and x₂ depends on x₁.

This is not convenient.

But it is not a problem of physics.

It is a problem of coordinates.

---

We change variables.

Instead of tracking each pendulum separately, we define:

X₁ = x₁ + x₂   (collective motion)
X₂ = x₂ - x₁   (relative motion)

This is not new physics.

It is a better description of the same physics.

---

Now substitute into the equations.

After algebraic combination, the system decouples:

d²X₁/dt² + ω₀² X₁ = 0

d²X₂/dt² + (ω₀² + 2ω_s²) X₂ = 0

---

Now the magic happens.

We transformed a coupled system into two independent oscillators.

Each one is a normal mode.

---

The solutions are:

Mode 1:
ω₁ = ω₀

Mode 2:
ω₂ = √(ω₀² + 2ω_s²)

Each mode oscillates independently.
No coupling remains.
""",

    deep_dive="""
Stop thinking of this as two pendulums.

Think in terms of structure.

---

Originally, the system lived in a 2D configuration space:
(x₁, x₂)

But that space is not the natural one.

It hides symmetry.

So we rotate the coordinates:

From (x₁, x₂)
to (X₁, X₂)

This is not just algebra.

It is a change of perspective that reveals the true degrees of freedom.

---

Normal modes are not “new motions”.

They are eigenvectors of the system.

Just like in linear algebra:
- matrices have eigenvectors
- oscillatory systems have normal modes

Same idea.

Different language.

---

In the normal mode basis:
- energy does not mix between modes
- each mode evolves independently
- the system becomes diagonal in its dynamics

That is why the motion becomes “clean”.

No interference between coordinates.

---

Physical meaning:

Mode 1 (X₁):
Both pendulums move together.
The spring is not stretched.

Mode 2 (X₂):
Pendulums move opposite each other.
The spring is maximally involved.

---

So what looks like complexity is actually just two hidden simple oscillators.

Nature is not complicated.

Our coordinates were.
"""
)