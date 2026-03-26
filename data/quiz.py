# data/quiz.py

quiz_data = {
    "Damped Oscillations": [
        {
            "question": "What happens to amplitude in damped oscillations?",
            "options": ["It increases", "It stays constant", "It decreases exponentially"],
            "answer": 3
        },
        {
            "question": "What is the condition for underdamped motion?",
            "options": ["γ > 2ω₀", "γ = 2ω₀", "γ < 2ω₀"],
            "answer": 3
        },
        {
            "question": "What is the general form of solution?",
            "options": [
                "x(t) = A cos(ωt)",
                "x(t) = A e^{-γt/2} cos(ωt + φ)",
                "x(t) = vt"
            ],
            "answer": 2
        },
        {
            "question": "What is a damped oscillation?",
            "options": [
                "An oscillation with constant amplitude",
                "Oscillatory motion that loses energy over time due to dissipative forces",
                "Random motion of particles",
                "Motion that never repeats"
            ],
            "answer": 2
        },
        {
            "question": "Which of the following forces represents linear damping?",
            "options": [
                "F = -k x",
                "F = -b v",
                "F = m a",
                "F = 0"
            ],
            "answer": 2
        },
        {
            "question": "What is the standard form of the damped oscillator equation?",
            "options": [
                "d²x/dt² + γ dx/dt + ω₀² x = 0",
                "d²x/dt² - γ dx/dt + ω₀² x = 0",
                "d²x/dt² + k x = 0",
                "dx/dt + γ x = 0"
            ],
            "answer": 1
        },
        {
            "question": "The damping factor γ is defined as:",
            "options": [
                "γ = k / m",
                "γ = b / m",
                "γ = m / b",
                "γ = ω₀² / b"
            ],
            "answer": 2
        },
        {
            "question": "The natural frequency of the undamped system ω₀ is:",
            "options": [
                "ω₀ = sqrt(k/m)",
                "ω₀ = b/m",
                "ω₀ = γ / 2",
                "ω₀ = k + m"
            ],
            "answer": 1
        },
        {
            "question": "What does the solution x(t) = A e^{-γ t/2} cos(ω t + φ) describe?",
            "options": [
                "Overdamped motion only",
                "Critically damped motion only",
                "Damped oscillatory motion with decaying amplitude",
                "Ideal undamped SHM"
            ],
            "answer": 3
        },
        {
            "question": "For underdamped motion, the condition is:",
            "options": [
                "γ < 2ω₀",
                "γ = 2ω₀",
                "γ > 2ω₀",
                "γ = 0"
            ],
            "answer": 1
        },
        {
            "question": "For critically damped motion, the system:",
            "options": [
                "Oscillates with decreasing amplitude",
                "Returns to equilibrium as fast as possible without oscillating",
                "Never returns to equilibrium",
                "Oscillates forever"
            ],
            "answer": 2
        },
        {
            "question": "For overdamped motion, the system:",
            "options": [
                "Returns to equilibrium slowly without oscillating",
                "Oscillates with increasing amplitude",
                "Never moves",
                "Oscillates with constant amplitude"
            ],
            "answer": 1
        },
        {
            "question": "The discriminant Δ = γ² - 4 ω₀² helps determine:",
            "options": [
                "Amplitude of oscillation",
                "Type of damping regime (under, critical, over)",
                "Mass of the oscillator",
                "Energy lost per cycle"
            ],
            "answer": 2
        },
        {
            "question": "The damped frequency ω is:",
            "options": [
                "ω = ω₀",
                "ω = sqrt(ω₀² - (γ/2)²)",
                "ω = γ / 2",
                "ω = 2π / T"
            ],
            "answer": 2
        },
        {
            "question": "Which of these statements about energy in damped oscillations is correct?",
            "options": [
                "Energy is constant over time",
                "Energy increases exponentially",
                "Energy decreases exponentially over time",
                "Energy oscillates without decay"
            ],
            "answer": 3
        },
        {
            "question": "The quality factor Q = ω₀ / γ indicates:",
            "options": [
                "Strength of damping: high Q → weak damping, low Q → strong damping",
                "Amplitude of oscillation",
                "Frequency of undamped system only",
                "Velocity at maximum displacement"
            ],
            "answer": 1
        },
        {
            "question": "Initial conditions (x₀, v₀) determine:",
            "options": [
                "Damping factor γ",
                "Amplitude and phase of oscillation",
                "Natural frequency ω₀",
                "Mass of the oscillator"
            ],
            "answer": 2
        },
        {
            "question": "Why is solving in the complex plane useful for damped oscillations?",
            "options": [
                "It changes the physical motion",
                "Derivatives of exponentials simplify the solution",
                "It removes damping",
                "It increases amplitude"
            ],
            "answer": 2
        },
        {
            "question": "Linear damping is preferred in practical physics because:",
            "options": [
                "It can be solved analytically",
                "It is physically unrealistic",
                "Quadratic damping always diverges",
                "It produces faster oscillations"
            ],
            "answer": 1
        }
    ],


    "Oscillations": [
        {
            "question": "What defines an oscillation?",
            "options": [
                "Motion that never repeats",
                "Motion around an equilibrium position that repeats in time",
                "Motion that moves in a straight line only",
                "Random motion of particles"
            ],
            "answer": 2
        },
        {
            "question": "Which quantity represents the time for one complete oscillation?",
            "options": ["Frequency", "Angular frequency", "Period", "Amplitude"],
            "answer": 3
        },
        {
            "question": "Frequency is defined as:",
            "options": [
                "Number of oscillations per unit time",
                "Maximum displacement from equilibrium",
                "Rate of change of phase angle",
                "The restoring force"
            ],
            "answer": 1
        },
        {
            "question": "Angular frequency ω is:",
            "options": ["ω = T", "ω = 2πf", "ω = f / 2π", "ω = A sin(φ)"],
            "answer": 2
        },
        {
            "question": "Elongation x(t) means:",
            "options": [
                "Maximum displacement",
                "Displacement from equilibrium at a given time",
                "Total energy of the system",
                "Frequency of oscillation"
            ],
            "answer": 2
        },
        {
            "question": "Amplitude A is:",
            "options": [
                "The restoring force",
                "Current velocity",
                "Maximum displacement from equilibrium",
                "Mass of the oscillator"
            ],
            "answer": 3
        },
        {
            "question": "The restoring force in SHM is:",
            "options": ["F = kx", "F = -kx", "F = m a²", "F = 0"],
            "answer": 2
        },
        {
            "question": "The equation of motion for SHM:",
            "options": [
                "m d²x/dt² + kx = 0",
                "m d²x/dt² - kx = 0",
                "F = m a + k x",
                "d²x/dt² = 0"
            ],
            "answer": 1
        },
        {
            "question": "The general solution x(t) = a cos(ωt) + b sin(ωt) can also be expressed as:",
            "options": [
                "x(t) = A cos(ωt + φ)",
                "x(t) = A sin(ωt)",
                "x(t) = ω t + φ",
                "x(t) = 0"
            ],
            "answer": 1
        },
        {
            "question": "Representing SHM with complex numbers x(t) = Re{A e^(i(ωt + φ))} is useful because:",
            "options": [
                "It is just a trick",
                "Differentiation becomes trivial and sine/cosine are encoded together",
                "It changes the motion physically",
                "It only works for massless springs"
            ],
            "answer": 2
        },
        {
            "question": "Why do sine and cosine functions appear naturally in SHM solutions?",
            "options": [
                "They are the only functions with derivatives that do not vanish",
                "They are easy to memorize",
                "They represent random motion",
                "They describe damping"
            ],
            "answer": 1
        },
        {
            "question": "In SHM, constants a and b are determined by:",
            "options": [
                "External forces",
                "Initial conditions of the system",
                "The mass of the observer",
                "The damping coefficient"
            ],
            "answer": 2
        },
        {
            "question": "Total energy in ideal SHM oscillates between:",
            "options": [
                "Potential energy and kinetic energy",
                "Mass and frequency",
                "Amplitude and phase",
                "Restoring force only"
            ],
            "answer": 1
        },
        {
            "question": "Why is the concept of solution space important in SHM?",
            "options": [
                "It shows that all solutions are random",
                "It shows that solutions form a structured, predictable set",
                "It is not important",
                "It only applies to damped oscillations"
            ],
            "answer": 2
        },
        {
            "question": "What does the phase constant φ represent?",
            "options": [
                "How fast the system oscillates",
                "The system’s initial state",
                "The total energy",
                "The amplitude"
            ],
            "answer": 2
        },
        {
            "question": "Why is SHM considered deterministic?",
            "options": [
                "Because motion depends only on initial conditions and known forces",
                "Because it is random",
                "Because energy disappears",
                "Because it depends on damping only"
            ],
            "answer": 1
        }
    ]
}