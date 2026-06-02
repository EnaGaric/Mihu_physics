from Mihu_physics.core.concept import Concept

fourier_analysis = Concept(

    name="Fourier Analysis of a Vibrating String",

    definition="""
Fourier analysis is the idea that any complicated vibration can be written as a sum of simple harmonic vibrations.

Instead of studying a complicated shape directly, we decompose it into normal modes.

For a string fixed at both ends, those normal modes are standing-wave harmonics.
""",

    explanation="""
Suppose we have a string fixed at:

x = 0
x = L

At time t = 0 we pull the entire string upward so that:

y(x,0) = a

for every point on the string.

At first glance this looks like a completely different shape from the standing waves we studied before.

The question is:

How do we determine which harmonics are hidden inside this shape?

---

This is exactly what Fourier analysis does.

The central idea is:

Any complicated motion = many simple harmonic motions added together.

Or look at it this way:

A complicated vibration is just a pile of simple harmonics stacked together.

Efficient, isn't it?

---

Think about Lego bricks.

Each harmonic is one Lego brick.

By combining many bricks, you can build an extremely complicated structure.

The same thing happens with waves.

A complicated string shape is built from many sinusoidal harmonics.

---

Why sinusoids?

Because we already know that the normal modes of a string fixed at both ends are:

sin(nπx/L)

These are the natural motions of the system.

Nature already chose the basis for us.

---

Suppose the initial shape is described by:

f(x)

We want to know:

How much of harmonic 1 is present?
How much of harmonic 2 is present?
How much of harmonic 3 is present?

That is the entire goal of Fourier analysis.

---

The general motion of a string can therefore be written as:

y(x,t) = Σ Bₙ sin(kₙx) cos(ωₙt)

where:

sin(kₙx)
describes the spatial shape of the nth harmonic

cos(ωₙt)
describes the time oscillation

Bₙ
tells us how strongly that harmonic participates

If:

B₃ = 0

then the third harmonic is absent.

If:

B₁ >> B₃

then the first harmonic dominates the motion.

---

So the entire problem reduces to finding:

B₁, B₂, B₃, ...

the amplitudes of the harmonics hidden inside the initial shape.
""",

    derivation="""
Before applying Fourier analysis we need a periodic function.

Why?

Because Fourier series works on periodic functions.

---

Suppose our string shape is:

f(x) = a       for 0 < x < L

To make it periodic we extend it so that:

f(x) = a       for 0 < x < L

f(x) = -a      for L < x < 2L

and then repeat this pattern forever.

The function now has period:

2L

---

Fourier theory is usually written using an angle variable with period:

2π

So we rescale the coordinate:

x → πx/L

This converts the interval into the standard Fourier interval.

---

The Fourier theorem states:

f(x) = A₀/2 + Σ Aₘ cos(mx) + Σ Bₘ sin(mx)

where:

A₀/2
is the average value

cos(mx)
represents the even part

sin(mx)
represents the odd part

---

Now look at the physical string.

The boundary conditions are:

y(0,t)=0

y(L,t)=0

---

The sine functions automatically satisfy:

sin(0)=0

sin(nπ)=0

for every integer n.

Perfect.

---

Cosines do not satisfy the boundary conditions.

For example:

cos(0)=1

which is not allowed.

Therefore the physical string can only contain sine modes.

The cosine terms disappear.

---

The constant term also disappears.

Why?

Because a constant shift would look like:

y(x)=3

But then:

y(0)=3

y(L)=3

which violates the fixed ends.

So:

A₀ = 0

---

The Fourier series becomes:

f(x) = Σ Bₘ sin(mπx/L)

or explicitly:

f(x) = B₁ sin(πx/L) + B₂ sin(2πx/L) + B₃ sin(3πx/L) + ...

---

Now comes the important question:

How do we find one specific coefficient?

How do we isolate B₃ for example?

---

Start with:

f(x) = Σ Bₘ sin(mπx/L)

Multiply both sides by:

sin(nπx/L)

and integrate from 0 to L

This gives:

∫f(x)sin(nπx/L)dx = Σ Bₘ ∫sin(mπx/L)sin(nπx/L)dx

---

Here something beautiful happens.

The sine functions behave like vectors.

Different harmonics are orthogonal.

---

What does orthogonal mean?

In ordinary vectors:

(1,0)·(0,1)=0

The vectors are perpendicular.

For functions the scalar product becomes:

<f,g> = ∫f(x)g(x)dx

So orthogonality means:

∫sin(mπx/L)sin(nπx/L)dx = 0

when:

m ≠ n

---

Therefore every harmonic disappears except the one we are looking for.

Only the term:

m=n

survives.

---

The remaining integral is:

∫₀ᴸ sin²(nπx/L) dx

This is a standard integral.

Its value is:

L/2

Therefore:

∫₀ᴸ f(x)sin(nπx/L)dx = Bₙ (L/2)

Finally:

Bₙ = (2/L)∫₀ᴸ f(x)sin(nπx/L)dx

This is the Fourier coefficient formula.

It tells us exactly how much of the nth harmonic is hidden inside the original shape.

Not more, not less.
""",

    deep_dive="""
Many students think Fourier analysis is a mathematical trick.

It is not.

It is actually a statement about physics.

---

A string fixed at both ends has infinitely many normal modes.

Nature allows:

n = 1

n = 2

n = 3

...

without limit.

Each one is a perfectly valid standing wave.

---

When you pluck a string, you almost never excite a single normal mode.

Instead you accidentally excite many of them at once.

The string does not ask for your permission.

It automatically decomposes your initial shape into the normal modes available to it.

---

Fourier analysis is simply the mathematical machinery that tells us:

How much of each normal mode was excited?

---

The coefficients Bₙ are therefore not random numbers.

They are the fingerprints of the initial condition.

They contain all information about the shape you created.

---

This is why Fourier analysis appears everywhere:

- vibrating strings
- sound waves
- quantum mechanics
- optics
- electrical signals
- image processing

The underlying idea is always identical:

Complicated pattern = sum of simple patterns

---

The deepest idea is this:

Normal modes are the alphabet of the system.

A complicated vibration is just a sentence written using that alphabet.

Fourier analysis is the process of reading the sentence and determining how many times each letter appears.
"""
)