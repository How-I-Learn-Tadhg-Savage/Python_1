# Question 1
# Simple Message: Assign a message to a variable, and then print that message.
message = "I like apples"
print (message)

#Question 2
# Simple Messages: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
message = "I like apples"
print (message)
message = "I don't like apples"
print (message)

# Question 3 
# Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = "Michael"
print (f"hello {name}, how are you doing today?")

# Question 4
# Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name = "john"
print (name.title())
print (name.lower())
print (name.upper())

# Question 5
# Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
Author = "Albert Eintein"
print (f'{Author}, once said: "A person who never made a mistake never tried anything new."')

# Question 6
# Assigning variable to quote and printing 
Author = "Albert Eintein"
famous_quote = (f'{Author}, once said: "A person who never made a mistake never tried anything new."')
print (famous_quote)

# Question 7
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
name = " John "
print (name)
name = " John "
print (name.lstrip())
name = " John "
print (name.rstrip())
name = " John "
print (name.strip())

# Question 8
#  File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
file = "python.txt"
print (file.removesuffix(".txt"))

# Question 9
# Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results.
print (4 + 4)
print (10 - 2)
print (2 * 4)
print (16 / 2)

# Question 10
# Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.
favourite_number  = 10
message = f"My favourite number is {favourite_number}!"
print (message)

# Question 11
## Use tab and new line for your favourite languages
print ("My favourite langauges are:\n\tPython\n\tJava\n\tGolang")

# The Zen of Python
import this
