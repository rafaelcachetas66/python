# PROJECT

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line

action_1 = input("Do you wish to go left or right? ").lower()

if(action_1 == "left"):
    print("Good choice.")
    action_2 = input("Do you wish to swim or to wait? ").lower()
    if(action_2 == "wait"):
        print("Good choice.")
        action_3 = input("Which door do you want to open: red, blue or yellow?" ).lower()
        if(action_3 == "red"):
            print("You die. Game over!")
        elif(action_3 == "blue"):
            print("You die. Game over!")
        elif(action_3 == "yellow"):
            print("You win. Congratulations!")
        else:
            print("No smarties here. Game over!")
    elif(action_2 == "swim"):
        print("You die. Game over!")
    else:
        print("No smarties here. Game over!")
elif(action_1 == "right"):
    print("You die. Game over!")
else:
    print("No smarties here. Game over!")    