from Mihu_physics.core.concept import Concept

normal_modes_method = Concept(

    name="Normal Modes - Method of Solution",

    definition="""
A systematic procedure for finding the natural independent oscillation patterns of a coupled system.
Each normal mode corresponds to a motion where all parts oscillate with the same frequency.
""",

    explanation="""
Normal modes are not guessed — they are constructed step by step from the equations of motion.

The goal is to take a coupled system (messy, interconnected equations) and transform it into independent harmonic oscillators.

Instead of chaos, you find structure.

Instead of coupled motion, you find pure patterns.
""",

    derivation="""
Let’s build the method step by step.

---

1. Start with the physical system

Draw the system first.

- Place each mass in equilibrium.
- Then displace each one slightly.

This is not calculation yet — this is setting the stage.

You define the geometry of motion.

---

2. Write Newton’s second law for each mass

Now identify all forces:

- spring forces
- gravitational components (if relevant)
- coupling forces between oscillators

Apply:

m d²x/dt² = ΣF

This gives you a system of coupled differential equations.

At this stage, the system looks complicated and entangled.

Each variable depends on the others.

---

3. Assume a normal mode solution

Now comes the key idea:

In a normal mode, every part of the system oscillates with the same frequency ω.

So we assume:

x₁(t) = C₁ cos(ωt)
x₂(t) = C₂ cos(ωt)

(and similarly for more oscillators)

Important:
- same ω for all
- different amplitudes C₁, C₂

This is the defining property of normal modes.

---

4. Substitute into equations of motion

We use:

d²x/dt² = -ω² x

So each equation becomes algebraic:

m ω² C₁ = (forces expressed in terms of C₁, C₂)
m ω² C₂ = (forces expressed in terms of C₁, C₂)

Now the differential system becomes a linear algebra problem.

We now have:
- 2 equations
- 3 unknowns: ω, C₁, C₂

---

5. Solve for eigenfrequencies

To get non-trivial motion (C₁, C₂ ≠ 0), the determinant condition must hold.

This gives allowed values of ω:

ω = ω₊, ω₋

Each ω corresponds to a different normal mode.

---

6. Determine mode shapes

For each ω, solve:

C₁ / C₂ = constant

This ratio defines the structure of the mode:

- in-phase motion
- out-of-phase motion
- symmetric or antisymmetric patterns

Each ω produces one unique spatial pattern.

---

7. Final solution

The full motion is a superposition:

x(t) = mode₊ + mode₋

Each mode is independent.

Each evolves separately in time.

Together they reconstruct the full motion of the system.

---

This is the hidden simplicity of coupled systems:

What looks like complexity is just a combination of a few pure oscillation patterns.
""",

    deep_dive="""
Normal modes are not just a mathematical trick.

They are a change of perspective.

---

Instead of thinking in terms of individual coordinates:

x₁, x₂, x₃ ...

you think in terms of collective coordinates:

Q₁, Q₂, Q₃ ...

These are independent directions in the system’s phase space.

---

This is why the method works:

You are diagonalizing the dynamics.

You are finding the eigenvectors of motion.

---

Each normal mode behaves like its own simple harmonic oscillator:

d²Q/dt² + ω² Q = 0

No coupling remains in this basis.

The system has been “decoded”.

---

Physical interpretation:

- Mode 1: usually symmetric motion (everything moves together)
- Mode 2: antisymmetric motion (opposite motion)

Higher systems produce richer patterns.

---

Key insight:

A system with N degrees of freedom ALWAYS has N normal modes.

No more. No less.

Because you cannot create extra independent motion directions.

---

So normal modes are not “special cases”.

They are the fundamental language of coupled oscillators.
"""
)