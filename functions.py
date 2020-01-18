def greet_nerds():
    """Display a simple greeting""" 
    print("Live long and prosper")

def better_greeting(username):
    """Display a simple greeting, pass name to function"""
    print(f"Live long and prosper, {username.title()}!")
#This function is similar to the first one, but we created the PARAMETER 'username' so we could pass a name value to it as an ARGUMENT. 
#The PARAMETER is 'username', the ARGUMENT could be any name - samuel, rebeka, etc. 

def display_message():
    """Prints a formatted block of text summarizing what I've learned from chapter 8."""
    print("This function is similar to the first one, but we created the PARAMETER 'username' so we could pass a name value to it as an ARGUMENT. \nThe PARAMETER is 'username', the ARGUMENT could be any name - samuel, rebeka, etc.")
    
def favorite_book(book_title):
    """Accepts one parameter, 'book_title'. Prints a message declaring the argument to be your favorite book."""
    print(f"{book_title.title()} is my favorite book!")

#You can pass arguments to parameters in a number of way. 
#A function definition may have multiple parameters, so a function call may need multiple arguments.
#POSITIONAL ARGUMENTS: Match each argument to parameter by the order in which the arguments are provided.

def describe_kitty(kitty_name, kitty_size, kitty_color):
    """Displays information about a pet cat. Name, size, color."""
    print(f"\nI have a cat named {kitty_name.title()}.")
    print(f"This is a {kitty_size} cat. Fur color is {kitty_color}.")
    
describe_kitty('snow','small','ashy brown and white')
    
#You can work with as many positional arguments as you like! Just don't forget their order.

#KEYWORD ARGUMENTS: Name-value pair you pass to a function. Name and value are associated within the argument.
#Thus you can't put arguments in the wrong order. 
#The function is written the same! You just name each parameter explicitly when passing your arguments:

describe_kitty(kitty_name='snow',kitty_color='ashy gray with white coat',kitty_size='small')

#DEFAULT VALUES: An argumment for a parameter provided in the function call.
#Note that order still matters, and you can overwrite a default argument by entering that argument with a new value when you call the function.
#Order is important, default parameters should always be last so you can enter new values for them only when needed.

def describe_doggo(doggo_name, doggo_breed, doggo_good='GOOD BOY'):
    """Display factual and unbiased information about a dog."""
    print(f"My dog's name is {doggo_name.title()}")
    print(f"This dog is a {doggo_breed.title()} and a very {doggo_good}!")

describe_doggo('Obby','bird dog mutt')
describe_doggo('Obby','bird dog mutt','okay boy')
#If you specify name-value parts when calling a function, you can enter them in any order.
describe_doggo(doggo_breed='corgi',doggo_good='VERY GOOD BOY',doggo_name='Zeke')
