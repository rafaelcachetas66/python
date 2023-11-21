# INSTRUCTIONS
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height.
# The BMI is calculated by dividing a person's weight (kg), by the square of their height (m).
# NOTE: You should convert the bmi to a whole number and print out a whole number in order to pass all the tests.

# 1st input: enter height in meters and cast to float
height = float(input())

# 2nd input: enter weight in kilograms and cast to integer
weight = int(input())

# do the math and cast to integer
bmi = weight / (height ** 2)
print(int(bmi))
