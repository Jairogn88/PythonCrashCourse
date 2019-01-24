# # Oh no! One person isn't gonna be able to make it to the dinner party!
# Start with  3-4_GuestList.py print a message at the end stating the name who can't make it to dinner.
invited = ['leo', 'dio', 'bruce']

print("Hey " + invited[0].title() + ", you are invited to dinner.")
print("Greetings " + invited[1].title() + ", you are invited to dinner.")
print("Sup " + invited[2].title() + ", you are invited to dinner at my place.")
print("\nUnfortunately, " + invited[1].title() + " won't be able to make to dinner.\n")

# Replace the name of the guest who can't make it with the name of the new person you are inviting.
invited[1] = 'danzig'

# Print a second set of invitation messages, one for each person who is still in your list.
print("Hey " + invited[0].title() + ", you are invited to dinner.")
print("Greetings " + invited[1].title() + ", you are invited to dinner.")
print("Sup " + invited[2].title() + ", you are invited to dinner at my place.")
