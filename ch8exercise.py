# Conditional logic examples below

print(1 <= 1)  # Evaluates to TRUE
print(1 != 1)  # Evaluates to FALSE
print(1 != 2)  # Evaluates to TRUE
print('good' != 'bad')  # Evaluates to TRUE
print('good' != 'Good')  # Evaluates to TRUE
print(123 == '123')  # Evaluates to FALSE

print(('A' != 'A') and not False)  # Evaluates to FALSE * Complex conditional logic  # noqa: E501

print((1 <= 1) and (1 != 1))  # Evaluates to FALSE
print(not (1 != 2))  # Evaluates to FALSE
print(('good' != 'bad') or False)  # Evaluates to TRUE
print(('good' != 'Good') and not (1 == 1))  # Evaluates to FALSE


# Control flow with IF/ELSE statements

def get_user_input_length(user_input):
    """ A function that takes one paramater -- a string -- and compares the length of the string to a set number. Will print out string comparison results."""  # noqa: E501
    set_of_characters = 5
    if len(user_input) == set_of_characters:
        print(f"Your input is {set_of_characters} characters long")
    elif len(user_input) < set_of_characters:
        print(f"Your input is less than {set_of_characters} characters long")
    else:
        print(f"Your input is greater than {set_of_characters} characters long")  # noqa: E501


user_input = input('Please enter a word: ')
get_user_input_length(user_input)

# A change
