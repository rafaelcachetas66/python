# CODING EXERCISE: BMI2.0

# INSTRUCTIONS
# Write a program that interprets the BMI based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
    # Under 18.5 they are underweight
    # Over 18.5 but below 25 they have a normal weight
    # Over 25 but below 30 they are slightly overweight
    # Over 30 but below 35 they are obese
    # Above 35 they are clinically obese
    
# Enter your height in meter
height = float(input("Enter your height: "))

# Enter you weight in kilograms
weight = int(input("Enter your weight: "))

# Write your code below

# Calculate the BMI
bmi = weight / (height ** 2)

# If/Else Statements
if(bmi < 18.5):
    print(f"You are underweight, because your BMI is {round(bmi, 2)}.")
elif(bmi >= 18.5 and bmi < 25):
    print(f"You have normal weight, because your BMI is {round(bmi, 2)}.")
elif(bmi >= 25 and bmi < 30):
    print(f"You are slightly overweight, because your BMI is {round(bmi, 2)}.")
elif(bmi >= 30 and bmi < 35):
    print(f"You are obese, because your BMI is {round(bmi, 2)}.")
else:
    print(f"You are clinically obese, because your BMI is {round(bmi, 2)}.")