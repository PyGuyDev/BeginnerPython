# variables.py -- A simple program that shows how variables are used
# within Python.

user_name = 'Christopher'  # The value 'Christopher' is assigned to the
# variable 'user_name'.

print(user_name)

# Now, let's do some calculations with variables and subsequent values

num1 = 2
num2 = 3

# An F-string allows integration of data structures inside strings
print(f"{num1} + {num2} is equal to {sum((num1, num2))}.")


# Let's define a function that takes both variables as parameters  # noqa: E302
def print_the_variables(x, y):
    """Function will pass arguments 'x' and 'y' to the print function"""
    print(f"Your first variable is: {x}, and the second is: {y}.")


print_the_variables(num1, num2)


