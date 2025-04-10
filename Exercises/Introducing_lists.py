# Question 1
#Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ['ben', 'harry', 'john', 'oliver']
print (names[0].title())
print (names[1].title())
print (names[2].title())

# Question 2
# Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
names = ['ben', 'harry', 'john', 'oliver']
print (f'Hello, {names[0].title()}, welcome.')
print (f'Hello, {names[1].title()}, welcome.')
print (f'Hello, {names[2].title()}, welcome.')

# Question 3
# Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
cars = ['bugatti', 'honda', 'bmw', 'mercedes', 'jaguar']
message_1 = (f'I would like to own a {cars[-1].title()}.')
message_2 = (f'I would not like to own a {cars[1].title()}.')
print (message_1)
print (message_2)

# Question 4
# Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
dinner_guests = ['harry', 'john', 'alfred']
invite_message_1 = (f'Hi, {dinner_guests[0].title()}, please come to dinner.')
invite_message_2 = (f'Hi, {dinner_guests[1].title()}, please come to dinner.')
invite_message_3 = (f'Hi, {dinner_guests[2].title()}, please come to dinner.')

print (invite_message_1)
print (invite_message_2)
print (invite_message_3)

# Question 5 
# Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
print (f'unfortunately, {dinner_guests[0]}, cannot make it.')

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
dinner_guests[0] = 'anthony'

# Print a second set of invitation messages, one for each person who is still in your list.
invite_message_1 = (f'Hi, {dinner_guests[0].title()}, please come to dinner.')
invite_message_2 = (f'Hi, {dinner_guests[1].title()}, please come to dinner.')
invite_message_3 = (f'Hi, {dinner_guests[2].title()}, please come to dinner.')
print (invite_message_1)
print (invite_message_2)
print (invite_message_3)

# Question 6
# More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
print (f'Hi, {dinner_guests[0].title()}, we have now found a bigger table.')
print (f'Hi, {dinner_guests[1].title()}, we have now found a bigger table.')
print (f'Hi, {dinner_guests[2].title()}, we have now found a bigger table.')

# Use insert() to add one new guest to the beginning of your list.
dinner_guests.insert(0, 'toby')
# Use insert() to add one new guest to the middle of your list.
dinner_guests.insert(1, 'kay')
# Use append() to add one new guest to the end of your list.
dinner_guests.append('lizzie')

# Print a new set of invitation messages, one for each person in your list.
print (f'Hello, {dinner_guests[0]}, please come to dinner.')
print (f'Hello, {dinner_guests[1]}, please come to dinner.')
print (f'Hello, {dinner_guests[2]}, please come to dinner.')
print (f'Hello, {dinner_guests[3]}, please come to dinner.')
print (f'Hello, {dinner_guests[4]}, please come to dinner.')
print (f'Hello, {dinner_guests[5]}, please come to dinner.')

# Question 7
# Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
print ('Appologies, only two guests can now come to dinner.')

# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
popped_guest = dinner_guests.pop()
print (f'sorry, {popped_guest.title()}, you have been disinvited.')

popped_guest = dinner_guests.pop()
print (f'Sorry, {popped_guest.title()}, you have been disinvited.')

popped_guest = dinner_guests.pop()
print (f'Sorry, {popped_guest.title()}, you have been disinvited.')

popped_guest = dinner_guests.pop()
print (f'Sorry {popped_guest.title()}, you have been disinvited.')

# Print a message to each of the two people still on your list, letting them know they’re still invited.
print (f"Hi, {dinner_guests[0].title()}, please remeber you're still invited")
print (f"Hi, {dinner_guests[1].title()}, pleaee remever you're still invited.")

# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del dinner_guests[1]
del dinner_guests[0]
print (dinner_guests)

# Question 8
# Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
locations = ['valletta', 'milan', 'rome', 'london', 'dublin', 'riyadh']

# Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
print (locations)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print (sorted(locations))

# Show that your list is still in its original order by printing it.
print (locations)

# Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print (sorted(locations, reverse = True))

# Show that your list is still in its original order by printing it again.
print (locations)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
locations.reverse()
print (locations)

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
locations.reverse()
print (locations)

# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
locations.sort()
print (locations)

# Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
locations.sort(reverse = True)
print (locations)

# Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.
print (len(dinner_guests))






