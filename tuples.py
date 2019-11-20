# Tuples are exactly like lists except their values cannot be modified. Written with (), not []
first_tuple = (200, 50)
print(first_tuple[0])
print(first_tuple[1])

# first_tuple[0] = 250
# Trying to change a value in a tuple results in an error.

# The way to change a tuple is to assign a new value to the variable representing the tuple
print("First numbers")
print(first_tuple)
first_tuple = (400, 150)
print("New numbers")
print(first_tuple)
