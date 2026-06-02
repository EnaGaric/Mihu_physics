from Mihu_physics.core.concept import Concept

doppler_effect = Concept(

    name="Doppler Effect",

    definition="""
The Doppler effect describes the change in observed frequency of a wave when there is relative motion between the source and the observer.
The wave itself does not change — only the spacing of wavefronts relative to the detector changes.
""",

    explanation="""
Start with the simplest case:

Source and observer are both at rest.

In time t, the wave travels a distance:

d = v t

where v is the speed of sound.

Each wavelength occupies a distance λ, so the number of wave cycles emitted is:

N = d / λ = vt / λ

Frequency is:

f = N / t = (vt / λ) / t = v / λ

So for a stationary system:

f = v / λ

Now we introduce motion of the detector.

If the detector moves with velocity v_d toward the source, it effectively “meets” more wavefronts per unit time.

If it moves away, it meets fewer.

So the relative wave speed becomes:

v ± v_d
""",

    derivation="""
Case 1: moving detector

In time t, detector sweeps through:

d' = (v ± v_d)t

Number of wavelengths detected:

N' = d' / λ = (v ± v_d)t / λ

So observed frequency:

f' = N'/t = (v ± v_d) / λ

Using f = v/λ:

f' = f (v ± v_d)/v


Case 2: moving source

Now the source changes wavelength spacing.

If the source moves with velocity v_s, wavefronts are either compressed or stretched.

Effective wavelength becomes:

λ' = (v ± v_s) / f

So observed frequency:

f' = v / λ' = v / ((v ± v_s)/f)

Simplify:

f' = f * v / (v ± v_s)


General Doppler formula:

f' = f * (v ± v_d) / (v ∓ v_s)

(Signs depend on direction: approach increases frequency, separation decreases it.)
""",

    deep_dive="""
Now we interpret what is actually happening.

The wave itself does NOT change speed in the medium.

What changes is:
- spacing between wavefronts
- how often the observer encounters them

So Doppler effect is NOT a change of wave physics.
It is a change of geometry in spacetime of wave emission.

---

Radar example:

Radar emits frequency f₀.

Car reflects the wave back.

Two Doppler shifts occur:
1. wave hits moving car
2. reflected wave returns to radar

So total shift doubles:

Δf = f' - f₀ = (2 v_d / v) f₀

This is why radar is extremely sensitive to velocity.

---

Extreme case:

If source speed approaches wave speed:

v_s → v

Then:

λ' → 0
f' → ∞ (mathematically)

But physically this breaks down.

Why?

Because wavefronts cannot stay ahead of the source anymore.

The source starts overtaking its own waves.

This leads to:

- shock waves
- nonlinear compression
- Mach cones

---

Mach number:

M = v_s / v

Interpretation:
- M < 1 → normal wave propagation
- M = 1 → sonic barrier
- M > 1 → supersonic regime

In supersonic motion, wavefronts pile up and form a shock wave envelope.

This is the physical reason behind the “sonic boom”.
"""
)