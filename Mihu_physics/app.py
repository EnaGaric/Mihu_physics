import random
import time

#MIHU TYPING EFFECT
def mihu_type(text):
    import time, random

    for char in text:
        print(char, end="", flush=True)

        if char in ".!?":
            time.sleep(1)
        elif char in ",":
            time.sleep(0.7)
        else:
            time.sleep(random.uniform(0.01, 0.1))

    print()


#IMPORTS
from Mihu_physics.data.waves.oscilations import oscilations
from Mihu_physics.data.waves.normal_mode2 import normal_modes_dive
from Mihu_physics.data.waves2.basic import waves_intro
from Mihu_physics.data.waves2.wave_velocity import wave_velocities

from Mihu_physics.data.waves.shm import shm
from Mihu_physics.data.waves.spring_mass import spring_with_mass
from Mihu_physics.data.waves.damped_oscilations import damped_oscillations
from Mihu_physics.data.waves.types_of_damped import types_damped
from Mihu_physics.data.waves.quiz import quiz_data
from Mihu_physics.data.waves.forced_oscilations import forced_oscillations
from Mihu_physics.data.waves.frequency_limit import frequency_limits
from Mihu_physics.data.waves.normal_mode1 import normal_modes
from Mihu_physics.data.waves.nm_method import normal_modes_method
from Mihu_physics.data.waves.nm_example import coupled_oscillators
from Mihu_physics.data.waves.N_oscillators import n_coupled_oscillators
from Mihu_physics.data.waves2.wave_equation import wave_equation_derivation
from Mihu_physics.data.waves2.standing_wave import standing_waves
from Mihu_physics.data.waves2.sound_wave import sound_waves
from Mihu_physics.data.waves2.energy_intensity import sound_energy_and_intensity
from Mihu_physics.data.waves2.doppler import doppler_effect
from Mihu_physics.data.waves2.fourier import fourier_analysis
from Mihu_physics.data.waves2.dispersion import dispersion_effect


#GROUPS (NEW STRUCTURE)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


OSCILLATIONS_CONCEPTS = [
    shm,
    spring_with_mass,
    damped_oscillations,
    types_damped,
    forced_oscillations,
    frequency_limits,
    normal_modes,
    normal_modes_method,
    coupled_oscillators,
    n_coupled_oscillators,
]

WAVES_CONCEPTS = [
    wave_equation_derivation,
    standing_waves,
    sound_waves,
    sound_energy_and_intensity,
    doppler_effect,
    fourier_analysis,
    dispersion_effect
]


#QUIZ
def run_quiz():
    print("\n=== QUIZ MODE ===")

    concepts = list(quiz_data.keys())

    for i, c in enumerate(concepts, start=1):
        print(f"{i}. {c}")
    print("0. Back")

    choice = input("Choose concept: ")

    if choice == "0":
        return

    try:
        concept_name = concepts[int(choice) - 1]
    except:
        print("Invalid choice.")
        return

    questions = quiz_data[concept_name].copy()
    random.shuffle(questions)

    score = 0

    for q in questions:
        print("\n" + q["question"])

        options = q["options"].copy()
        correct_text = options[q["answer"] - 1]

        random.shuffle(options)

        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        ans = input("Your answer: ")

        if ans.isdigit():
            ans_index = int(ans) - 1

            if 0 <= ans_index < len(options) and options[ans_index] == correct_text:
                print("✔ Correct")
                score += 1
            else:
                print("✖ Wrong")
                print(f"Correct answer: {correct_text}")
        else:
            print("✖ Invalid input")

    print(f"\nScore: {score}/{len(questions)}")

    if score == len(questions):
        print("Mihu: Acceptable. You didn't embarrass yourself.")
    elif score >= len(questions) // 2:
        print("Mihu: You understand the basics. Barely.")
    else:
        print("Mihu: This is disappointing.")


#CONCEPT VIEW
def display_concept_part(concept):
    while True:
        print(f"\n=== {concept.name} ===")
        print("1. Definition")
        print("2. Explanation")
        print("3. Derivation")
        print("4. Deep dive")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            mihu_type(concept.definition)
        elif choice == "2":
            mihu_type(concept.explanation)
        elif choice == "3":
            mihu_type(concept.derivation)
        elif choice == "4":
            mihu_type(concept.deep_dive)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


#BASIC THEORY SOURCES
basic_theory_sources = [
    oscilations,
    normal_modes_dive,
    waves_intro,
    wave_velocities
]


#BASIC THEORY MENU
def show_basic_theory():
    combined = {}

    for source in basic_theory_sources:
        for k, v in source.items():
            combined[k] = v

    while True:
        print("\n=== BASIC THEORY (Oscillations + Modes) ===")

        keys = list(combined.keys())

        for i, key in enumerate(keys, start=1):
            print(f"{i}. {key}")

        print("0. Back")

        choice = input("Choose concept: ")

        if choice == "0":
            break

        try:
            idx = int(choice) - 1

            if 0 <= idx < len(keys):
                key = keys[idx]
                value = combined[key]

                print("\n----------------------------------")
                print(key.upper())
                print("----------------------------------")

                mihu_type(value.get("mihu", ""))

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input.")


#MAIN MENU (UPDATED)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def main_menu():
    while True:
        print("\n==============================")
        print("        MIHU PHYSICS")
        print("==============================")
        print("1. Basic theory")
        print("2. Concepts")
        print("3. Quiz")
        print("0. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            show_basic_theory()

        elif choice == "2":

            #GROUP MENU
            while True:
                print("\n--- CONCEPT GROUPS ---")
                print("1. Oscillations")
                print("2. Waves")
                print("0. Back")

                group_choice = input("Choose group: ")

                if group_choice == "0":
                    break

                if group_choice == "1":
                    current_group = OSCILLATIONS_CONCEPTS
                    group_name = "OSCILLATIONS"

                elif group_choice == "2":
                    current_group = WAVES_CONCEPTS
                    group_name = "WAVES"

                else:
                    print("Invalid choice.")
                    continue

                #CONCEPT LIST
                while True:
                    print(f"\n--- {group_name} CONCEPTS ---")

                    for i, c in enumerate(current_group, start=1):
                        print(f"{i}. {c.name}")

                    print("0. Back")

                    sub_choice = input("Choose concept: ")

                    if sub_choice == "0":
                        break

                    try:
                        idx = int(sub_choice) - 1

                        if 0 <= idx < len(current_group):
                            display_concept_part(current_group[idx])
                        else:
                            print("Invalid choice.")

                    except ValueError:
                        print("Invalid input.")

        elif choice == "3":
            run_quiz()

        elif choice == "0":
            print("\nMihu is done with you.\n")
            break

        else:
            print("Invalid choice.")


#start
if __name__ == "__main__":
    main_menu()