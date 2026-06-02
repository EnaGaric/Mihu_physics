from Mihu_physics.core.concept import Concept

dispersion_effect = Concept(

    name="Dispersion Effect",

    definition="""
Dispersion is the effect in which the propagation speed of a wave depends on its angular frequency ω.

If different frequencies travel with different speeds, the medium is called dispersive.

If all frequencies travel with the same speed, the medium is non-dispersive.
""",

    explanation="""
Imagine sending several waves through a medium.

One low frequency wave.
One medium frequency wave.
One high frequency wave.

The key question is:

Do they travel at the same speed?

---

In a non-dispersive medium, the answer is yes.

All waves propagate with the same velocity.

v is constant and does NOT depend on frequency.

v = constant

Examples:
- ideal stretched string (approximation)
- shallow water waves
- sound in air (approximation)

---

In such a medium:

- wave packets keep their shape
- all harmonics arrive together
- no spreading occurs

The system behaves as if all frequencies are “locked” to the same speed.

---

In a dispersive medium, the situation changes.

Wave velocity depends on frequency:

v = v(ω)   or   v = v(k)

Different frequency components travel at different speeds.

---

As a result:

- higher harmonics may move faster or slower than lower ones
- the wave packet begins to deform
- the signal spreads in space over time

The original shape is not preserved.
""",

    derivation="""
To understand why dispersion matters, consider the superposition of two similar waves.

Let:

y₁ = A sin(k₁x - ω₁t)
y₂ = A sin(k₂x - ω₂t)

Assume the waves are close:

k₁ ≈ k₂ ≈ k
ω₁ ≈ ω₂ ≈ ω

---

Adding them:

y = y₁ + y₂

Using trigonometric identities:

y = 2A sin(kx - ωt) cos(Δkx/2 - Δωt/2)

---

Now we clearly see two structures:

1) Fast oscillation:
sin(kx - ωt)

This represents the carrier wave.

2) Slow modulation:
cos(Δkx/2 - Δωt/2)

This represents the envelope.

---

The envelope is crucial.

It carries:
- energy
- information
- signal structure

---

The velocity of this envelope defines the group velocity:

v_g = dω/dk

---

The carrier oscillates at phase velocity:

v = ω/k

---

If v depends on k or ω, then different components separate in time.

This leads to deformation of the wave packet.
""",

    deep_dive="""
Everything in wave physics can be understood through a single object:

the dispersion relation ω = ω(k)

---

If ω(k) is linear:

ω = vk

Then:

v_g = dω/dk = v

Phase velocity = group velocity

The medium is non-dispersive.

Wave packets keep their shape perfectly.

---

If ω(k) is nonlinear:

then different k-values produce different velocities.

The wave packet spreads.

---

We can model dispersion using:

ω² = v²k² + αk⁴

---

Case α = 0:

ω = vk

→ non-dispersive medium

---

Case α > 0 or α < 0:

ω(k) becomes nonlinear

→ dispersive medium

---

Two regimes appear:

1) Normal dispersion:
v_g < phase velocity
Wave packet moves slower than individual waves.

2) Anomalous dispersion:
v_g > phase velocity
Wave packet moves faster than individual wave components.

---

Physically:

- phase velocity describes motion of individual crests
- group velocity describes motion of energy and information

---

In dispersive systems:

The shape of the wave is not preserved.

The packet continuously reshapes while propagating.

This is not a small effect.

It is a fundamental property of the medium itself.
"""
)