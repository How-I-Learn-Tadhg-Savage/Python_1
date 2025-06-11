# Making a list of cars
cars = ['jagur','mercedes', 'bmw', 'audi']
# Permanently sorting in alphabetical order
cars.sort()
# Creating a for loop
for car in cars:
    # Usining our if statemtn to treat BMW differently
    if car == 'bmw':
        print (car.upper())
    # All others get put to tittle instead of upper by using the else statement
    else:
        print(car.title())

# Set the value of car equal to 'audi'
car = 'audi'
# Is the value of car equal to 'Audi'?
car == 'Audi'
# Case sensitivity matter to change variable to title
car.title() == 'Audi'

# Checking for inequality 
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
else:
    print('Use anchovies')

# Numerical comparison 
age = 22
if age >= 18:
    print('True')



