person = {'eyes': 'green', 'hair': 'red', 'sex': 'female', 'age': 37, 'superpower': 'telekinesis',
          'first_name': 'Jean', 'last_name': 'Gray', 'city': 'Boston'}

user_0 = {
    'username': 'jgraytk',
    'firstname': 'jean',
    'lastname': 'gray'
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")
# The .items() method loops through the dictionary and prints out all keys and values.
# 'Key' and 'Value' are placeholders the .items() method needs to operate.

for stored_things in person.keys():
    print(stored_things.title())
# The .keys() method prints each key value, and has a nice eponymous name.

friends_favorite_drinks = {
    'Mike': 'Old-fashioned',
    'Kyle': 'Butterbeer',
    'Dom': 'Pan-Galactic Gargle Blaster',
    'Gavin': 'Peanut Butter Stout',
    'Paul': 'Orange Juice',
    'Alex': 'Cabernet',
    'Nikki': 'Barbera'
}

wine_friends = ['Alex', 'Nikki']
for name in sorted(friends_favorite_drinks.keys()):
    print(name)

    if name in wine_friends:
        drink = friends_favorite_drinks[name]
        print(f"\t{name}, I see you love {drink}!")
    else:
        print(f"\t{name}, looks like you prefer beer over wine.")
# Since the .keys() method returns every key in a dictionary, rather than just looping through them, it is great for
# jobs like these where you want to see all keys and check their values too.
# The sorted() method puts keys in alpha order.

print("The following libations have been listed:")
for libation in friends_favorite_drinks.values():
    print(libation)
# There is also a .values() method to return values instead of keys!
print("The following libations have been listed:")
for libation in set(friends_favorite_drinks.values()):
    print(libation)
# Use the set() function when you suspect some values will be repeated and want to return only unique values.


python_glossary = {
    'method': 'Similar to a function, but associated with objects/classes. Methods are implicitly used with an object '
              'when called.',
    'function': 'A block of code to carry out a specific task. Looks like function().',
    'pop_method': 'Removes the last item from a list, but lets you work with the item after removing it.',
    'tuple': 'Similar to a list but with parentheses instead of brackets. Unlike lists, their values cannot be changed.'
                'should be used when you need to store data that will not be changed through the life of a program.',
    'slice': 'A specific group of items from a list, pulled into a separate mini-list as part of a program.',
    'range_function': 'a function used to generate series of numbers. Read the documentation!',
    'looping': 'a common method of carrying out the same action(s) on every item in a list/dictionary',
    'nesting': 'Stick multiple dictionaries in a list; stick a list of items in a dictionary as a value; '
                'store a dictionary as a value inside another dictionary.'
}
