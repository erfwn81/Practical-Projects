#Erfan Mirzae HW1 Q3
"""
Zoo Management System
- Store animals in a list
- Show their details
- Classify them by number of legs
"""

# a function to print one animal's details using dictionary
def print_animal(animal):
    # animal is just a dictionary with info
    print(f"Name: {animal['name']}, Species: {animal['species']}, "
          f"Legs: {animal['legs']}, Habitat: {animal['habitat']}")

# a function that classifies animals based on how many legs they have
def classify_legs(legs):
    if legs == 0:
        return "No legs → Snake or Fish"
    elif legs == 2:
        return "Two legs → Bird or Human"
    elif legs == 4:
        return "Four legs → Mammal or Reptile"
    elif legs > 4:
        return "More than four legs → Insect or Spider"
    else:
        return "Unknown classification"

def main():
    # A list of animals (each one is a dictionary)
    animals = [
        {"name": "Lion", "species": "Mammal", "legs": 4, "habitat": "Grassland"},
        {"name": "Eagle", "species": "Bird", "legs": 2, "habitat": "Mountains"},
        {"name": "Cobra", "species": "Reptile", "legs": 0, "habitat": "Forest"},
        {"name": "Frog", "species": "Amphibian", "legs": 4, "habitat": "Wetlands"},
        {"name": "Spider", "species": "Arachnid", "legs": 8, "habitat": "Various"},
        {"name": "Clownfish", "species": "Fish", "legs": 0, "habitat": "Ocean"},
    ]

    # Show details of each animal
    print("-- Animal Details --")
    for animal in animals:
        print_animal(animal)

    # Show classification by legs
    print("\n-- Classification by Legs --")
    for animal in animals:
        print(f"{animal['name']}: {classify_legs(animal['legs'])}")

# Running the program
main()

