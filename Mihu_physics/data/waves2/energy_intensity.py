from Mihu_physics.core.concept import Concept

sound_energy_and_intensity = Concept(

    name="Energy & Intensity of Sound Waves",

    definition="""
A sound wave carries energy through a medium without transporting matter.
This energy is stored in the oscillatory motion of particles and can be quantified through kinetic energy and energy flux (intensity).
""",

    explanation="""
We start with a longitudinal sound wave:

ni(x,t) = ni_max sin(kx - ωt)

This describes the displacement of particles in a medium (like air).

The key idea:
Sound is not the movement of matter from A to B.
It is the transmission of energy through oscillations of particles around equilibrium.

To understand energy transport, we look at particle velocity.

Velocity is the time derivative of displacement:

v(x,t) = ∂ni/∂t
       = -ω ni_max cos(kx - ωt)

So particles oscillate back and forth with angular frequency ω.

Now we consider a small slice of air:
- thickness: dx
- cross-sectional area: 1
- volume: dV = dx
- mass: dm = ρ₀ dx

This allows us to compute kinetic energy locally.
""",

    derivation="""
Kinetic energy of a small element:

dE_kin = 1/2 dm v^2

Substitute dm = ρ₀ dx and v:

dE_kin = 1/2 ρ₀ dx (ω^2 ni_max^2 cos^2(kx - ωt))

So:

dE_kin = 1/2 ρ₀ ω^2 ni_max^2 cos^2(kx - ωt) dx


Now we want energy in one wavelength λ:

E_kin = ∫₀^λ dE_kin

E_kin = 1/2 ρ₀ ω^2 ni_max^2 ∫₀^λ cos^2(kx - ωt) dx


We use a standard result:

∫ cos^2(...) dx over one period = λ/2

So:

E_kin = 1/2 ρ₀ ω^2 ni_max^2 (λ/2)

E_kin = (1/4) ρ₀ ω^2 ni_max^2 λ


Now substitute wave relations:

ω = 2πv / λ
ρ₀ v^2 = Bₐ  (bulk modulus)


So:

ω^2 = (2πv/λ)^2 = 4π^2 v^2 / λ^2

Substitute into energy:

E_kin = (1/4) ρ₀ (4π^2 v^2 / λ^2) ni_max^2 λ

Simplify:

E_kin = (π^2 ρ₀ v^2 ni_max^2) / λ

Replace ρ₀ v^2 = Bₐ:

E_kin = (π^2 Bₐ ni_max^2) / λ


This shows:
Sound energy depends on:
- stiffness of medium (Bₐ)
- amplitude squared (ni_max^2)
- inversely on wavelength (λ)
""",

    deep_dive="""
Now we interpret what this result actually means.

First key insight:
Energy in a sound wave is not uniform motion of air.
It is stored in oscillations.

Each particle is doing SHM:
- kinetic energy from velocity
- potential energy from compression

They continuously exchange energy.

But over a full wavelength, the average energy transport is stable.

---

Second insight:
Why does amplitude matter as ni_max^2?

Because doubling displacement does not just double energy.
It increases velocity AND compression effects.

So energy scales quadratically:
→ louder sound = exponentially more energetic system

---

Third insight:
Why does wavelength appear in denominator?

Shorter wavelength means:
- more oscillations per unit space
- more “packed” energy distribution

So high frequency sound carries energy more densely.

---

Fourth insight:
The medium matters.

We see:

Bₐ = bulk modulus

So:
- stiffer medium → faster energy transfer
- air vs water vs solid → completely different acoustics

This is why sound travels:
fastest in solids,
slowest in gases.

---

Fifth insight — INTENSITY:

Energy alone is not what we usually measure in practice.
We care about how fast energy is being transported.

That is intensity.

Intensity is defined as:

I = P / A

Where:
- I = intensity
- P = power (energy per unit time)
- A = area

For a plane wave, intensity can also be written as:

I = (1/2) ρ₀ v ω^2 ni_max^2

This is one of the most important results in acoustics.

---

What this means physically:

- intensity ∝ amplitude²
- intensity ∝ frequency²
- intensity ∝ medium density
- intensity ∝ wave speed

So a small increase in amplitude produces a huge increase in perceived loudness.

---

Finally — decibel scale:

Human hearing is logarithmic, not linear.

So we define:

L = 10 log10(I / I₀)

Where:
- I₀ = 10⁻¹² W/m² (threshold of hearing)

Unit:
- bel (B)
- decibel (dB) = 10⁻¹ bel

This is why:
- 10× intensity increase = +10 dB
- 100× intensity increase = +20 dB

Sound perception is therefore nonlinear.

---

Final idea:

A sound wave has energy.
But what we actually experience is intensity distribution through space and time.

What travels is not just energy.

What travels is how fast that energy is delivered.
"""
)