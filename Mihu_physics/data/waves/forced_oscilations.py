from Mihu_physics.core.concept import Concept

forced_oscillations = Concept(

    name="Forced Oscillations",

    definition="""
Oscillatory motion under the influence of an external periodic driving force.
Unlike free oscillations, the system is continuously driven by an outside source of energy.
""",

    explanation="""
Forced oscillations occur when a system is not left to evolve on its own.

Instead, an external force keeps acting on it:

F(t) = F₀ cos(ωt)

This force is oscillatory in nature — it is not constant, not impulsive, but periodic.
Its role is crucial: it compensates for energy lost due to damping and friction.

Without it, the system would eventually die out.
""",

    derivation="""
Start from Newton’s second law:

m d²x/dt² = -k x - b dx/dt + F₀ cos(ωt)

Divide through by m:

d²x/dt² + γ dx/dt + ω₀² x = (F₀/m) cos(ωt)

Where:
γ = b/m
ω₀² = k/m

---

This is a NON-homogeneous linear differential equation of second order.

General structure:

x(t) = x_h(t) + x_p(t)

- x_h(t): homogeneous solution (free damped oscillations)
- x_p(t): particular solution (driven response)

---

# 1. Homogeneous part

Solve:

d²x/dt² + γ dx/dt + ω₀² x = 0

Try:

x = e^{λt}

λ² + γλ + ω₀² = 0

Solve quadratic:

λ = -γ/2 ± sqrt(γ²/4 - ω₀²)

For underdamped case (γ² < 4ω₀²):

λ = -γ/2 ± iω

where:

ω = sqrt(ω₀² - γ²/4)

So:

x_h(t) = e^{-γt/2}(C₁ e^{iωt} + C₂ e^{-iωt})

---

Rewrite using Euler form:

x_h(t) = e^{-γt/2}(C cos(ωt) + D sin(ωt))

---

As t → ∞:

e^{-γt/2} → 0

So:

x_h(t) → 0

The system forgets its initial conditions.

Energy is continuously lost to damping.

---

# 2. Why oscillation still survives?

Because of the external force.

It continuously injects energy into the system.

So even though free motion dies out,
the system does NOT stop moving.

It transitions to steady-state motion.

---

# 3. Particular solution

We assume:

x_p(t) = A cos(ωt) + B sin(ωt)

Or more elegantly in complex form:

x_p(t) = Re{ X e^{iωt} }

Substitute into equation and solve for amplitude:

---

Final steady-state solution:

x_p(t) = (F₀/m) / sqrt((ω₀² - ω²)² + γ² ω²)

---

Phase shift:

tan(δ) = (γ ω) / (ω₀² - ω²)

So final physical solution:

x(t) = X cos(ωt - δ)

---

# 4. Physical interpretation

- Homogeneous part → dies out (energy loss)
- Particular part → survives forever (driven by external force)
- System forgets initial conditions
- Motion locks to driving frequency ω

---

# 5. Key idea

The oscillator is no longer “free”.

It becomes enslaved to the driving force.

It oscillates not because of its own energy,
but because energy is continuously supplied from outside.
""",
    deep_dive="""
You are no longer looking at a simple oscillator.

You are looking at a system in conflict.

---

In free oscillations, the system is alone.
It evolves based on its own stored energy.

In damped oscillations, the system is slowly dying.
Energy leaks out. Nothing replaces it.

But in forced oscillations, something fundamentally changes.

There is now a constant external “hand” pushing the system.

---

So the motion becomes a balance of three things:

1) Inertia (mass resists change)
2) Damping (energy loss to environment)
3) External driving force (energy input)

---

This is not equilibrium in the usual sense.

It is dynamic equilibrium.

Energy in = energy out

Not zero motion — but sustained motion.

---

Now split the solution:

x(t) = x_h(t) + x_p(t)

---

## 1. Homogeneous part (transient response)

This is the system remembering its past.

It behaves exactly like damped oscillations:

x_h(t) = e^{-γt/2}(C₁ cos(ωt) + C₂ sin(ωt))

But there is a key fact:

As time increases:

e^{-γt/2} → 0

So:

x_h(t) → 0

---

This means:

The system forgets its initial conditions.

It does not matter how you started it.

It does not matter how you pushed it initially.

Everything fades.

---

## 2. Particular part (steady-state response)

This is the only motion that survives forever.

Why?

Because it is continuously driven.

The system stops “deciding” its motion.

It starts “following” the force.

---

So after long time:

x(t) ≈ x_p(t)

---

## 3. Phase shift intuition

The system is NOT in phase with the driving force.

It cannot respond instantly.

Because of inertia and damping, it lags behind.

That lag is:

δ

So:

x(t) = X cos(ωt - δ)

---

Meaning:

- The force pushes first
- The system reacts slightly later
- That delay depends on damping and frequency

---

## 4. Amplitude behaviour (the most important insight)

The amplitude is NOT constant in a trivial way.

It depends on how “compatible” the driving frequency is with the natural frequency.

X = (F₀/m) / sqrt((ω₀² - ω²)² + γ² ω²)

---

This expression hides everything:

- If ω ≈ ω₀ → denominator becomes small → amplitude grows
- If damping is small → response becomes huge
- If damping is large → system is suppressed

---

## 5. Resonance (hidden idea)

If damping is very small:

γ → 0

Then:

X becomes very large when ω ≈ ω₀

This is resonance.

The system stops resisting motion efficiently
and instead amplifies the driving force.

---

## 6. Final intuition

Forced oscillations are not about the system anymore.

They are about matching.

The external force defines reality,
and the system tries — imperfectly — to follow it.

At long times:

- Initial conditions disappear
- Natural motion disappears
- Only forced motion remains

The system “forgets itself”
and becomes a responder to the environment.
"""
)