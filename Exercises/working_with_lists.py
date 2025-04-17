# Quesiton 1
# Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ['diavola', 'capriciosa', 'funghi']
for pizza in pizzas:
    print(pizza.title())

# Question 2
# Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
pizzas = ['diavola', 'peperoni', 'funghi', 'capriciosa']
for pizza in pizzas:
    print("My favourite pizza in the world is a ")
    print(pizza.title())

# Question 3
# Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
pizzas = ['capriciosa', 'diavola', 'peperoni', 'margheritta']
print("\n")
for pizza in pizzas:
    print("My preffered pizza is a ")
    print(pizza.title())
print("\nI truly love pizza because I love Italy!")

# Question 4
# Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal
animals = ['dog', 'pony', 'cat', 'fox', 'turtle']
for animal in animals:
    print(animal.title())

# Questions 5
# Modify your program to print a statement about each animal, such as A dog would make a great pet.
animals = ['dog', 'pony', 'cats', 'fox']
for animal in animals:
    print(f'A {animal}, would make a great pet')

# Question 6
# Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
print('\n')
animals = ['dog', 'cat', 'fox', 'pengiun']
for animal in animals:
    print(f'A {animal}, would make a great pet')
print('Any of these animals would make a great pet')


