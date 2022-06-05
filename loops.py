# loops.py -- A program that will show two different types of loops,
# the for-loop and the while-loop.

# First will be the while loop. Simply put, 'while the code hasn't met
# a certain criteria, keep running the code.'

loops = 0
while loops <= 10:
    print(loops)
    loops += 1

# Second is now the for loop. Simply put, 'for every point in the iteration
# do something.'

grocery_list = ('apple', 'banana', 'milk', 'eggs')
print("Your grocery list is:")
for items in grocery_list:
    print(items)
