# Printing a string that uses double-quote marks inside the string
print("\"To be, or not to be! That is the question.\"")


# Printing a string that uses an apostrophe inside the string
print('You can\'t possibly mean that!')


# Printing with whitespace preserved
print("""Mary had a little lamb,
    a little lamb,
        a little lamb. Mary had a little lamb,
            it's fleece was white as snow.""")


# A coded string on multiple lines but printed on a single line
print("""My day started by getting \
out of bed. I then took \
a shower and got dressed afterward.""")

# Creating a string and printing its length using the len() function.
# There are several ways you can do this and I'll demonstrate two of them.
# First path:
string = 'How are you doing today?'
length_of_string = len(string)
print(length_of_string)
# Second path:
print(len('How are you doing today?'))  # More streamlined - 1 line is better than 3.  # noqa: E501


# Concatenating two created strings and printing them.
first_string = 'George'
second_string = 'Washington'
both_strings = first_string + second_string  # I assign the values of first_string and second_string into a new variable.  # noqa: E501
print(both_strings)


# Printing two concatenated strings with an added space in between.
new_string = first_string + " " + second_string
print(new_string)


# Using slice notation, I'll print a portion of a specified string.
string_again = 'Christopher'
print(string_again[0: -6]) # Will print the abbreviated 'Chris'


# Converting a list of strings to lowercase and printing on a separate line.
animals = ('Animals', 'Badger', 'Honey Bee', 'Honey Badger')
for animal in animals: # Loops over the list of animals
    print(animal.lower())


# Converting the same list of strings to uppercase.
for animal in animals:
    print(animal.upper())


# Removing whitespace from three different strings.
string1 = '   Hello'
string2 = 'Hello   '
string3 = '   Hello   '

print(string1.lstrip()) # Removes whitespace from the left
print(string2.rstrip()) # Removes whitespace from the right
print(string3.strip()) # Removes all whitespace from the string


# Printing out the results of using the .startswith() function on strings
strings = ('Apples', 'Oranges', 'vegetables', 'aNimals')
for string in strings:
    print(string.startswith('Or'))


# Using the list of strings below, alter them so .startswith('be') will equal to TRUE.  # noqa: E501
more_strings = ('Becomes', 'becomes', 'BEAR', '  bEautiful')
for string in more_strings:
    lower_list = []
    lower_list.append(string.lower())
    for items in lower_list:
        strip_list = []
        strip_list.append(items.strip())
        for items in strip_list:
            print(items.startswith('be'))


# Taking input from user and printing result.
user_input = input("Please type something -> ")
print(user_input)


# Taking input from user and printing it in lowercase.
user_input = input("Please type something -> ")
print(user_input.lower())


# Taking input from user and printing the number of characters typed.
user_input = input("Pleae type something -> ")
print(len(user_input))


# Creating a string with an integer, converting it to an actual integer object using the int() function. Then test the new object by multiplying it by another number and displaying the result.  # noqa: E501
string = '4'
print(int(string) * 4)


# Another example of the previous example, however using the float() function instead.  # noqa: E501
string = '4.321'
print(float(string) * 2)


# Creating a string object and an integer object. Display both objects side by side using the str() function.  # noqa: E501
string = '4'
number = 0
print("My age is " + string + str(number))


# Using input() twice to get two different numbers, multiply them and display the result as a floating point number.  # noqa: E501
num1 = input("First number: ")
num2 = input("Second number: ")
print("The product of " + num1 + " and " + num2 + " is " + str(float(num1) * float(num2)))  # noqa: E501


# Two examples of string interpolation. One example is through concatenation.
name = 'Christopher'
age = '40'
height = '72'
print("My name is " + name + ", I'm " + age + " years old and I am " + height + " inches tall.")  # noqa: E501

# The second example is by using 'f-strings'.
print(f"My name is {name}, I'm {age} years old and I am {height} inches tall.")

# Three different string literals.
weight = 0.2
animal = 'newt'

print(str(weight) + " is the weight of the " + animal + ".")  # String Concatenation  # noqa: E501
print("{} is the weight of the {}.".format(str(weight), animal))  # Using the .format() function  # noqa: E501
print(f"{weight} is the weight of the {animal}.")  # Using f-strings


# Finding a string within a string using the .find() function
string = "My name is Christopher."
print(string.find('Christopher'))


# The result of trying to find the substring 'a' in the string 'AAA.'
print(('AAA').find('a'))


# Replacing 's' with the letter 'x'
print(("Somebody said something to Samantha").replace('s', 'x'))


# Getting input with the input() function and trying to .find() a particular letter.  # noqa: E501
user_input = input("Please type something: ")
print(user_input.find('i')) # Will find the first occurence of the letter and print its index position within the string. Strings are ordered lists.  # noqa: E501
