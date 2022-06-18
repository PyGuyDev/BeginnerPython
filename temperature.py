# temperature.py --> A program that converts temperatures of celsius and fahrenheit respectively to their opposites.  # noqa: E501

def convert_cel_to_far(temp):
    """ This function takes one user inputed floating paramater and converts from degrees of celsius to fahrenheit."""  # noqa: E501
    return (temp * (9/5)) + 32

def convert_far_to_cel(temp):
    """ This function takes one user inputed floating parameter and converts from degrees fahrenheit to celsius."""  # noqa: E501
    return (temp - 32) * (5/9)


user_celsius = input("Please enter a temperature in degrees C: ")
print(f"{user_celsius} degrees C = {convert_cel_to_far(float(user_celsius)):.1f} degrees F")  # noqa: E501

user_fahrenheit = input("Please enter a temperature in degrees F: ")
print(f"{user_fahrenheit} degrees F = {convert_far_to_cel(float(user_fahrenheit)):.1f} degrees C")  # noqa: E501
