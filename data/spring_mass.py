from core.concept import Concept

spring_with_mass = Concept(

    name="Spring with Mass",

    definition="""
A more realistic model of a spring where the spring itself has mass.
""",

    explanation="""
You assumed the spring was massless.

That was convenient.

It was also a lie.

Now we remove that simplification.
""",

    derivation="""
Let us set up the system.

A mass m is attached to a spring of length L and total mass M.

The spring is homogeneous.
Oscillations are small.
No friction. No air resistance.

---

Now ask the question:

Can we treat the entire mass of the spring as if it were concentrated at one point?

No.

You cannot.

Because the spring is not a rigid body.

Not all parts move the same way.

---

Imagine a bus full of people.

Some are standing still.
Some are walking.
Some are running.

If you are asked for total kinetic energy,
you cannot pretend everyone is moving at the same speed.

You must account for each one.

---

The spring is the same.

It is a chain of small masses.

Three regions:

- The fixed end → velocity is zero
- The free end → velocity is maximum
- Everything in between → interpolates

---

So we take an infinitesimal piece.

Let linear density be:

ρ = M / L

Take a small segment ds.

Its mass is:

dM = (M / L) ds

---

Now describe motion.

If the total extension is x(t):

- At s = 0 → displacement = 0
- At s = L → displacement = x(t)

So at position s:

x'(s, t) = (s / L) x(t)

---

Velocity:

v(s, t) = d/dt [x'] = (s / L) dx/dt

---

Now kinetic energy of that piece:

dE = 1/2 dM v²

Substitute:

dE = 1/2 * (M / L) ds * (s² / L²)(dx/dt)²

dE = (M / 2L³)(dx/dt)² s² ds

---

Total kinetic energy:

Integrate from 0 to L:

E = ∫ dE

E = (M / 2L³)(dx/dt)² ∫₀ᴸ s² ds

E = (M / 2L³)(dx/dt)² * (L³ / 3)

E = (1/6) M (dx/dt)²

---

So the spring behaves as if:

Only one third of its mass contributes to kinetic energy.

---

Total energy:

E = 1/2 kx² + 1/2 m (dx/dt)² + 1/6 M (dx/dt)²

E = 1/2 kx² + 1/2 (m + M/3)(dx/dt)²

---

So the system behaves like:

An effective mass:

m_eff = m + M/3

---

Equation of motion:

m_eff d²x/dt² + kx = 0

---

Angular frequency:

ω² = k / (m + M/3)
""",

    deep_dive="""
Your intuition already knew the answer.

Not everything moves equally.

So not everything contributes equally.

---

The spring is not a point.

It is a distribution.

And when you move from point-mass thinking to distributed systems,
you stop summing objects…

and start integrating structure.

---

The factor 1/3 is not magic.

It is geometry.

It comes from how velocity scales linearly along the spring.

Square that scaling → integrate → you get 1/3.

---

So the statement:

“The spring has mass M”

is incomplete.

The correct statement is:

“The spring contributes M/3 dynamically.”

---

Physics is not about what exists.

It is about what actually participates.
"""
)