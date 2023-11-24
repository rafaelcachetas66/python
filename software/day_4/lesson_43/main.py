# CODING EXERCISE: Heads or Tails

# INSTRUCTIONS
# You are going to write a virtual coin toss program. It will randomly tell the user
# "Heads" or "Tails"

# Important, the first letter should be capitalised and spelt exactly like in the example

# There are many ways of doing this. But to practice what we learnt in the last lesson,
# you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

# 1 => "Heads"
# 0 => "Tails"

# Write your code below

import random

coin_toss = random.randint(0, 1) # generate a random number between 0 and 1

if(coin_toss == 0):
    print("Tails")
else:
    print("Heads")