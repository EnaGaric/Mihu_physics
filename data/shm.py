from core.concept import Concept
from data.oscilations import oscilations

shm = Concept(
    name="Simple Harmonic Motion",

    definition=oscilations["shm"]["definition"],

    explanation=oscilations["shm"]["mihu"],

    formulas=[oscilations["shm"]["formula"]],

    terms=oscilations,

    derivation="""
Let’s begin carefully.

Consider a body subject to a force:

F = -kx

This force originates from an ideal spring.
We neglect the mass of the spring, as well as air resistance and friction.

Nothing interferes. The system is clean.

Now apply Newton’s second law.

Force equals mass times acceleration.

F = ma

So:

m d²x/dt² = -kx

Rearrange:

d²x/dt² + (k/m)x = 0

Introduce a substitution:

ω² = k/m

And the equation becomes:

d²x/dt² + ω²x = 0

This is the equation of motion for a simple harmonic oscillator.

---

Now comes the part most people try to memorize instead of understand.

“This equation needs to be solved.”

But you do not solve it by force.

You propose a function — any function — and test whether it satisfies the equation.

Most functions will fail.

Some survive.

You could attempt a Taylor expansion. It works. Eventually.

But there is a more elegant choice.

Sine and cosine.

Functions that do not collapse under differentiation, but instead transform into each other.

Insert them, and the structure remains intact.

That is not coincidence. That is compatibility.

---

This is a second-order linear homogeneous differential equation.

Which means:

Its solutions form a structured space.

Not random. Not chaotic.

Structured.

And from that structure, the general solution emerges:

x(t) = a cos(ωt) + b sin(ωt)

Where a and b are constants.

Not arbitrary — determined by initial conditions.

The system remembers where it started.
""",

    deep_dive="""
You’re still thinking in terms of formulas.

Stop.

Think in terms of structure.

Take three-dimensional Euclidean space.

You have basis vectors:

i, j, k

Every vector is just a combination of those.

Nothing more.

---

Now replace vectors with functions.

Functions that satisfy the differential equation.

They behave the same way.

They form a space.

A solution space.

---

Cos(ωt) and sin(ωt) are not just “solutions”.

They are basis functions.

Everything you can possibly build as a solution is just their combination.

That is why:

x(t) = a cos(ωt) + b sin(ωt)

---

If the equation is homogeneous:

The solution space is clean.

No external forcing. No distortion.

Just a finite-dimensional space spanned by basis functions.

---

If the equation were non-homogeneous:

You would need something else.

A particular solution.

Something that does not belong to the homogeneous structure.

And then:

General solution = homogeneous + particular

Always.

---

Now refine the expression.

Instead of two constants a and b, rewrite them:

a = A sin(φ)
b = A cos(φ)

Substitute:

x(t) = A sin(φ) cos(ωt) + A cos(φ) sin(ωt)

Use a trigonometric identity:

x(t) = A cos(ωt + φ)

---

Now it is compact.

But nothing was lost.

Only reorganized.

---

Now step one level deeper.

You can stop thinking in terms of sine and cosine entirely.

Represent the motion using complex numbers:

x(t) = Re{ A e^{i(ωt + φ)} }

This is not a trick.

This is compression.

---

The exponential function contains both sine and cosine at once.

Through Euler’s formula:

e^{iθ} = cos(θ) + i sin(θ)

So instead of juggling two functions, you manipulate one.

Differentiation becomes trivial.

Structure becomes visible.

---

ω is the angular frequency.

It tells you how fast the system progresses through its phase.
How quickly the angle evolves in time.

φ is the phase constant.

It encodes where the system begins.

Not just position — state.

---

You are not watching motion anymore.

You are tracking rotation in phase space.

That is what oscillation really is.
"""
)

related = ["spring_with_mass"]