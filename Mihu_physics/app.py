from Mihu_physics.data.waves.oscilations import oscilations
from Mihu_physics.data.waves.shm import shm
from Mihu_physics.data.waves.spring_mass import spring_with_mass
from Mihu_physics.data.waves.damped_oscilations import damped_oscillations
from Mihu_physics.data.waves.types_of_damped import types_damped
from Mihu_physics.data.waves.quiz import quiz_data
import random

def run_quiz():
    print("\n=== QUIZ MODE ===")

    #izbor koncepta
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

    #RANDOM ORDER
    questions = quiz_data[concept_name].copy()
    random.shuffle(questions)

    score = 0

    for q in questions:
        print("\n" + q["question"])

        #RANDOMIZACIJA
        options = q["options"].copy()
        correct_answer = options[q["answer"] - 1]

        random.shuffle(options)

        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        ans = input("Your answer: ")

        if ans.isdigit():
            ans_index = int(ans) - 1

            if 0 <= ans_index < len(options) and options[ans_index] == correct_answer:
                print("✔ Correct")
                score += 1
            else:
                print("✖ Wrong")
                print(f"Correct answer: {correct_answer}")
        else:
            print("✖ Invalid input")

    print(f"\nScore: {score}/{len(questions)}")


    if score == len(questions):
        print("Mihu: Acceptable. You didn't embarrass yourself.")
    elif score >= len(questions) // 2:
        print("Mihu: You understand the basics. Barely.")
    else:
        print("Mihu: This is disappointing.")


# ----- Funkcija za pod-menu koncepta -----
def display_concept_part(concept):
    """Prikaz Explanation, Derivation ili Deep dive za odabrani koncept."""
    while True:
        print(f"\n=== {concept.name} ===")
        print("1. Explanation")
        print("2. Derivation")
        print("3. Deep dive")
        print("0. Back to Concepts")
        choice = input("Choose: ")

        if choice == "1":
            print(f"\n{concept.explanation}\n")
        elif choice == "2":
            print(f"\n{concept.derivation}\n")
        elif choice == "3":
            print(f"\n{concept.deep_dive}\n")
        elif choice == "0":
            break
        else:
            print("\nInvalid choice.\n")

# ----- Funkcija za Basic Theory -----
def show_basic_theory():
    print("\n=== BASIC THEORY (Oscillations) ===")
    for key, value in oscilations.items():
        print(f"\n--- {key.upper()} ---")
        print(f"Definition: {value.get('definition', '')}")
        print(f"Mihu: {value.get('mihu', '')}")

# ----- Glavni menu -----
def main_menu():
    concepts = [shm, spring_with_mass, damped_oscillations,types_damped]

    while True:
        print("\n==============================")
        print("        MIHU PHYSICS")
        print("==============================")
        print("1. Basic theory (Oscillations)")
        print("2. Concepts")
        print("3. Quiz")
        print("0. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            show_basic_theory()

        elif choice == "2":
            #Pod-menu za izbor koncepta
            while True:
                print("\n--- CONCEPTS ---")
                for i, c in enumerate(concepts, start=1):
                    print(f"{i}. {c.name}")
                print("0. Back to Main Menu")

                sub_choice = input("Choose concept: ")
                if sub_choice == "0":
                    break
                try:
                    sub_index = int(sub_choice) - 1
                    if 0 <= sub_index < len(concepts):
                        display_concept_part(concepts[sub_index])
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid input. Enter a number.")

        elif choice == "0":
            print("\nMihu is done with you.\n")
            break

        elif choice == "3":
            run_quiz()

        else:
            print("\nInvalid choice.\n")

# ----- Pokretanje aplikacije -----
if __name__ == "__main__":
    main_menu()