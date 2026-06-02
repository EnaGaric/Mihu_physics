from Mihu_physics.core.concept import Concept

sound_waves = Concept(

    name="Sound Waves",

    definition="""
A sound wave is a longitudinal mechanical wave.

The particles of the medium oscillate parallel to the direction in which
the disturbance propagates.

Examples:
- sound in air
- compression waves in a spring
- pressure waves in fluids

Unlike transverse waves, the motion of particles occurs in the same direction
as the wave propagation.
""",

    explanation="""
Imagine a loudspeaker.

The membrane moves forward.

Nearby air becomes compressed.

A region of higher pressure appears.

Then the membrane moves backward.

The air expands.

A region of lower pressure appears.

The result is a sequence of compressions and rarefactions travelling through space.

---

Nothing actually travels from the speaker to your ear.

Individual air molecules only oscillate around equilibrium.

What propagates is the pressure disturbance.

That disturbance carries energy.

That disturbance is the sound wave.

---

To describe sound mathematically we introduce:

P = P₀ + p

where:

P₀ = equilibrium pressure

p = small pressure variation produced by the sound wave

Similarly:

ρ = ρ₀ + ρ_d

where:

ρ₀ = equilibrium density

ρ_d = density perturbation

And:

V = V₀ + v

where:

V₀ = equilibrium volume

v = small volume change

---

Two important quantities appear.

Dilatation:

S = v/V₀

which measures relative volume change.

Condensation:

δ = ρ_d/ρ₀

which measures relative density change.

---

Mass must be conserved.

Before the sound wave:

m = ρ₀V₀

After the sound wave:

m = ρV

Therefore:

ρ₀V₀ = (ρ₀ + ρ_d)(V₀ + v)

Dividing by ρ₀V₀ gives:

1 = (1 + δ)(1 + S)

Expanding:

1 = 1 + δ + S + δS

For ordinary sound waves:

δ << 1
S << 1

Therefore:

δS ≈ 0

and:

δ + S = 0

so:

δ = -S

This means:

if the medium expands, density decreases.

if density increases, volume decreases.

Exactly what we expect physically.
""",

    derivation="""
We now derive the wave equation for sound.

---

Imagine a chain of masses connected by springs.

Each mass interacts only with its nearest neighbours.

The displacement of the r-th particle is:

y_r(t)

The forces are:

F_right = k(y_(r+1) - y_r)

F_left = k(y_(r-1) - y_r)

Adding them:

F = k(y_(r+1) + y_(r-1) - 2y_r)

Applying Newton's law:

m d²y_r/dt² = k(y_(r+1) + y_(r-1) - 2y_r)

---

For a stretched string:

d²y_r/dt² = (T/ma)(y_(r+1) + y_(r-1) - 2y_r)

This is the discrete wave equation.

Every particle feels its neighbours.

That interaction causes disturbances to propagate.

That is the origin of waves.

---

Now let:

a = L/N

As:

N → ∞

we obtain:

a → 0

The particles become infinitely closely packed.

The discrete system becomes continuous.

---

Instead of numbering particles:

r = 1,2,3,...

we introduce:

x = ra

and write:

y_r → y(x,t)

Then:

y_(r+1) = y(x+a,t)

y_(r-1) = y(x-a,t)

and:

d²y_r/dt² → ∂²y/∂t²

The equation becomes:

∂²y/∂t² = (T/ma)[y(x+a,t)+y(x-a,t)-2y(x,t)]

---

Now perform a Taylor expansion.

For y(x+a,t):

y(x+a,t) = y + a∂y/∂x + (a²/2)∂²y/∂x² + ...

Similarly:

y(x-a,t) = y - a∂y/∂x + (a²/2)∂²y/∂x² + ...

Adding:

y(x+a,t)+y(x-a,t)-2y = a² ∂²y/∂x²

Substituting:

∂²y/∂t² = (Ta²/ma) ∂²y/∂x²

which simplifies to:

∂²y/∂t² = (Ta/m) ∂²y/∂x²

Introduce:

μ = m/a

(linear mass density)

Then:

Ta/m = T/μ

Therefore:

∂²y/∂t² = (T/μ) ∂²y/∂x²

Define:

v² = T/μ

and obtain:

∂²y/∂t² = v² ∂²y/∂x²

This is the wave equation.

---

For sound waves we perform an analogous derivation.

Let ξ(x,t) be the displacement of an air particle.

A particle originally located at x moves to:

x + ξ(x,t)

For a neighbouring particle:

ξ(x+Δx,t)

Taylor expansion gives:

Δξ = (∂ξ/∂x)Δx

The dilatation becomes:

S = Δξ/Δx

Therefore:

S = ∂ξ/∂x

---

Using the bulk modulus:

B = -V(dP/dV)

and:

S = ΔV/V

one obtains:

P = -BS

Thus:

P = -B(∂ξ/∂x)

Differentiating:

∂P/∂x = -B ∂²ξ/∂x²

---

Consider a small air element.

Newton's law gives:

ρ₀∂²ξ/∂t² = -∂P/∂x

Substituting:

ρ₀∂²ξ/∂t² = B∂²ξ/∂x²

or:

∂²ξ/∂x² = (ρ₀/B) ∂²ξ/∂t²

Comparing with the standard wave equation:

v² = B/ρ₀

Thus:

v = √(B/ρ₀)

For an adiabatic gas:

B = γP

Therefore:

v = √(γP/ρ₀)

This is the speed of sound.

A solution is:

ξ(x,t)
=
ξ_max sin(kx - ωt)
""",

    deep_dive="""
The most important question is:

Why do we use adiabatic compression instead of isothermal compression?

---

Because sound is fast.

Very fast.

A compression region travels through air before significant heat exchange
with the environment can occur.

The gas simply does not have enough time.

---

The first law of thermodynamics is:

ΔU = Q - W

For an adiabatic process:

Q = 0

Therefore:

ΔU = -W

All energy remains inside the gas.

No energy leaks away through heat transfer.

---

This means sound energy remains stored in compression and expansion
of the medium.

That is why the adiabatic bulk modulus is the physically correct one.

---

Another important observation:

Sound is not a wave of matter.

It is a wave of information.

Individual air molecules travel only microscopic distances.

Yet a disturbance can travel hundreds of metres.

---

The molecules act like messengers.

Each molecule pushes its neighbour.

That neighbour pushes the next one.

And so the disturbance propagates.

---

The final wave equation looks identical to every other wave equation in physics:

∂²ξ/∂t² = v² ∂²ξ/∂x²

The details of the medium disappear.

Only the wave speed remains.

For strings:

v = √(T/μ)

For sound:

v = √(B/ρ₀)

Different physics.

Same mathematical structure.

That is one of the deepest ideas in wave theory.
"""
)