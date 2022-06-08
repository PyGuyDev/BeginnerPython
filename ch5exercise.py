# Two variables, num1 and num2. Both variables will be assigned the same integer literal (the value) but one will be written with underscores and the other without. Both will be printed on two separate lines.  # noqa: E501
num1 = 5_000_000
num2 = 5000000
print(num1)
print(num2)


# Assigning a floating-point value to the variable num using E notation and then printing it.  # noqa: E501
num = 175e3
print(num) # Will print 175,000.0


# Getting user input and then displaying that number rounded to two decimal places.  # noqa: E501
number = input("Enter a number: ")
print(f'{number} rounded to 2 decimal places is {round(float(number), 2)}')


# Getting user input and then displaying the numbers absolute value.
number = input("Enter a number: ")
print(f'The absolute value of {number} is {abs(float(number))}')


# Getting user input for two variables. Will display the difference of those two numbers is an integer.  # noqa: E501
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
difference = float(num1) - float(num2)
print(difference)
print(f"The difference between {num1} and {num2} is an integer? {difference.is_integer()}")  # noqa: E501


# Printing the result of a number raised to a fixed-point power with three decimal places.  # noqa: E501
num = 3
print(f"{num ** .234:.3f}")


# Print a number as currency with thousands grouped with commas and displayed with two decimal places.  # noqa: E501
num = 4000
print(f"${num:,.2f}")


# Printing the result of a fraction as a percentage with no decimal places.
num = 2 / 10
print(f"{num:.0%}")



