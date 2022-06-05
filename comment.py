# comment.py -- A python file that showcases my understanding of
# comment usage. Comments are ignored by the interpreter and are solely
# meant to help others understand your code.

"""This is another way to comment in Python. This style is used more for
   docstrings for defined functions in your code."""

# The following code will run a small program of adding two numbers
# that the user chooses:

def greeting(user_name):
    """This function will return a simple greeting."""
    print(f"Hello, {user_name}")

def add_two_numbers(x, y):
    """This function will take two arguments (x and y), add them and
       then return the result."""
    return x + y

print('*' * 30)
user_name = input("Welcome ???, what is your name? ")
greeting(user_name)
print("Which two numbers would you like to add?")
first_choice = input("> ")
second_choice = input("> ")
print(f"Alright {user_name}, {first_choice} + {second_choice} is {add_two_numbers(int(first_choice), int(second_choice))}")  # noqa: E501
