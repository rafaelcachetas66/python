# CODING EXERCISE

# Check if a number is odd or even based on the user input.

# Which number do you want to check?
number = int(input())

# Write your code below this line

if (number % 2 == 0): # if it can be divided by 2, then it is even
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")