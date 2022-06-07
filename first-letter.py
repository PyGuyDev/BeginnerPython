# first-letter.py --> A program that will prompt the user for a password, determine the first letter of the input, capitalize it and the display it back.  # noqa: E501

user_input = input("Please enter your password: ")
print("The first letter of your password is " + user_input[0].upper())
