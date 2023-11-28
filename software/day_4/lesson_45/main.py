# CODING EXERCISE: Banker Roullette - Who will pay the bill?

# INSTRUCTIONS

# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

# IMPORTANT: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names.
# For this to work, you must enter all the names as names followed by comma then space.

# NOTE: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.

import random

# HINT: Assume that names looks like this: input: x, y, z names = ["x", "y", "z"]

names = names_string.split(",")

# The code above converts the input into an array separating each name in the input by a comma and space.

# Get the total number of items in list
num_items = len(names)

# Generate a random number between 0 and the last index
random_choice = random.randint(0, num_items-1)

# Pick out random person from list of names using the random number.
person_who_pays = names[random_choice]

print(person_who_pays + " is going to buy the meal.")





