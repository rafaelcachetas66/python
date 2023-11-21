# TYPE ERROR, TYPE CHECKING AND TYPE CONVERSION

num_char = len(input("What's your name?"))
#print("Your name has " + num_char + " characters.") # ERROR: cause it can only concatenate str, not int

print(type(num_char)) # function to return the type of the variable

new_num_char = str(num_char) # convert num_char to str
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

b = float(123)
print(type(b))
