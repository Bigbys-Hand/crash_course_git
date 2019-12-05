# Making different Thargoids for a space shooter
thargoids = []

# Make 30 minor Thargoids
for spawn_number in range(30):
    new_thargoid = {'color': 'yellow', 'speed': 'fast', 'hp': '100', 'range': 'short', 'damage': 'minor'}
    thargoids.append(new_thargoid)

# Show the first 5 Thargoids
for thargoid in thargoids[:5]:
    print(thargoid)
print('...')

# Show how many Thargoids have been created
print(f"The total number of Thargoids: {len(thargoids)}. Types are {new_thargoid['color']}")

# Even though every 'new_thargoid' dictionary object in the 'thargoids' list is identical, Python tracks them
# individually. This lets us modify batches of them via slices.

for thargoid in thargoids[:4]:
    if thargoid['color'] == 'yellow':
        thargoid['color'] = 'white'
        thargoid['speed'] = 'moderate'
        thargoid['hp'] = 175
        thargoid['range'] = 'long'
        thargoid['damage'] = 'strong'

for thargoid in thargoids[:5]:
    print(thargoid)
print('...')

pets = []

dog = {
   'name': 'Obby',
    'human': 'Heidi',
    'type': 'dog',
    'age': 4
}
pets.append(dog)

cat = {
    'name': 'Snow',
    'human': 'Jim',
    'type': 'cat',
    'age': 5
}
pets.append(cat)

rat_dog = {
    'name': 'Cookie',
    'human': 'Gavin',
    'type': 'rat-dog',
    'age': 14
}
pets.append(rat_dog)

for pet in pets:
    print(f"{pet['name']} is a {pet['type']} of age {pet['age']}")
