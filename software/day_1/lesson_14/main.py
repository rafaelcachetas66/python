# INSTRUCTIONS
# This program takes two inputs. The first input is stored in a variable called a.
# The second input is stored in a variable called b.
########################################
# Write a program that switches the value stored in the variables a and b.
########################################
# There are two variables, a and b from input

a = input()
b = input()

# Don't change the code above
#############################
# Write your code below this line
 
x = a # x is a dummy variable
a = b  
b = x 

# Write your code above this line
print("a: " + a)
print("b: " + b)
