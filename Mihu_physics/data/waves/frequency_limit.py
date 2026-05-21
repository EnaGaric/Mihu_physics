from Mihu_physics.core.concept import Concept

frequency_limits = Concept(

    name="Frequency Limits & Resonance",

    definition="""
Response of a forced oscillator depends strongly on the driving frequency ω.
Different frequency regimes produce fundamentally different physical behaviour.
""",

    explanation="""
In forced oscillations, the steady-state amplitude and phase are given by:

A(ω) = (F₀/m) / sqrt((ω₀² - ω²)² + (γ ω)²)

tan(δ) = (γ ω) / (ω₀² - ω²)

Where:
- ω₀ = natural frequency
- γ = damping factor
- δ = phase shift between force and response

These two expressions completely determine how the system reacts to external driving.
""",

    derivation="""
We now analyze three key frequency limits.

---

# 1. Low frequency limit (ω → 0)

The external force changes very slowly:

F(t) = F₀ cos(ωt), ω → 0

The system has enough time to adjust at every instant.

So force balance is approximately:

F₀ ≈ kx

Thus:

x ≈ F₀ / k

Since amplitude A corresponds to maximum displacement:

A = F₀ / k

Phase shift:

tan(δ) = (γ ω) / (ω₀² - ω²) → 0

So:

δ = 0

Interpretation:
- System follows the force perfectly
- Motion is in phase with driving force
- No delay in response

---

# 2. High frequency limit (ω → ∞)

The external force oscillates extremely fast.

The system cannot respond fast enough due to inertia.

So effectively:
- The mass cannot follow the forcing
- Displacement averages out

Thus:

A → 0

Phase:

tan(δ) → 0 / (-∞) → 0 but sign implies:

δ = π

Interpretation:
- System is out of phase
- Response is opposite to driving force
- Motion is strongly suppressed

---

# 3. Resonance region (ω ≈ ω₀)

Now the denominator:

(ω₀² - ω²)² + (γ ω)²

becomes minimal.

So amplitude becomes maximal.

This is resonance.

For weak damping (γ → 0):

Maximum occurs near:

ω ≈ ω₀

---

## Physical meaning of resonance

Resonance is not just frequency matching.

It is maximum energy transfer.

Power:

P = F · v

At resonance:
- Force and velocity are in phase
- Energy input is maximized every cycle
- System absorbs energy efficiently

---

## Phase behaviour at resonance

At ω ≈ ω₀:

ω₀² - ω² ≈ 0

So:

tan(δ) → ∞

Thus:

δ = π/2

Meaning:
- Force is proportional to cos(ωt)
- Velocity is proportional to sin(ωt)
- Force and velocity are in phase

This is the true resonance condition:
maximum power transfer.

---

## 4. Exact resonance shift (with damping)

Because damping removes energy, the true maximum is slightly shifted.

To find it, differentiate amplitude:

A(ω) = (F₀/m) / sqrt((ω₀² - ω²)² + (γ ω)²)

Set derivative dA/dω = 0.

Result:

ω_max = ω₀ * sqrt(1 - γ² / (2 ω₀²))

---

So:
- damping shifts resonance slightly left
- stronger damping → larger shift

---

## 5. Quality factor Q

Define:

Q = ω₀ / γ

Interpretation:
- High Q → weak damping → sharp resonance peak
- Low Q → strong damping → broad, weak resonance

---

## Final intuition

The oscillator behaves like a frequency filter:

- Low ω → follows force easily
- High ω → cannot respond
- Near ω₀ → amplifies motion

Resonance is not a coincidence.

It is the point where energy input and system response align perfectly in time.
""",
    deep_dive="""
Frequency limits are not just mathematical cases.

They are physical regimes of communication between the system and the external world.

---

## 1. What is really happening?

A forced oscillator is constantly trying to respond to an external signal:

F(t) = F₀ cos(ωt)

But it is not just “following a function”.

It is constantly negotiating between:

- inertia (resists change)
- damping (removes energy)
- driving force (injects energy)

---

So frequency ω determines the “language” of the forcing.

The system either understands it,
partially follows it,
or completely fails to respond.

---

## 2. Low frequency regime (slow forcing)

When ω → 0:

The force changes so slowly that the system behaves almost statically.

There is no lag.

No memory effect.

At every moment:

the system is basically in equilibrium.

So:

- force ≈ spring force
- motion is smooth and in-phase
- system fully tracks external change

---

This is why:

A = F₀ / k

It is not oscillation anymore in a dynamic sense.

It becomes quasi-static deformation.

---

## 3. High frequency regime (fast forcing)

When ω → ∞:

The system is overwhelmed.

The force changes faster than the system can physically react.

So:

- inertia dominates
- displacement averages out
- the mass “freezes” in place

---

Even though force is large and rapid,
the system cannot accumulate coherent motion.

So energy transfer fails.

Result:

A → 0

---

This is not resistance.

It is inability to respond.

---

## 4. Resonance regime (matching condition)

When ω ≈ ω₀:

Now something fundamentally different happens.

The external force and natural dynamics of the system align.

Not just in frequency — but in timing.

---

Each push arrives at the correct phase.

Instead of cancelling motion, it amplifies it.

So energy does NOT cancel out.

It accumulates.

Cycle after cycle.

---

This is why resonance is dangerous and powerful:
it is constructive energy accumulation over time.

---

The phase shift δ tells you something deeper than delay.

It tells you how the system “chooses” to respond:

- δ = 0 → system follows force instantly
- δ = π/2 → system stores energy maximally
- δ = π → system responds opposite to force

---

At resonance:

δ = π/2

This is the most efficient energy transfer state.

Force is not doing maximum work instantly,
but over time it injects maximum energy per cycle.

---

## 6. Why resonance peak is not exactly ω₀

Damping always exists.

And damping continuously removes energy.

So the system compensates:

It shifts its optimal response slightly away from natural frequency.

Because it is trying to balance:

input energy = lost energy

---

So resonance is not a point.

It is a compromise between driving and dissipation.

---

Forced oscillations are not about motion.

They are about information flow between:

- external driver (environment)
- internal dynamics (system response)

---

Frequency is the control knob of that interaction.

It decides whether:

- system follows smoothly
- system ignores input
- system amplifies input catastrophically

---

This is why resonance appears everywhere:

bridges, circuits, atoms, mechanical systems.

Because every physical system has:

- a natural frequency
- a way to store energy
- a way to lose energy

And when those align with external forcing —
the system stops being stable.

It becomes reactive.
"""
)