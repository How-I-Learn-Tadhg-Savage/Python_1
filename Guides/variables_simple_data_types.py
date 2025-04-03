#First basic python program
print ("Hello World")

#Ussage of variable to store string and then print it
message = "Hello World"
print (message)

#Reassigning the variable and then printintg it
message  = "Hello Reader"
print (message)

#Changing case 
name = "ada lovelace"
print (name.title())
print (name.upper())
print (name.lower())

#Using Variables with f strings 
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print (full_name)
print (full_name.title())

#Making a message out of an f string and variables 
greeting = f"Hello, {full_name.title()}, how are you?"
print (greeting)

#Addition of a new line in a string 
print ("Languages:\nPython,\nJava\nTypescript")

#Using of both new line and new tab
print ("Languages:\n\tPython\n\tJava\n\tTypescript")

#lstrip rstrip and strip methos used on a string 
#rstrip
favourite_language = "python "
print (favourite_language.rstrip())
#lstrip
favourite_language = " python"
print (favourite_language.lstrip())
#strip
favourite_language = " python "
print (favourite_language.strip())

#Removing Prefixes with the remove preffix method
google_url = "https//:google.com"
print (google_url.removeprefix("https//:"))


#Numbers
print (2 + 2)
print (4 - 2)
print (2 * 3)
print (3 / 2)

#Exponents 
print (3 ** 2)
print (4 ** 3)

#Proof of pythons order of operations
print (2 + 3 * 2)
print ((2 + 3) * 2)

#Floats 
print (0.1 + 0.1)
print (2 * 0.2)

#Integers with Floats 

print (4 / 2)
print (2 * 0.3)
print (3.0 ** 2)

#Using underscores to make large numbers more readable 
universie_age = 14_000_000_000
#when printing python removes the underscores
print (universie_age)

#Initialising a set of number vaiables with multiple assignment 
x, y, z = 1, 2, 3
print (x,y,z)

#Using capitals to indicate a variable is a contsant 
MAX_CONNECTIONS = 5000
print (MAX_CONNECTIONS)


#The Zen of Python
import this 














