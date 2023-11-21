# NUMBER MANIPULATION AND F STRINGS IN PYTHON

# To round a number, instead of using int() (that doesn't round), we can use round()
print(round(8 / 3 , 3)) # round it to 3 decimal places

# If after the division, instead of using int() we can use // (it does not round)
print(8 // 3)

# f-string (use f"EXAMPLE")
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height} and you are winning is {isWinning}")
