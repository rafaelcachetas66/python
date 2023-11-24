# RANDOM MODULE

import random # import random module
import mymodule # import my module

random_integer = random.randint(1,10) # generate a random int between 1 and 10
print(random_integer)

random_float = random.random() # generate a random float number between 0.0 and 0.99
print(random_float)

print(random_float * 5) # generate a random float between 0.00 and 4.99

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

print(mymodule.pi)