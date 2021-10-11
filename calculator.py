# A simple calculator program that does basic arithmetic

def add():
    print("Please choose two numbers to add.")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) + int(num2)
    print(f"{num1} + {num2} = {answer}\n")
    play_again()

def subtract():
    print("Please choose two numbers to subtract.")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) - int(num2)
    print(f"{num1} - {num2} = {answer}\n")
    play_again()

def multiply():
    print("Please choose two numbers to multiply.")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) * int(num2)
    print(f"{num1} * {num2} = {answer}\n")
    play_again()

def divide():
    print("Please choose two numbers to divide.")
    num1 = input("> ")
    num2 = input("> ")
    answer = int(num1) / int(num2)
    print(f"{num1} / {num2} = {answer}\n")
    play_again()

def menu():
    print("*" * 28)
    print("Welcome To Simple Calculator")
    print("*" * 28)
    print("\n")
    print("Please choose an option (1-5).")
    print("-" * 31)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

def play_again():
    print("Would you like to play Simple Calculator again? (Y or N)")
    answer = input("> ")
    while True:
        if answer == 'Y' or answer == 'y':
            main()
        elif answer == 'N' or answer == 'n':
             exit(1)
        else:
            print("Please choose Y or N.")
            answer = input("> ")
        
   

def main():
    menu()
    choice = input("> ")
    while True:
        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            exit(1)
        else:
            print("Please choose an option (1-5).")
            choice = input("> ")
        
        

main()
