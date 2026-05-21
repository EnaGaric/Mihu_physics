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

from Mihu_physics.data.waves.shm import shm
from Mihu_physics.data.waves.spring_mass import spring_with_mass
from Mihu_physics.data.waves.damped_oscilations import damped_oscillations
from Mihu_physics.data.waves.types_of_damped import types_damped
from Mihu_physics.data.waves.quiz import quiz_data
from Mihu_physics.data.waves.forced_oscilations import forced_oscillations
from Mihu_physics.data.waves.frequency_limit import frequency_limits
from Mihu_physics.data.waves.normal_mode1 import normal_modes


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
        print("1. Explanation")
        print("2. Derivation")
        print("3. Deep dive")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            mihu_type(concept.explanation)
        elif choice == "2":
            mihu_type(concept.derivation)
        elif choice == "3":
            mihu_type(concept.deep_dive)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


#BASIC THEORY SOURCES
basic_theory_sources = [
    oscilations,
    normal_modes_dive
]


#BASIC THEORY MENU
def show_basic_theory():
    combined = {}

    #merge svih dictova
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


#MAIN MENU
def main_menu():
    concepts = [
        shm,
        spring_with_mass,
        damped_oscillations,
        types_damped,
        forced_oscillations,
        frequency_limits,
        normal_modes
    ]

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
            while True:
                print("\n--- CONCEPTS ---")

                for i, c in enumerate(concepts, start=1):
                    print(f"{i}. {c.name}")

                print("0. Back")

                sub_choice = input("Choose concept: ")

                if sub_choice == "0":
                    break

                try:
                    idx = int(sub_choice) - 1

                    if 0 <= idx < len(concepts):
                        display_concept_part(concepts[idx])
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