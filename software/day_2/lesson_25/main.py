# INSTRUCTIONS

# Create a program using maths and f-strings that tells us how many weeks we have left, if we live until 90 y/o.
# It will take your current age as the input and the output a message with our time left in this format:
# "You have x weeks left."
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.
# WARNING: your output should match the EXAMPLE OUTPUT format exactly, even the positions of the commas and full stops.

age = input()

# Write your code below

# Calculate the number of years left
years = 90 - int(age)

# Pass the years to weeks
weeks_left = years * 52

# Print the result
print(f"You have {weeks_left} left.")