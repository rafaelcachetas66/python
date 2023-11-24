# UNDERSTANDING THE OFFSET AND APPENDING ITEMS TO LISTS

# We can store various types of data in the list

states_of_america = ["Delaware", "Pennsylvania"] # creation of the list

print(states_of_america[0]) # it prints the first item in the list

print(states_of_america[-1]) # it prints the last item in the list

states_of_america[1] = "Pencilvania" # modify an item in the list

print(states_of_america[1]) # prints the modified item

states_of_america.append("New Jersey") # appends an item to the end of the list

states_of_america.extend(["Virginia", "New York"]) # extends the list
print(states_of_america)

