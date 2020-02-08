def make_pizza(*toppings):
    ###Prints all requested toppings###
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','creamy garlic sauce')
#Putting the asterisk in front of the parameter lets the function accept an unspecified (and unlimited) number of
#-arguments to the parameter.

def picky_pizza(size, shape, *toppings):
    ###make a pizza with a certain size, shape, and any combination of toppings###
    print(f"\nMaking a {size}-inch {shape} pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
picky_pizza(16, 'square','mushrooms','green peppers','creamy garlic sauce')
#If you want to have multiple parameters, only one can be arbitrary and it must be placed at the end of the list of
#parameters
#!Arbitrary parameters are TUPLES: https://data-flair.training/blogs/python-tuples-vs-lists/

def new_user(username, firstname, lastname, **user_info):
    ###Build a dictionary holding everything we know about a user###
    user_info['username'] = username
    user_info['first_name'] = firstname
    user_info['last_name'] = lastname
    return user_info

user_profile = new_user('OGmurican@gmail.com','James','Madison',profession='writer',pastime='CENSORED')
#Instead of a tuple, this function builds a dictionary and the double-asterisk parameter is a placeholder letting us
#-pass as many key-value pairs into the dictionary as we like after supplying the first 3 parameters.

def car_exercise(manufacturer, model, **attributes):
    attributes['manufacturer'] = manufacturer
    attributes['model'] = model
    return attributes

car_info = car_exercise('Mitsubishi','Mistake',year='2019',engine='untested',safety_rating='lolnope')
