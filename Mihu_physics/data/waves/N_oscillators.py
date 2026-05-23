from Mihu_physics.core.concept import Concept

n_coupled_oscillators = Concept(

    name="System of N Coupled Oscillators",

    definition="""
A system of N masses connected through interactions so that the motion of each mass
depends on its neighbors.

Because the oscillators are coupled, the system possesses N normal modes —
N independent collective patterns of oscillation.
""",

    explanation="""
Consider N identical masses m placed along a string.

Each mass is separated by distance a.

The string is under tension T.

The masses are allowed to oscillate only vertically
(in the y-direction).

No motion in x-direction is allowed.

---

The ends of the string are fixed.

That means:

the boundary points cannot move.

So:

y₀(t) = 0
yₙ₊₁(t) = 0

These are boundary conditions.

---

The “0-th” and “(n+1)-th” masses are not real.

They are fictitious points introduced to make the equations uniform.

Without them, edge masses would require special equations.

With them, every mass obeys the same formula.

---

Each mass interacts only with nearest neighbors.

So the motion of mass r depends on:
- mass r-1
- mass r+1

Everything becomes coupled.

---

And because there are N coupled oscillators,
there must exist exactly N normal modes.

Not more.
Not less.

Each normal mode corresponds to:
- one collective pattern of motion
- one allowed frequency
""",

    derivation="""
Let’s begin carefully.

We consider N masses attached to a stretched string.

The string has:
- tension T
- spacing a between masses

The masses can move only vertically.

Call the displacement of the r-th mass:

y_r(t)

---

Now isolate one mass.

Mass r experiences two tensions:
- from the left segment
- from the right segment

Apply Newton’s second law vertically.

The vertical components of tension determine the motion.

So:

m d²y_r/dt² = -T sin(θ₁) - T sin(θ₂)

---

Now use the small-angle approximation.

For small oscillations:

sin(θ) ≈ tan(θ)

And geometrically:

sin(θ₁) = (y_r - y_(r-1))/a

sin(θ₂) = (y_r - y_(r+1))/a

---

Insert into Newton’s law:

m d²y_r/dt² = -T(y_r - y_(r-1))/a - T(y_r - y_(r+1))/a

Expand:

m d²y_r/dt² = -(T/a)[2y_r - y_(r-1) - y_(r+1)]

Divide by m:

d²y_r/dt² = -(T/ma)(2y_r - y_(r-1) - y_(r+1))

This equation is extremely important.

Everything follows from it.

---

Now assume normal mode motion.

All masses oscillate with the SAME frequency.

So propose:

y_r(t) = A_r cos(ωt)

The amplitudes A_r may differ.

But ω must be identical for all masses.

That is the definition of a normal mode.

---

Differentiate twice:

d²y_r/dt² = -A_r ω² cos(ωt)

Insert into the equation:

-A_r ω² cos(ωt) = -(T/ma)[2A_r - A_(r-1) - A_(r+1)]cos(ωt)

Cancel cos(ωt):

-A_r ω² = -(T/ma)[2A_r - A_(r-1) - A_(r+1)]

Rearrange:

-A_r ω² = (T/ma)[A_(r-1) + A_(r+1) - 2A_r]

Multiply by ma/T:

-(maω²/T)A_r = A_(r-1) + A_(r+1) - 2A_r

Move everything to one side:

-A_(r-1) - A_(r+1) + A_r(2 - maω²/T) = 0

This is the key spatial equation.

---

Now apply boundary conditions.

Because the ends are fixed:

y₀(t) = 0
yₙ₊₁(t) = 0

Therefore:

A₀ = 0
Aₙ₊₁ = 0

---

Now examine simple cases.

CASE: n = 1

Only one mass exists.

Then:

A₀ = A₂ = 0

The equation becomes:

A₁(2 - maω²/T) = 0

Nontrivial solution requires:

2 - maω²/T = 0

So:

ω² = 2T/(ma)

---

CASE: n = 2

Now we have:
- A₀ = 0
- A₃ = 0

For r = 1:

-A₂ + A₁(2 - maω²/T) = 0

For r = 2:

-A₁ + A₂(2 - maω²/T) = 0

This system gives two possible solutions.

---

FIRST MODE:

A₂/A₁ = +1

Both masses oscillate together.

Same direction.
Same phase.

---

SECOND MODE:

A₂/A₁ = -1

The masses oscillate oppositely.

Out of phase.

---

Now comes the important step.

We search for the general form of A_r.

Start from:

-A_(r-1) + (2 - maω²/T)A_r - A_(r+1) = 0

Divide by A_r:

(2 - maω²/T) = (A_(r-1) + A_(r+1))/A_r

Now define:

ω₀² = T/(ma)

Then:

(2ω₀² - ω²)/ω₀² = (A_(r-1) + A_(r+1))/A_r

Notice something crucial.

The left side is constant.

It does NOT depend on r.

Therefore:

(A_(r-1) + A_(r+1))/A_r

must also remain constant.

---

This strongly constrains the possible form of A_r.

In mathematics, equations like this naturally lead to:
- sine functions
- cosine functions
- complex exponentials

But the boundary conditions decide which survives.

Because:

A₀ = 0
Aₙ₊₁ = 0

the sine function fits perfectly.

So we propose:

A_r = C sin(rθ)

---

After substitution and verification,
the allowed values become quantized.

Finally, the complete normal mode solution emerges:

y_(r,p)(t) = C_p sin(rpπ/(n+1))cos(ω_p t)

Where:
- r labels the mass
- p labels the normal mode
- ω_p is the frequency of mode p

---

And there they are.

N normal modes.

Exactly as expected.

Because:
- N oscillators
- N degrees of freedom
- N independent collective oscillations
""",

    deep_dive="""
At first glance,
this system looks impossible.

You do not have:
- one oscillator
- one equation
- one frequency

You have an entire chain.

Every mass affects its neighbors.

Disturb one particle,
and the disturbance spreads through the entire structure.

---

This is no longer “particle physics”.

It is collective behavior.

The system behaves as a connected medium.

---

And yet something extraordinary happens.

Despite all the coupling,
despite all the complexity,
nature still organizes itself into clean patterns.

Those patterns are the normal modes.

---

Look carefully at the solution:

y_(r,p)(t) = C_p sin(rpπ/(n+1))cos(ω_p t)

The oscillation separates into:
- spatial structure
- time evolution

That separation is not accidental.

It means the system found motions where:
- every particle knows exactly how to move
- the entire chain remains self-consistent

---

The sine term determines SHAPE.

It tells you:
which particles move strongly,
which barely move,
which are nodes.

---

The cosine term determines TIME.

Every particle in the same normal mode oscillates with the same frequency ω_p.

Always.

That is the defining feature of a normal mode.

---

Now notice something deeper.

The mode number p behaves almost like a quantum number.

Different values of p produce different standing-wave patterns.

Small p:
- long wavelength
- smooth motion
- neighboring particles move similarly

Large p:
- short wavelength
- rapid alternation
- neighboring particles move oppositely

---

This is why coupled oscillators become so important.

Because this exact mathematics appears everywhere:
- crystal vibrations
- sound propagation
- molecular vibrations
- electromagnetic cavities
- quantum fields
- phonons in solids

---

The chain of oscillators is secretly the beginning of wave physics.

As N becomes enormous,
the discrete masses begin behaving like a continuous medium.

The normal modes become standing waves.

And eventually:

the entire system transforms into a field.

---

That is the deeper truth here.

You started with masses and springs.

But mathematics quietly pushed you toward wave mechanics,
Fourier analysis,
and eventually quantum theory.

---

And all of it began from one observation:

Complex coupled motion can be decomposed into independent normal modes.

Always.

That is one of the most powerful ideas in all of physics.
"""
)