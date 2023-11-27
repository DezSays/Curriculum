# Python Basics
# URL to presentation: https://www.canva.com/design/DAF07-Kohlo/uI-dpUpI2458yTQvC_Rpow/edit?utm_content=DAF07-Kohlo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

# Intro to Python Types

# Integers
# Assigning the left hand side (the variable), then the assignment operator (=) which assigns the value on the right hand side (28) to the variable on the left hand side (age). The age variable below is only considered an integer because it is a whole number!
age = 28
print(age)

# Float - A float is anumber that is not a whole number.
pi = 3.14159
print(pi)

# A statement is a general term for a single instruction that uses or manjipulates a value. Lines 5,6,9, and 10 are all examples of statements. These comments are NOT considered a statement.

#  Boolean - can only have True or False value. T and F must be capital!
is_raining = False
print(is_raining)

# Strings - a combination of alphanumeric values. All of the following are examples of strings:
name = 'Dez'
team = "Braves"
birthday = "October 7, 1995"
# If you want to print on multiple lines, like a paragraph, do the following:
months = '''
Jan,
Feb,
March
'''
print(months)
print(name)

# List - This is a sequence of values. These values can be integers, floats, strings, etc.
scores = [12,54,896,15]
names = ['doug', 'teddy', 'mister meseeks']
print(scores[0])

# Dictionaries - this is a sequence of labaled values:
NBA_Teams = {"Atlanta":"Hawks", "Houston": "Rockets", 'Orlando': 'Magic'}
print(NBA_Teams["Orlando"])

# Special Characters:
# \b - backspace
# \n - new line
# \t - horizontal tab
# \v - vertical tab
# \r - carriage return

username = input("Type in your username: ")
password = input("Type in your password: ")
print(username,password)

# Using a variable within the print command in a more personalized way by using the interpolation operator. The interpolation operator takes values that are stored in variables and placed them within the string. 
print("Welcome %s" % username)

my_age = '28'
print('I am %s' % my_age)

# Using a float, you will use %f. If you only want a few numbers after the decimal, say you want 3 after the decimal, you would write it as you see below. It will round the number!
print("pi = %f" % pi)
print("pi to the third decimal = %.3f" % pi)

# Division: The below will return the result as a float (2.0), NOT as an integer.
result = 4/2
print('Result: ', result)

# Absolute value
positive_integer = abs(-45)
print(positive_integer)

# Exponents and Rounding
exponents = pow(2,2)
rounding = round(pi)
exp = 2**2
print(exponents, rounding, exp)

current_temp = 45
freezing_temp = 32

if current_temp < freezing_temp:
    print('It is way too cold out here man!')
elif current_temp > freezing_temp:
    print('Not frozen! Yay!')
elif current_temp == freezing_temp:
    print('It is right at the freezing point! Better buy some milk and bread!')
else:
    print('There seems to be an error. Check your code.')
    
is_sunny = False

# AND - meaning both conditions on either side of the and must be true
if current_temp < freezing_temp and is_raining == True:
    print('It is freezing and raining. Snow/hail time yall.')
elif current_temp > freezing_temp and is_raining == False:
    print("What a lovely day!")
else:
    print("It is not a lovely day.")

# OR - only one condition needs to be true
if current_temp < freezing_temp or is_raining == True:
    print('It is freezing or it is raining. Either way, stay inside today guys.')
elif current_temp > freezing_temp or is_raining == False:
    print('It is a clear day today!')
    
if is_sunny != True:
    print('It is not sunny. The != operator in the if statement means not.')
    
# Lists
class_peeps = ['Dez', 'Tri', 'Kenny', 'Hien', 'John', 'Tony']

# Print the entire list
print(class_peeps)

# Print the first person in the list
print(class_peeps[0])

# Example 1: Print all names in the list
for name in class_peeps:
    print(name)
    
# Example 2: Change Dez to say instructor, Kenny to Ken, Tri to student
for name in class_peeps:
    if name == "Dez":
        print("Instructor")
    elif name == 'Kenny':
        print('Ken')
    elif name == 'Tri':
        print('Student')
    else:
        print(name)

# Example 3: Will print the numbers 0-9
for num in range(10):
    print(num)

# Example 4: Print the numbers 5-10
for num in range(5,11):
    print(num)

# Print the first letter of Atlanta ('A')
city = 'Atlanta'
print(city[0])

# How to delete the last item from a list:
class_peeps.pop()
print(class_peeps)

# Exercise 1:
    # Programming Task: ID Number Classification
    # Develop a program prompting the user for their ID number.
    # Display "1st" if ID < 100, "2nd" if 100 <= ID <= 249, and "All reservations taken" if ID > 250.

# Exercise 2: 
    # Python Error Types Review:
    # Incorporate additional error types from provided flashcards into your notes.
    # Review flashcards at Quizlet link.
    # Be prepared to discuss various error types in the morning class.