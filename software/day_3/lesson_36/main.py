# CODE EXERCISE: Pizza Order

# INSTRUCTIONS
# Congratulations, you've got a job at Python Pizza! Your first
# job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
    # SMALL PIZZA (S): $15
    # MEDIUM PIZZA (M): $20
    # LARGE PIZZA (L): $25
    # PEPPERONI FOR SMALL PIZZA: +$2
    # PEPPERONI FOR MEDIUM OR LARGE PIZZA: +$3
    # EXTRA CHEESE FOR ANY PIZZA: +$1

print("Thank you for choosing Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")

# Write your code below

bill = 0

if(size == 'S'):
    bill += 15
    if(add_pepperoni == 'Y'):
        bill += 2
    if(extra_cheese == 'Y'):
        bill += 1
elif(size == 'M'):
    bill += 20
    if(add_pepperoni == 'Y'):
        bill += 3
    if(extra_cheese == 'Y'):
        bill += 1
elif(size == 'L'):
    bill += 25
    if(add_pepperoni == 'Y'):
        bill += 3
    if(extra_cheese == 'Y'):
        bill += 1
print(f"Your final bill is ${bill}.")