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

