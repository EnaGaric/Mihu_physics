from Mihu_physics.core.concept import Concept

coupled_oscillators = Concept(

    name="Normal Modes - Example",

    definition="""
A system of oscillators connected in such a way that the motion of one affects the others.

Because the oscillators interact, the equations of motion become coupled.
The system no longer behaves like independent oscillators, but as a collective structure
with multiple natural modes of oscillation.
""",

    explanation="""
Consider the system:

wall -- k1 -- m1 -- k_c -- m2 -- k2 -- wall

Two masses.
Three springs.
Nothing isolated anymore.

If one mass moves, the coupling spring pulls the other one.

The motion spreads through the system.

---

At first glance, the system looks chaotic.

Everything affects everything.

But normal modes reveal hidden order.

There exist special motions where:
- both masses oscillate with the SAME angular frequency
- the ratio of amplitudes stays constant
- the entire coupled system behaves like one organized structure

Those motions are the normal modes.

---

The strategy is always the same:

1. Draw the system.
2. Write Newton’s law for each mass.
3. Assume all oscillators move with the same frequency:
   
   x_i(t) = C_i cos(ωt)

4. Solve for:
   - allowed frequencies ω
   - amplitude ratios C1/C2

---

You are not solving random motion anymore.

You are searching for the special patterns
the system naturally prefers.
""",

    derivation="""
Let’s begin carefully.

Consider the system:

wall -- k1 -- m1 -- k_c -- m2 -- k2 -- wall

Two masses are connected through a coupling spring.

This means:

The motion of one mass affects the other.

The equations will become coupled.

---

Now draw all forces carefully.

For mass m1:

- left spring pulls toward equilibrium:
  
  F_left = -k1 x1

- coupling spring depends on relative displacement:

  F_couple = k_c (x2 - x1)

Why?

Because:
- if x2 > x1, the spring is stretched
- the spring tries to shrink
- so it pulls m1 toward the right

---

Apply Newton’s second law:

m d²x1/dt² = -k1 x1 + k_c(x2 - x1)

---

Now for mass m2.

Again:
- right spring restores equilibrium:

  F_right = -k2 x2

- coupling spring now acts oppositely:

  F_couple = -k_c(x2 - x1)

because if the spring pulls m1 right,
it must pull m2 left.

Newton’s law becomes:

m d²x2/dt² = -k2 x2 - k_c(x2 - x1)

---

Now divide both equations by m.

First equation:

d²x1/dt² = -(k1/m)x1 + (k_c/m)(x2 - x1)

Second equation:

d²x2/dt² = -(k2/m)x2 - (k_c/m)(x2 - x1)

---

And now comes the important step.

Normal mode assumption.

We assume both masses oscillate with the SAME frequency.

Not optional.

That is the definition of a normal mode.

So we propose:

x1(t) = C1 cos(ωt)

x2(t) = C2 cos(ωt)

Same ω.
Different amplitudes allowed.

---

Now differentiate twice.

Since:

d²/dt² [cos(ωt)] = -ω² cos(ωt)

we get:

d²x1/dt² = -C1 ω² cos(ωt)

d²x2/dt² = -C2 ω² cos(ωt)

---

Insert into the equations.

First equation:

-C1ω² cos(ωt) = -(k1/m)C1 cos(ωt) + (k_c/m)(C2 - C1)cos(ωt)

Every term contains cos(ωt).

Cancel it.

Result:

-C1ω² = -(k1/m)C1 + (k_c/m)(C2 - C1)

---

Expand:

-C1ω² = -(k1/m)C1 + (k_c/m)C2 - (k_c/m)C1

Move everything involving C1 together:

(k1/m + k_c/m - ω²)C1 = (k_c/m)C2

Now divide by C2:

(C1/C2)(k1/m + k_c/m - ω²) = k_c/m

So:

C1/C2 = (k_c/m) / (k1/m + k_c/m - ω²)

---

Now repeat for the second equation.

Insert the assumed motion:

-C2ω² = -(k2/m)C2 - (k_c/m)(C2 - C1)

Expand:

-C2ω² = -(k2/m)C2 - (k_c/m)C2 + (k_c/m)C1

Rearrange:

(k2/m + k_c/m - ω²)C2 = (k_c/m)C1

Divide by C2:

C1/C2 = (m/k_c)(k2/m + k_c/m - ω²)

---

Now comes the key step.

Both expressions describe the SAME ratio C1/C2.

So they must be equal.

Set them equal and simplify.

After algebra, the characteristic equation becomes:

m²ω⁴ - mω²(k1 + k2 + 2k_c) + (k1k2 + k1k_c + k2k_c) = 0

---

This is quadratic in ω².

So define:

z = ω²

Then:

m²z² - m(k1 + k2 + 2k_c)z + (k1k2 + k1k_c + k2k_c) = 0

Now solve using the quadratic formula.

The result:

ω²_± = (k1 + k2 + 2k_c)/(2m) ± (1/2m)sqrt(4k_c² + (k1-k2)²)

---

And there they are.

Two natural frequencies.

Two normal modes.

Exactly what we expected.

Because:
- two oscillators
- two degrees of freedom
- two independent normal modes

Not more.
Not less.

---

Now interpret them physically.

ω_- :

The slower mode.

The masses move approximately in phase:

x1 ≈ x2

The coupling spring barely stretches.

So it contributes very little restoring force.

The system behaves almost like two independent oscillators.

Frequency stays lower.

---

ω_+ :

The faster mode.

The masses move out of phase.

When one moves right,
the other moves left.

The coupling spring stretches and compresses continuously.

Extra restoring force appears.

Frequency increases.

---

And yes:

The mathematics naturally gives ω².

Because the equation itself contains:

d²x/dt² = -ω²x

Only at the end do you take:

ω = sqrt(ω²)

Positive root only.

Because angular frequency must be positive.

---

Special symmetric case:

If:

k1 = k2 = k_c = k

then:

ω²_± = 2k/m ± k/m

So:

ω²_- = k/m

ω²_+ = 3k/m

The two cleanest normal modes emerge immediately.
""",

    deep_dive="""
Look carefully at the system again.

wall -- k1 -- m1 -- k_c -- m2 -- k2 -- wall

At first it looks simple.

Two masses.
Three springs.

But the moment the coupling spring appears,
the entire structure changes.

---

m1 is no longer free to oscillate independently.

Every time m1 moves,
it stretches or compresses the coupling spring.

And the coupling spring immediately affects m2.

Then m2 reacts back on m1.

Information constantly travels through the system.

---

That is why the equations become coupled.

x1 depends on x2.
x2 depends on x1.

You no longer have two independent oscillators.

You have one interacting system.

---

And this is exactly where most people get lost.

Because they keep trying to think about:
- “mass 1 separately”
- “mass 2 separately”

But nature is no longer thinking that way.

The coupling spring erased that separation.

---

Now observe the two normal modes carefully.

First mode:

ω_-

The slow mode.

The masses move together:

x1 ≈ x2

This means the coupling spring barely changes length.

And if the coupling spring barely stretches,
then it barely exerts force.

So effectively,
the middle spring almost disappears dynamically.

---

The system behaves almost like:

two oscillators moving as one object.

That is why the frequency is smaller.

There is less restoring force.

---

Now look at the second mode.

ω_+

The fast mode.

The masses move opposite to each other.

When m1 moves right,
m2 moves left.

Now the coupling spring stretches maximally.

And a stretched spring means:
more restoring force.

The middle spring participates strongly now.

It constantly pulls both masses back.

---

So the system becomes effectively “stiffer”.

More restoring force → higher frequency.

That is why:

ω_+ > ω_-

Always.

---

Now think about what the mathematics actually discovered.

You started with messy coupled equations.

Everything depended on everything.

But after imposing the normal mode condition:

x1(t) = C1 cos(ωt)
x2(t) = C2 cos(ωt)

the chaos collapsed into algebra.

---

That is the important part.

Normal modes are not random guesses.

They are the specific motions where the entire coupled system becomes self-consistent.

The system “agrees” to oscillate in one organized pattern.

---

And the amplitude ratio:

C1/C2

tells you exactly what that pattern looks like.

Positive ratio:
- masses move together
- in phase

Negative ratio:
- masses move oppositely
- out of phase

---

So the frequencies alone are not enough.

The true normal mode is:

frequency + shape of motion

Both matter.

---

And now the deepest observation.

You never truly solved for x1 and x2 independently.

You solved for collective motion.

The system stopped being:
- “mass 1”
- “mass 2”

and became:

a single dynamical structure
with two allowed patterns of oscillation.

That is what a normal mode actually is.
"""
)