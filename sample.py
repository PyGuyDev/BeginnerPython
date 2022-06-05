# sample.py -- A program that covers the use of comments, variables, functions, if-else statements and the while-loop. # noqa: E501
def greeting():
    name = input("What is your name: ")
    return name

def add():
    """The addition function"""
    print("Please choose two numbers:")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) + int(num2)
    print(f"{num1} + {num2} is equal to {answer}.")
    print("Would you like to continue? (Y / N)")
    choice = input("> ")
    if choice.lower() == 'y':
        add()
    elif choice.lower() == 'n':
        math()
    else:
        print("Please enter a valid option.")

def subtract():
    """The subtraction function"""
    print("Please choose two numbers:")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) - int(num2)
    print(f"{num1} - {num2} is equal to {answer}.")
    print("Would you like to continue? (Y / N)")
    choice = input("> ")
    if choice.lower() == 'y':
        subtract()
    elif choice.lower() == 'n':
        math()
    else:
        print("Please enter a valid option.")

def multiply():
    """The multiplication function"""
    print("Please choose two numbers:")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) * int(num2)
    print(f"{num1} * {num2} is equal to {answer}.")
    print("Would you like to continue? (Y / N)")
    choice = input("> ")
    if choice.lower() == 'y':
        multiply()
    elif choice.lower() == 'n':
        math()
    else:
        print("Please enter a valid option.")

def divide():
    """The division function"""
    print("Please choose two numbers:")
    num1 = input("> ")
    num2 = input("> ")
    answer = float(num1) / float(num2)
    print(f"{num1} + {num2} is equal to {answer}.")
    print("Would you like to continue? (Y / N)")
    choice = input("> ")
    if choice.lower() == 'y':
        divide()
    elif choice.lower() == 'n':
        math()
    else:
        print("Please enter a valid option.")

def math():
    """The arithmetic portion of the program"""

    print("Please choose an option below:")
    print("*" * 30)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")


    option = input("> ")
    if option == '1' or option.lower() == 'add':
        add()
    elif option == '2' or option.lower() == 'subtract':
        subtract()
    elif option == '3' or option.lower() == 'multiply':
        multiply()
    elif option == '4' or option.lower() == 'divide':
        divide()
    elif option == '5' or option.lower() == 'quit':
        exit(0)
    else:
        print("Please enter a valid response!")
        math()

user_name = greeting()

print(f"Welcome {user_name}!")

while True:
    print("Would you like to do some math? (Y / N)")
    choice = input("> ")

    if choice.lower() == 'y' or choice.lower() == 'yes':
        math()
    elif choice.lower() == 'n' or choice.lower() == 'no':
        exit(0)
    else:
        print("Please enter a valid option.")

