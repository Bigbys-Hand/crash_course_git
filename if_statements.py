# LETS GET IFFY!!!!
car = 'beamer'
car == 'beamer'
# True
car == 'audi'
# False
car == 'Beamer'
# False. Case matters unless you say it doesn't
car.title() == 'Beamer'
# True. You can pass methods on the variable being evaluated to change it so that it matches the value being checked.

car != 'Beamer'
# True. != works in Python as it does in SQL

age = 31
age == 31
# True. Numbers are treated the same.
42 > age
# True. Mathematical operators work for these conditional tests.

age_2 = 19
(age < 42) and (age > age_2)
# True. You can test multiple conditions, and/or work for these. Parentheses improve readability

toppings = ['mozzerella', 'pepperoni', 'linguica', 'black olives', 'pineapple', 'canadian bacon', 'tomato sauce']
'white sauce' in toppings
# False. See how the 'in' is orange in the editor so you know it is the conditional test?
'tomato sauce' in toppings
# True
'white sauce' not in toppings
# True

age = 31
if age >= 19:
    print("Congratulations! You are old enough to vote.")
else:
    print("Sorry, you are not old enough to vote yet.")
print("Who are you rooting for?")
# If statements will always ignore the indented code if the statement is false.
# In this case, the program will always print "Who are you rooting for?". It will print 35 or 37 depending on the test.

age = 31
if age <= 18:
    print("Sorry, you are not old enough to vote yet.")
elif age >= 19:
    print("Congratulations! You are old enough to vote.")
elif age >= 65:
    print("I hope you have been voting.")
# Elif is the hot new 'elseif'. It is another 'if' test that only runs if the previous test fails.
# This program will always return the second line, because Python stops the elif chain after the first successful test.
# Thus, laying out tests in a logical order is very important!

age = 99
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 15
elif age < 25:
    ticket_price = 24
elif age < 65:
    ticket_price = 20
print(f"Your total comes to ${ticket_price}.")
# You do not need to include an 'else' and can simply keep stacking 'elif' blocks to account for all conditions.
# You can also stack 'if' blocks in case multiple conditions could be true, Python will evaluate each in turn.

toppings = ['mozzerella', 'pepperoni', 'linguica', 'black olives', 'pineapple', 'canadian bacon', 'tomato sauce']
odd_toppings = ['french fries', 'gravy', 'another pizza lol', 'pineapple']
if toppings:
    for topping in toppings:
        if topping == 'black olives':
            print(f"Sorry, we are out of {topping.title()}")
        else:
            print(f"Adding your requested topping of {topping.title()}")
    for odd_topping in odd_toppings:
        if odd_topping in toppings:
            print(f"Adding your requested topping of {odd_topping.title()}")
        else:
            print(f"Sorry, we don't carry {odd_topping.title()}")
    print("Your pizza is ready!")
else:
    print("Are you sure you don't want any toppings?")



if age < 2:
    print("Status: baby")
elif 4 > age >= 2:
    print("Status: toddler")
elif 13 > age >= 4:
    print("Status: kid")
elif 20 > age >= 13:
    print("Status: teenager")
elif 65 > age >= 20:
    print("adult")
elif age > 65:
    print("elder")

