# Creating a list of bicycles and printing 
bicycles = ['trek', 'cannondale', 'dawes', 'specialized']
print (bicycles)

# Accessing the first element in the list
print (bicycles[0])

# Using a method to make the format more presentable
print (bicycles[0].title())

# Accesaing the last element in a list using -1
print (bicycles[-1].title())

# Accessing the second last and third last elements from a list
print (bicycles[-2].title())
print (bicycles[-3].title())

# Using individual intems from a list in a message
bicycles = ['trek','cannondale', 'dawes', 'specialized']
message = f"My first bike was a {bicycles[2].title()}, it was also my favourite."
print (message)

# Modifying Elements in a List
motorcycles = ['honda', 'ducati', 'yamaha', 'suzuki']
print (motorcycles)
motorcycles[1] = 'bmw'
print (motorcycles)

# Adding Elements to a List
# Using append to add new motorcycles to a list
motorcycles = ['honda', 'ducati', 'suzuki', 'yamaha']
print (motorcycles)
motorcycles.append('bmw')
print (motorcycles)

# Starting with an empty list and adding elements 
motorcycles = []
print (motorcycles)
# Appending 4 new elements to the list
motorcycles.append('bmw')
motorcycles.append('ducati')
motorcycles.append('yamaha')
motorcycles.append('honda')
# Printing newly formed list
print (motorcycles)

# Inserting Elements into a List
motorcycles = ['yamaha', 'honda', 'bmw']
motorcycles.insert(0, 'ducati')
print (motorcycles)

# Removing Elements from a List
motorcycles = ['yamaha', 'honda', 'bmw']
print (motorcycles)
# Removing using del statement
del motorcycles[0]
print (motorcycles)
# Removing bmw using del statement
del motorcycles[1]
print (motorcycles)

# Using the pop method to remove items from a list
motorcycles = ['honda', 'yamaha', 'bmw', 'ducati']
print (motorcycles)
popped_motorcycle = motorcycles.pop()
# Printing the popped motorcycle showing that its value was not lost and instead reassigned
print (popped_motorcycle)

# Printing my last owned motorbike using f strings and the popped method 
motorcycles = ['ducati', 'honda', 'bmw', 'yamaha']
last_owned = motorcycles.pop()
message = f"My last owned motorbike was a {last_owned.title()}."
print (message)

# Popping Items from Any Position in a List
motorcycles = ['ducati', 'honda', 'bmw', 'yamaha']
first_owned = motorcycles.pop(0)
# Using it to write a message concatenated with an f string
message = f"My first motorbike was a {first_owned.title()}"
print (message)

# Removing an Item by Value
motorcycles = ['ducati', 'honda', 'bmw', 'yamaha']
motorcycles.remove('yamaha')
print (motorcycles)

# Using the removed value to print a statement
motorcycles = ['yamaha', 'bmw', 'honda', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (f"\nA {too_expensive.title()}, is too expensive.")
# Remove method only deleted the one occurance in a list not all

# Organising a list 
cars = ['bmw', 'audi', 'jaguar', 'mercedes', 'ford']
# Permanently changing the order of a list
cars.sort()
print (cars)
# Reverse alphabetial order can also be achieved by passing the argument reverse=True to the sort method
cars = ['bmw', 'audi', 'jaguar', 'mercedes', 'ford']
cars.sort(reverse=True)
print (cars)
# In both cases the order of the lists have been permanently changed

# Sorting a List Temporarily with the sorted() Function
# This maintains the original order but presents in a sorted order
# This can be achieved by using the sorted function
# Defining a list of cars
cars = ['bmw', 'audi', 'subaru', 'mercedes']
# Printing the orginal list
print ('Here is the original list:')
print (cars)
#Printing the sorted list
print ('\nHere is the sorted list:')
print (sorted(cars))
#printing again the original list of cars
print ('\nHere again is the original list:')
print (cars)

# The sorted function can also accept a revers=True argument 
print ('\nHere is the list sorted in reverse alphabetical order:')
print (sorted(cars, reverse = True))

# Printing a List in Reverse Order using reverse method 
cars = ['bugatti', 'audi', 'mercedes', 'bmw']
print (cars)
# This reverse method will permanently reverse the order of the list of cars
cars.reverse()
print (cars)
# The order of the list can be reverted back by again using the reverse method
cars.reverse()
print (cars)

# Finding the Length of a List
cars = ['bwm', 'audi', 'mercedes', 'bugatti']
# Note, Python counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors
print (len(cars))










