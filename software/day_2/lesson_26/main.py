# DAY 2: PROJECT

# If the bill was 150.00€, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

# Write your code below

print("Welcome to the tip calculator.") # Greet the user

bill = float(input("What was the total bill? $")) # Read the input and cast to float
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) # Read the input and cast to float
people = int(input("How many people to split the bill? ")) # Read the input and cast to int


total = round((bill / people) * (tip / 100 + 1), 2)

print(f"Each person should pay: ${total}")
 