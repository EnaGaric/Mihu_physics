from data.oscilations import oscilations
from data.shm import shm
from data.spring_mass import spring_with_mass

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
    concepts = [shm, spring_with_mass]

    while True:
        print("\n==============================")
        print("        MIHU PHYSICS")
        print("==============================")
        print("1. Basic theory (Oscillations)")
        print("2. Concepts")
        print("0. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            show_basic_theory()

        elif choice == "2":
            # Pod-menu za izbor koncepta
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

        else:
            print("\nInvalid choice.\n")

# ----- Pokretanje aplikacije -----
if __name__ == "__main__":
    main_menu()