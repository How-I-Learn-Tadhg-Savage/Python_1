# Looping through an enire list and printing
# First lets define a list
magicians = ['david', 'alice', 'sarah', 'cristina']
# Now lets deifne the loop
for magician in magicians:
    # Remeber to keep the indentation and print each magician allowing the loop to loop through the list 
    print (magician)

# One can also do more work with lists by incorporating f strings 
# First define the list
dogs = ['smudge', 'paddy', 'jackson']
# Define the loop
for dog in dogs:
    # Printing the loop for all dogs in an f string and also to title
    print (f"Good boy, {dog.title()}.")

# The indentation is important, anything indented is considered in the loop and will be looped. 
# Defining a list
cars = ['bugatti', 'ferarri', 'lamborghini']
# Defining the loop
for car in cars:
    # Indented and therefore both print statements will be looped, new line will make each loop be seperated
    print (f"I really want a {car.title()}.")
    print (f'{car.title()}, is very pretty.\n')
# Not indented and will not be looped 
print ("End of loop")

# Making Numerical Lists
# Using the range function to generate a list of numbers of 1 too 6
for value in range(1, 5):
    print (value)

# One can also more direcly use the range function with it starting from 0
for value in range(6):
    print (value)

# We can also use the function to create a list using range
numbers = list(range(1, 6))
print (numbers)

# We can also pass a thrid argument to range to skip numbers in intervals 
even_numbers = list(range(0, 11, 2))
print (even_numbers)

# One can also create a list of squared nunbers using the range and loop function
# First create an empty list
squares = []
# Create a for loop with range to craete initial set of numbers 
for value in range(1, 11):
    # We then square the value and give it the variable square
    square = value ** 2
    # Append the new values attached to square to our list squares
    squares.append(square)
# Print the new list
print (squares)

# Using minimum and maximum and sum in numbers
digits = []
for value in range(1, 101):
    digits.append(value)
print (digits)

# Using min, max and sum functions on our newly created list
print (min(digits))
print (max(digits))
print (sum(digits))


# List comprehensions 
# A list comprehension allows you to generate this same list in just one line of code.
# List of digits created using list comprehension 
digits = [value for value in range(1, 11)]
print (digits)

# List of squares created using a list comprehension
squares = [value ** 2 for value in range(1, 11)]
print (squares)

# Slicing a list in python
players = ['chales', 'phobe', 'katie', 'chiara', 'tadhg', 'dan', 'jason', 'anne', 'mat']
print (players[0:3])
# One can slice at sny intervel set
print (players[1:4])
# If you omit the first index python starts at the begginging of the list
print (players[:3])
# If you omit the last index python will print to the end of the list
print (players[2:])
# Remeber we can also use a negative index to output begining or end index of a list regarless of length
# This will only print the last three values in a list
print (players[-3:])
# This will always omit the last three values in a list
print (players[:-3])

# We can now use this to show how we can loop through a slice to print a message
# Defining a list
players = ['dan', 'jason', 'anne', 'tadhg', 'caoimhe']
# Initial print statement outside of loop
print ("Welcome to the game:")
# Creating the for loop for certain index range
for player in players[:3]:
    # Printing inside of the for loop each player to title
    print(player.title())


# Copying a list 
# We can use slices to copy a list by taking a slice of an entire list 
cars = ['bugatti', 'bmw', 'mercedes', 'jaguar', 'ford']
# We can copy to a new list by taking a slice using no indexs to get a copy of an entire list
friends_cars = cars[:]
print ("My favourite cars are:")
print (friends_cars)
# A new copy has been made and to prove we can append new items to both in the list
cars.append("kia")
friends_cars.append("honda")
print (f'\n{cars}')
print (friends_cars)

# Now you cannot copy a list by setting a list equal to a new list, foir example
my_foods = ['beans', 'toast', 'eggs', 'bacon', 'beef']
# THIS WILL NOT WORK (LOGICAL ERROR)
# This has set friends_foods equal to my_foods
friends_foods = my_foods
print (my_foods)
print (friends_foods)
# Appending a new different item to both lists
my_foods.append('turkey')
friends_foods.append('yogurt')
# Printing both lists and they will now contain oneanothers food, logical error produced
print (my_foods)
print (friends_foods)


















