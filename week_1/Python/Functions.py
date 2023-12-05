# Reversing a list 
sample_text = 'Hello World'
sample_list = [1,2,3,4,5]
reversed_list = []

# Example 1, using a while loop. Not mutating original list:
ints = len(sample_list) - 1 
while ints >= 0:
    reversed_list.append(sample_list[ints])
    ints = ints - 1
print(sample_list, reversed_list)

# Example 2, also using a while loop. Mutating list:
while len(sample_list) > 0:
    integer = sample_list.pop()
    reversed_list.append(integer)
print(sample_list,reversed_list)

# Reverse a list using slice. The number indicates how many you want to go back at a time, in this case 1:
print(sample_list[::-1])

# Reverse a string using slice:
print(sample_text[::-1])

# Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

for int_value in range(1,101):
    if int_value % 15 == 0:
        print('FizzBuzz')
    elif int_value % 5 == 0:
        print('Buzz')
    elif int_value % 3 == 0:
        print('Fizz')
    else:
        print(int_value)

# What is a function? A function is a reuseable block of code that can be called any time. In order to call a function in python, we need to start with def. def just stands for definition. The user will need to pass in a parameter. See example below:

# The parameter is a variable that a function takes in. Below is a parameter user_name. 
def say_howdy(user_name):
    print('Howdy', user_name)
    
# Any time you write a function, you must call it and pass in an argument. 
name = input('What is your name? ')
say_howdy(name)

# A function that has more than one parameter
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

def second_function(parameter1, parameter2):
    print("Hey there", parameter1 + ' ' + parameter2)     # This method uses string concatenation
    print("Hey there", parameter1, parameter2)
    
second_function(first_name,last_name)

# Want to print multiple times? Call the function multiple times

second_function(first_name,last_name)
second_function(first_name,last_name)
second_function(first_name,last_name)

# Calculate the area of a rectangle using a function and a variable

# Function where we define what we expect to be passed in as a parameter:
def area(length: int, width: int) -> int:
    return length * width

area_of_rectangle = area(5,6)

print(area_of_rectangle)

# How to get the area of a circle:
def area_of_circle(radius):
    PI = 3.14
    return PI * radius**2 # Alternatively, you could write this: return PI * pow(radius, 2)

circle_area = area_of_circle(10)
print(circle_area)

# Class Exercise: You want to create a Python function called `wearSweater` that helps determine whether you should wear a sweater based on the weather conditions. The function takes three inputs: temperature (`temp`), humidity (`humidity`), and wind speed (`windSpeed`). The function should return `True` if you should wear a sweater and `False` otherwise. Here are the conditions:

# 1. If the temperature is less than 55 degrees, it's cold, so you should wear a sweater.
# 2. If the temperature is between 55 and 65 degrees and the humidity is less than 30%, it's cool and dry, so you should wear a sweater.
# 3. If the temperature is less than 60 degrees and the wind speed is greater than 10, it's chilly due to the wind, so you should wear a sweater.

# Now, create a Python function that incorporates these conditions. Use the `input` function to take user input for temperature, humidity, and wind speed. Ensure that the function returns the correct result based on the given conditions. Finally, print the result of calling this function. Can you provide the code for this?

def wearSweater():
    try:  
        temp = int(input("What is the temp outside? "))
        humidity = int(input("What is the humidity? "))
        windSpeed = int(input("What is the wind speed? "))
        
        wearSweater = False
        
        if temp < 55:
            wearSweater = True
        elif temp >= 55 and temp < 65 and humidity < 30:
            wearSweater = True
        elif temp < 60 and windSpeed > 10:
            wearSweater = True 
        return wearSweater
    except ValueError:
        return 'Please enter a valid whole integer. Decimals and other special characters are not allowed.'

print(wearSweater())

# When to use a function within a function:

def order_flooring(order_number: int, length: int, width: int) -> int:
    if order_number <= 0:
        print('Invalid order number')
    elif order_number > 0:
        amount_of_flooring = area(length, width)
        return amount_of_flooring
print("You ordered", order_flooring(101,20,30), "sqft of flooring.")