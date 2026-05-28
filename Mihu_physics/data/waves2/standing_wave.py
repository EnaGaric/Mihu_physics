from Mihu_physics.core.concept import Concept

standing_waves = Concept(

    name="Standing Waves on a Fixed String",

    definition="""
A standing wave is a wave pattern that appears stationary in space.

It is formed by the superposition of two waves of equal amplitude and frequency
traveling in opposite directions.

Energy does not propagate along the medium in a net direction; instead, the pattern oscillates in place.
""",

    explanation="""
Consider a string fixed at both ends (x = 0 and x = L).

When the string is excited, a wave travels along it.

However, when it reaches a fixed boundary, it reflects:
- the wave inverts phase by π at a fixed end
- reflection preserves amplitude (ideal case)

Because of continuous reflections, the string contains:
- a wave traveling to the right
- a wave traveling to the left

These two waves continuously overlap and interfere.
""",

    derivation="""
STEP 1: TWO TRAVELLING WAVES

We describe the system as a superposition of two waves:

y₁(x,t) = A sin(kx - ωt)
y₂(x,t) = A sin(kx + ωt)

Right-moving wave: y₁
Left-moving wave: y₂ (due to reflections)

---

STEP 2: SUPERPOSITION PRINCIPLE

Total displacement:

y(x,t) = y₁ + y₂

So:

y(x,t) = A sin(kx - ωt) + A sin(kx + ωt)

Factor A:

y(x,t) = A[sin(kx - ωt) + sin(kx + ωt)]

---

STEP 3: TRIGONOMETRIC IDENTITY

Use identity:

sin(a - b) + sin(a + b) = 2 sin(a) cos(b)

Let:
a = kx
b = ωt

Then:

y(x,t) = 2A sin(kx) cos(ωt)

---

STEP 4: SEPARATION OF VARIABLES

We obtain:

y(x,t) = (2A sin(kx)) · (cos(ωt))

This is crucial:

- spatial part: sin(kx)
- temporal part: cos(ωt)

The shape is fixed in space
Only time oscillation remains

This is why it is called a "standing" wave.
""",

    deep_dive="""
STEP 1: NODES AND ANTI-NODES

From:

y(x,t) = 2A sin(kx) cos(ωt)

If sin(kx) = 0:

→ y(x,t) = 0 for all t

These points never move → NODES

Condition:

sin(kx) = 0 → kx = nπ

So nodes are fixed positions in space.

---

If |sin(kx)| = 1:

→ amplitude is maximum

These are ANTI-NODES

They oscillate with maximum amplitude.

---

STEP 2: BOUNDARY CONDITIONS

String is fixed:

y(0,t) = 0
y(L,t) = 0 for all t

Check x = 0:

y(0,t) = 2A sin(0) cos(ωt) = 0 ✔

Check x = L:

y(L,t) = 2A sin(kL) cos(ωt)

For this to be always zero:

sin(kL) = 0

---

STEP 3: QUANTIZATION OF WAVE NUMBER

sin(kL) = 0 → kL = nπ

So:

kₙ = nπ / L

Only discrete values are allowed.

This is the key result:
NOT all waves are allowed on a fixed string.

Only specific "modes" survive.

---

STEP 4: WAVELENGTH

We know:

k = 2π / λ

So:

2π / λₙ = nπ / L

Solve:

λₙ = 2L / n

---

STEP 5: FREQUENCY

Wave relation:

ω = v k

So:

ωₙ = v (nπ / L)

Frequency:

fₙ = ωₙ / (2π)

fₙ = (n v) / (2L)

---

STEP 6: NORMAL MODES INTERPRETATION

Each integer n corresponds to a normal mode.

n = 1 → fundamental mode (first harmonic)
n = 2 → second harmonic
n = 3 → third harmonic
...

Each mode has:
- fixed spatial shape sin(nπx/L)
- fixed frequency ωₙ

---

STEP 7: WHY DISCRETE MODES EXIST

The boundary conditions force the system to "fit" waves inside the string.

Only waves that form perfect standing patterns survive.

Everything else cancels out over time.

This is why the system behaves like it has quantized allowed states.

---

FINAL RESULT:

yₙ(x,t) = Aₙ sin(nπx/L) cos(ωₙ t)

with:

kₙ = nπ/L
ωₙ = nπv/L
fₙ = n v / (2L)
"""
)