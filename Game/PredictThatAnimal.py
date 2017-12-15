'''
Predict the animal the user is thinking of by prompting them with a series of yes or no questions about the animal.
Team Members: Tessa Gebert and Shreya Ravi
'''

# Add points to all specified animals (any number is allowed)
def add_points(dict_animals, points, *critters):
	for critter in critters:
		dict_animals[critter] += points
	return True

# Ask user the question
def ask_question(question):
	return (raw_input(question + " Answer Yes or No. ").lower() == "yes") 

# List of all the animals -- used to initialize dictionary
list_of_animals = [
    "Dog",
    "Cat",
    "Horse",
    "Tiger",
    "Bear",
    "Giraffe",
    "Bird",
    "Lion",
    "Pig",
    "Otter",
    "Panda",
    "Hippopotamus",
    "Octopus",
    "Frog",
    "Alligator",
    "Raccoon",
    "Deer",
    "Sloth",
    "Snake",
    "Shark",
    "Cow",
    "Monkey",
    "Elephant",
    "Ape",
    "Kangaroo",
    "Platypus",
    "Camel",
    "Flamingo",
    "Lizard",
    "Bat",
    "Seal",
    "Fish",
    "Fox",
    "Ostrich",
    "Hyena",
    "Spider",
    "Insect",
    "Buffalo",
    "Goat",
    "Duck",
    "Baboon",
    "Lemur",
    "Salamander",
    "Mouse",
    "Porcupine",
    "Armadillo",
    "Lobster",
    "Dolphin",
    "Rabbit",
    "Chicken",
    "Human",
    "Koala"
]

# Create dictionary with all animals, set all animal scores to 0
animals = dict()
for critter in list_of_animals:
	animals[critter] = 0

# User chooses animal
raw_input("Pick an animal and press Enter when you have settled on one.")

# Question 1
if ask_question("Do people usually keep this animal as a pet?"):
    add_points(animals, 15, 
        "Dog", "Cat",
        "Horse", "Bird",
        "Frog", "Snake",
        "Lizard", "Fish",
        "Mouse", "Rabbit",
        "Monkey","Pig",
		"Chicken")

# Question 2
if ask_question("Do people in the United States typically eat this animal?"):
	add_points(animals, 25,
		"Cow", "Fish",
		"Duck", "Pig",
		"Chicken", "Lobster",
		"Rabbit", "Frog",
		"Octopus", "Goat")
else:
	add_points(animals, 5, "Porcupine", "Dog", "Cat")

# Question 3
if ask_question("Is your animal a mammal?"):
	add_points(animals, 25,
		"Cow", "Pig",
		"Rabbit", "Goat",
		"Dolphin", "Dog", 
		"Cat", "Horse",
		"Tiger", "Bear",
		"Giraffe", "Lion",
		"Otter", "Panda",
		"Hippopotamus", "Raccoon",
		"Deer", "Sloth",
		"Monkey", "Elephant",
		"Ape", "Kangaroo",
		"Platypus", "Camel",
		"Bat", "Seal",
		"Fox", "Hyena", 
		"Buffalo", "Porcupine",
		"Armadillo", "Koala",
		"Lemur", "Mouse",
		"Human")

# Question 4
if ask_question("Does this animal come from Africa?"):
	add_points(animals, 20,
		"Giraffe","Lion",
		"Hippopotamus", "Bird",
		"Snake", "Monkey",
		"Elephant", "Ape",
		"Baboon", "Flamingo",
		"Camel", "Lizard",
		"Frog", "Fish", 
		"Ostrich", "Hyena",
		"Spider", "Lemur",
		"Insect")
else:
	add_points(animals, 25, "Tiger", "Bear", "Armadillo")
	add_points(animals, -20, "Hippopotamus")
# Question 5
if ask_question("Are most people afraid of this animal?"):
	add_points(animals, 40,
		"Tiger", "Bear",
		"Lion", "Alligator",
		"Snake", "Shark",
		"Hyena", "Spider",
		"Insect", "Lizard",
		"Mouse")

