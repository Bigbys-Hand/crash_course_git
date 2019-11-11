# electric_cars = ['tesla', 'bolt', 'leaf', 'aspark owl']
# print(electric_cars)
#
# electric_cars[0] = 'roadster'
# print(electric_cars)
# # Use the numerical select to adjust values based on what place in the list they occupy
#
# electric_cars.append('Rimac Concept One')
# print(electric_cars)
#
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('ducati')
# motorcycles.append('suzuki')
# print(motorcycles)
#
# motorcycles.insert(3, 'yamaha')
# print(motorcycles)
#
# first_owned = motorcycles.pop(2)
# print(f"The first motorcycle I owned was a {first_owned.title()}")
# print(motorcycles)
# # pop is used to pull out a value based on position and then use it elsewhere.
# # pop pulls the string out of its list, but it does not put that string into a new list.
#
# del motorcycles[1]
# print(motorcycles)
#
# motorcycles.remove('yamaha')
# print(motorcycles)
# # del and remove both completely remove a value from the list. Del does so by position, remove by value
# # Remove only pulls out the first instance of the value. If there could be dupes, loop the remove function
#
# motorcycles.append('Bughatti Chiron')
# print(motorcycles)
#
# too_expensive = 'Bughatti Chiron'
# motorcycles.remove(too_expensive)
# print(motorcycles)
#
# keeper = motorcycles.pop(0)
# # to references 'Honda' as I want to below, I have to pull it out of the list.
# print(f"\n A {too_expensive} was too expensive, I will keep my {keeper.title()}")
# commented out above exercises to reduce output, continuing on page 43

sedans = ['bmw', 'audi', 'toyota', 'subaru']
print(sedans)
sedans.sort()
print(sedans)
# sort is permanent!
sedans.sort(reverse=True)
print(sedans)
# but there is a reverse sort, also permanent

trucks = ['F-150', 'Tundra', 'Hemi', 'Raptor']
print(trucks)
# if you fear sort commitment, use sorted()
print(sorted(trucks))
print(trucks)
# you can also simply .reverse() things. This ignores alphabetical order.
# also permanent!!
trucks.reverse()
print(trucks)
# Hey, how long is your list? len() will show the way
# Notice how len() and sorted() are both wrapped in print, while .reverse() is called separately.
# len() and sorted() are FUNCTIONS, .reverse() is a METHOD.
print(len(trucks))
# Notice how len() counts from 1, not from 0. This is simply to make it more human-readable.
# If your list has a len() count of 4, the 4th item has an index # of 3 if you wish to call for it specifically in a
# print cmd.