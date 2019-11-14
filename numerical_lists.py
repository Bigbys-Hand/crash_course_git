for value in range(1, 5):
    print(value)
# range() starts counting from the first value provided and stops at (not with) the last value.
for value in range(2):
    print(value)
# unless you give two values, range() assumes the count starts at zero and stops at (not with) the provided number.

numbers = list(range(10))
print(numbers)
# Feed a range into a list!
tricknumbers = list(range(1, 11, 2))
print(tricknumbers)
# Two things shown here: First, a third value is used by range() as a step size. 2 = every second number is skipped.
# Second, since every second number is skipped and the range ends on an odd number, we don't see 10 as we would
# without the step value.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# Math! First, we make an empty list called 'squares' Next, we make a FOR loop running every number in a range(1,
# 11) through the "value" temp variable.
# Each "value" is squared. ** means an exponential equation, so ** 2 means 'raise to the second power'. Then, another-
# -variable named "square" takes the result of "value" ** 2.
# Finally, the "square" variable is appended to the "squares" list. Remember, .appEND() means it goes to the END.
squares = []
for value in range(1, 11):
    squares.append((value ** 2))
print(squares)
# Same code but better. Simple is better than complex. Sparse is better than dense. Readability counts!
# The first version is much easier to read (especially while learning), the second version is less complicated.
big_numbers = []
for number in range(1, 1000000):
    big_numbers.append(number)
print(sum(big_numbers))

for value in range(1,20,2):
    print(value)

multiples = [value ** 3 for value in range(1,11)]
print(multiples)