# Question 6
if ask_question("Does this animal normally live in the water?"):
	add_points(animals, 50,
		"Otter", "Hippopotamus",
		"Octopus", "Frog",
		"Alligator", "Platypus",
		"Seal", "Fish",
		"Dolphin", "Salamander",
		"Duck", "Lobster")

# Question 7
if ask_question("Does this animal walk on only four legs?"):
	add_points(animals, -50,
		"Duck", "Chicken",
		"Dolphin", "Lobster",
		"Insect", "Spider",
		"Ostrich", "Human",
		"Fish", "Seal",
		"Bat", "Flamingo",
		"Kangaroo", "Ape",
		"Shark", "Snake",
		"Platypus")
# Question 8
if ask_question("Is this animal considered a pest?"):
	add_points(animals, 50,
		"Insect", "Spider",
		"Snake", "Mouse",
		"Raccoon")

# Question 9
if ask_question("Can this animal fly long distances?"):
	add_points(animals, 65,
		"Duck", "Insect",
		"Bat", "Flamingo",
		"Bird", "Pig")

# Question 10
if ask_question("Does this animal have armor?"):
	add_points(animals, 100,
		"Porcupine", "Insect",
		"Armadillo")

# Question 11
if ask_question("Do people ride this animal?"):
	add_points(animals, 75,
		"Horse", "Cow",
		"Elephant", "Camel",
		"Dolphin")

# Question 12
if ask_question("Is this animal used in lab testing"):
	add_points(animals, 100,
		"Mouse", "Pig",
		"Goat", "Frog",
		"Ape")

# Question 13
if ask_question("Is this animal an amphibian?"):
	add_points(animals, 250,
		"Frog", "Salamander")

# Question 14
if ask_question("Is this animal considered relatively intelligent?"):
	add_points(animals, 75,
		"Ape", "Human",
		"Dolphin", "Horse",
		"Dog", "Cat",
		"Octopus", "Fox",
		"Elephant")

# Question 15
if ask_question("Can this animal roar?"):
	add_points(animals, 125,
		"Tiger", "Bear",
		"Lion")

# Question 16
if ask_question("Is this animal considered man's best friend?"):
	add_points(animals, 500,
		"Dog")

# Question 17
if ask_question("Does this animal have scales?"):
	add_points(animals, 80,
		"Fish","Alligator",
		"Lizard","Snake",
		"Shark")

# Question 18
if ask_question("Is this animal extremely large?"):
	add_points(animals, 100,
		"Hippopotamus", "Elephant",
		"Giraffe")

# Question 20
if ask_question("Does this animal laugh?"):
	add_points(animals, 250,
		"Dolphin", "Hyena",
		"Fox")
# Question 21
if ask_question("Does this animal sleep a lot?"):
	add_points(animals, 200,
		"Cat", "Sloth",
		"Koala", "Panda")

# Question 22
if ask_question("Is this animal black and white?"):
	add_points(animals, 250,
		"Panda", "Lemur",
		"Raccoon")

#Question 23
if ask_question("Does this animal live in Australia?"):
	add_points(animals, 300,
		"Kangaroo", "Koala",
		"Platypus")
else:
	add_points(animals, -15, "Koala")

# Question 24
if ask_question("Does this animal jump to get places?"):
	add_points(animals, 300,
		"Kangaroo", "Frog",
		"Rabbit")

# Question 25
if ask_question("Does this animal bark?"):
	add_points(animals, 400,
		"Dog", "Seal")

# Question 26
if ask_question("Is this animal an herbivore?"):
	add_points(animals, 350,
		"Sloth", "Giraffe",
		"Horse", "Kangaroo",
		"Koala", "Elephant",
		"Camel", "Cow",
		"Rabbit", "Porcupine")

# Question 27
if ask_question("Is this animal typically hunted in the US?"):
	add_points(animals, 50,
		"Bear", "Deer",
		"Fox", "Rabbit",
		"Raccoon", "Buffalo",
		"Duck", "Alligator",
		"Snake", "Otter")
else:
	add_points(animals, 20, "Tiger")

# Find animal with highest score
max_score = 0
max_animal = ""
index = 0
for critter in animals.keys():
	max_score = max(max_score, animals[critter])
	if animals[critter] == max_score:
		max_animal = critter
print ("Your animal is a " + max_animal)
