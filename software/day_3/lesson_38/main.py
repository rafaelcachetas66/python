# CODING EXERCISE: Love Calculator

# INSTRUCTIONS
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
    # Take both people's names and check for the number of times the letters in the word TRUE occurs.
    # Then check for the number of times the letters in the word LOVE occurs.
    # Then combine these numbers to make a 2 digit number
# For Love Scores less than 10 or greater than 90, the message should be:
    # "Your score is x, you go together like coke and mentos"
# For Love Scores between 40 and 50, the message should be:
    # "Your score is x, you are alright together"
# Otherwise, the message should be just the score

print("The Love Calculator is calculating your score...")
name1 = input("Insert the name of the first person: ")
name2 = input("Insert the name of the second person: ")

# Write your code below

combined_names = name1 + name2 # combine both names
lower_names = combined_names.lower() # put the combined name all in lower case
t = lower_names.count("t") # count how many 't' it has
r = lower_names.count("r") # count how many 'r' it has
u = lower_names.count("u") # count how many 'u' it has
e = lower_names.count("e") # count how many 'e' it has
first_digit = t + r + u + e

l = lower_names.count("l") # count how many 'l' it has
o = lower_names.count("o") # count how many 'o' it has
v = lower_names.count("v") # count how many 'v' it has
second_digit = l + o + v + e

total_score = int(str(first_digit) + str(second_digit))

# if/else statements
if(total_score < 10 and total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos")
elif(total_score < 50 and total_score > 40):
    print(f"Your score is {total_score}, you are alright together")
else:
    print(f"Your score is {total_score}")