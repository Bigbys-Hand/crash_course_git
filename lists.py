bicycles = ['trek', 'cannondale', 'specialized', "whatever it was Eval Knievel's mom rode", 'redline']
print(bicycles)
print(bicycles[0].upper())
# The first item in a list is always at 0, not at 1
# You can run methods on list print commands! Fancy.
print(bicycles[-1])
# negative values let you select from right to left. There is no -0!
print(bicycles[3])
# 4th value is pulled
boast = f"I am, in fact, partial to {bicycles[-1]} bicycles."
print(boast)
