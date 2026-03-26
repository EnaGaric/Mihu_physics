oscilations = {
    "oscilation" : {
        "definition" : "Motion around an equilibrium position that repeats in time.",
        "mihu" : "The system does not remain displaced. It returns. Again. And again.",
        "intuitive" : "A motion that keeps coming back to the same state after equal time intervals.",
        "deep_explanation" : """
Oscillation is a type of periodic motion in which a system moves around an equilibrium position.
After each period of time, the system returns to the same position and state of motion.

This motion can occur along a line, a circle, or more complex paths, depending on the system.
The defining feature is repetition in both position and dynamical state.
"""
    },

    "period" : {
        "definition" : "Time required for one complete oscillation.",
        "formula" : "T",
        "mihu" : "You are not measuring motion. You are measuring how long it takes to repeat itself.",
        "intuitive" : "Time for one full cycle.",
        "deep_explanation" : """
The period represents the time interval between two identical states of motion.
This includes both position and velocity.

It is a fundamental property of periodic systems and determines how frequently
the motion repeats.
"""
    },
    "frequency" : {
        "definition" : "Number of oscillations per unit time.",
        "formula" : "f = 1/T",
        "mihu" : "If period tells you how long it takes… frequency tells you how often it happens.",
        "intuitive" : "How many oscillations happen in one second.",
        "deep_explanation": """
Frequency is the inverse of the period and describes how many complete oscillations
occur in a given time interval.

It is commonly measured in Hertz (Hz), where 1 Hz corresponds to one oscillation per second.
"""
    },
    "angular_frequency" : {
        "definition" : "Rate of change of phase angle.",
        "formula" : "ω = 2πf",
        "mihu" : "You are not counting cycles anymore. You are tracking how fast the phase evolves.",
        "intuitive" : "How fast the oscillation progresses in terms of angle.",
        "deep_explanation": """
Angular frequency provides a more natural description of oscillatory motion
in systems described by trigonometric functions.

It connects linear frequency with rotational or phase-based descriptions.
"""
    },
    "elongation" : {
        "definition" : "Displacement from equilibrium position at a given time.",
        "formula": "x(t)",
        "mihu" : "At any moment, this is how far you've deviated from balance.",
        "intuitive" : "Current position relative to equilibrium.",
        "deep_explanation": """
Elongation represents the instantaneous displacement of the system from equilibrium.

It changes continuously in time and defines the state of the system at any given moment.
"""
    },
    "amplitude": {
        "definition": "Maximum displacement from equilibrium.",
        "formula": "A",
        "mihu": "There is a limit to how far the system will go. That limit defines everything.",
        "intuitive": "The highest point reached during oscillation.",
        "deep_explanation": """
Amplitude defines the maximum extent of motion from equilibrium.

It is directly related to the energy stored in the system: larger amplitudes correspond
to higher total energy.
"""
    },

    "shm" : {
        "definition": "Oscillatory motion with restoring force proportional to displacement.",

        "formula": "F = -kx",

        "mihu": "The system does not tolerate displacement. The further you go, the stronger it pulls you back.",

        "intuitive": "Spring-like motion that always pulls toward equilibrium.",

        "deep_explanation": """
Simple harmonic motion is defined by a linear restoring force that is proportional
to displacement and directed toward equilibrium.

This leads to a second-order differential equation whose solutions are sinusoidal.
Energy oscillates between kinetic and potential forms without loss in the ideal case.

The motion is fully deterministic and periodic.
"""
    },
    "assumptions": {
        "definition": "Conditions required for oscillatory motion to occur.",

        "mihu": "Not every system oscillates. Only those that are allowed to return.",

        "deep_explanation": """
For oscillations to occur, two key conditions must be satisfied:

1) A restoring force must exist, acting to return the system to equilibrium.
   Examples include gravitational and elastic forces.

2) The system must possess energy. Displacing the system from equilibrium requires work,
   which is stored as potential energy and later converted into motion.
"""
    }
}
