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

# Python always expects the first line after a FOR loop to be indented, but after that it stops looking for indents.
# If you have a multi-line set of instructions for the loop and forget to keep indenting, it will only run those un-
# -indented instructions on the last item in the list, since it will be the last item associated with the temp variable.
# That would be a LOGICAL ERROR. Valid code, but not correctly carrying out your intent.
# Also, Python will not run a FOR loop without the colon (line 18, line 2).

pizzas = ["spartan", "supreme", "canadian bacon"]
for pizza in pizzas:
    print(f"who wants a piece of {pizza.title()} pizza?")
print(f"I like all of these, but {pizzas[2].title()} is my favorite.")