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











