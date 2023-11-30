# PROJECT: Rock Paper Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 

import random

# Input for the user choice
user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Print the ASCII of the chosen option
if(user_option == 0):
    print(rock)
elif(user_option == 1):
    print(paper)
elif(user_option == 2):
    print(scissors)
else:
    print("Wrong option.")
    
# Randomize the computer option
computer_option = random.randint(0, 2)

# Print the ASCII of the chosen computer option
if(computer_option == 0):
    print(rock)
elif(computer_option == 1):
    print(paper)
elif(computer_option == 2):
    print(scissors)
else:
    print("Wrong option.")
    
# If/Else Statement Rules for the RSP
if(user_option == 0 and computer_option == 0):
    print("It's a draw.")
elif(user_option == 1 and computer_option == 1):
    print("It's a draw.")
elif(user_option == 2 and computer_option == 2):
    print("It's a draw.")        
elif(user_option == 0 and computer_option == 1):
    print("You lose.")
elif(user_option == 1 and computer_option == 0):
    print("You win.")
elif(user_option == 0 and computer_option == 2):
    print("You win.")
elif(user_option == 2 and computer_option == 0):
    print("You lose.")
elif(user_option == 1 and computer_option == 2):
    print("You lose.")
elif(user_option == 2 and computer_option == 1):
    print("You win.")