# A function called cube() that takes one parameter and returns the value of that number raised to the third power.  # noqa: E501
def cube(number):
    """A function that takes one parameter 'number' and will return the cube of that number."""  # noqa: E501
    return number ** 3


print(cube(4))  # Prints the value of '4' cubed
print(cube(3))  # Prints the value of '3' cubed


def greet(name):
    """A function that takes one parameter 'name' and will return a print statement that says, 'Hello' and the value of 'name'."""  # noqa: E501
    print(f"Hello {name}!")


greet('Christopher')  # Prints 'Hello Christoher!'
greet('William')  # Prints 'Hello William'


# A for loop that prints out integers, each on a new line
for n in range(0, 11):
    print(n)

# A while loop that prints out integers, each on a new line
n = 0  # Start with a value of 0
while n <= 10:  # While n <= 10, print the value of n
    print(n)
    n += 1  # Must increment by 1 each iteration


def doubles(num):
    """A function that takes a number value and doubles that value each time."""  # noqa: E501
    i = 1  # The number will be doubled 5 times
    while i <= 5:
        double = num * 2
        print(double)
        num = num * 2
        i += 1


doubles(2)
