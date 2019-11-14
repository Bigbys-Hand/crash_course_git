magicians = ['zanzibar', 'balthazar', 'harry dresden', "Tuk'tuk"]
for magician in magicians:
    print(magician.title())

# First we define a list
# Then we define a FOR loop
# -The FOR loop tells Python to pull an item from the list 'magicians' and assign it to a variable 'magician'
# Finally, we print the name assigned to 'magician' and titlecase it.
# The FOR loop sees no more instructions and checks the list. It sees another item after the first one. Rinse, repeat.
# When it finds no more items for its instructions to work with, the program simply ends.
# It can be read as "For every magician in the list called 'magicians', print and titlecase their name"
# Sticking to the plural-singular naming convention for the list and temp variable is best practice.
# Magicians-Magician, Cats-Cat, Dogs-Dog, etc.
# Now things get fun. Every indented line after the FOR is inside the loop, so you can stack up lots of instructions.


magicians = ['zanzibar', 'balthazar', 'harry dresden', "Tuk'tuk"]
for magician in magicians:
    print(f"Well done, {magician.title()}, you've saved the day again!")
    print(f"{magician.title()}, wait, where did that rabbit go?")
print("Thank you all for your hard work")
