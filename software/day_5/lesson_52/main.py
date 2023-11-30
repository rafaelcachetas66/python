# CODING EXERCISE: Average Height

# INSTRUCTIONS
# You are going to write a program that calculates the average student
# height from a List of heights.

# Average height rounded to the nearest whole number.
# You should not use the sum() or len() functions in your
# answer. You should try to replicate their functionality using what you
# have learnt about for loops.

# Input a Python list of students height
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
    
# Add the students heights in the loop
total_height = 0
for height in student_heights:
    height += total_height
    
print(f"The total height is {total_height}.")

# Number of students
number_students = 0
for number in student_heights:
    number_students += 1

print(f"The total number of students is {number_students}.")

average = round(total_height / number_students)
print(f"The average is {average}.")


    


 