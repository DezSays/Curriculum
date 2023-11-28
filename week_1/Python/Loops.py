# Solution from Homework from Intro.py

# try:
#     id = int(input("Type in your reservation number: "))
#     if id <= 100 and id > 0:
#         print("1st")
#     elif id > 100 and id < 250:
#         print("2nd")
#     elif id > 250:
#         print("All reservations have been filled. Please try again later.")
#     else:
#         print("This is not a number in our system. Please check your reservation number and try again.")
# except ValueError:
#     print("The input was not a valid integer. Please check your reservation number and try again.")


name = 'Dez Bryan'

# Get the length of a string
print(len(name))

# To get just the z from the string above, use the index value:
print(name[2])

drinks = ["Sprite", "Water", "Coffee", "Tea", "Coke"]
# To get the length of a list, use the len function:
print(drinks)
print(len(drinks))

# How to get the type, in this case a list:
print(type(drinks))

# How to get the type of an integer
length_of_drinks_list = len(drinks)
print(length_of_drinks_list)
print(type(length_of_drinks_list))

# Using a for loop:
for drink in drinks:
    print(drink)
    
nums = [1,2,3,4,5]

# Looping through a list of integers
for integers in nums:
    print(integers)

# Example of a while loop. It is iportant to increment the value, otherwise you will get stuck in an endless loop.
value = 0
while value < length_of_drinks_list:
    print(drinks[value])
    value = value + 1 
    
# How to iterate through a string using a for loop, such as my name listed at the top.
for letter in name:
    print(letter)

# How to do the same thing using a while loop
letter = 0
while letter < len(name):
    print(name[letter])
    letter += 1
    
# For loop to print each number that is evenly divisible by 4
int_list = [1,2,3,4,5,6,7,8,9,10]

for ints in int_list:
    if ints % 4 == 0:
        print(ints)
        
# Print all odd numbers from the list above
for ints in int_list:
    if ints % 2 == 1:
        print(ints)

# Let the user decide what to print. Ask what they would like each number to be divided by. 
try:
    user_choice = int(input("What would you like each number to be divided by? "))
    for i in int_list:
        if i % user_choice == 0:
            print(i)
except ValueError:
    print("The input was not a valid integer.")
    
# How to concatenate a string:
first_name = 'Dez'
last_name = 'Bryan'
full_name = first_name + ' ' + last_name
print(full_name)

# How to do a lexicon comparison. It is important to note that capital letters will always display as being before lower case. See below for example:
mystery_letter = 'F'
first_name_letter = 'd'
if first_name_letter < mystery_letter:
    print('First letter of the name comes before the myster letter')
else:
    print('Mystery letter comes before the first letter of the name.')

# Class Exercise: Place students in breakout rooms and organize them by their first name. Pay attention to capitalization! If your cutoff letter is a lower case but all of the students names are upper case, the upper case will always display BEFORE the lower case letters. Use the .lower() function to resolve this.
students = ['matt', 'Kenny', 'an', 'carlos B.', 'Tri', 'Tony', 'Hien', 'hein', 'John']
breakout_room_1 = []
breakout_room_2 = []
cut_off_letter = 'i'

for element in students:
    if element[0].lower() <= cut_off_letter:
        breakout_room_1.append(element)
    elif element[0].lower() > cut_off_letter:
        breakout_room_2.append(element)
        
        
print(breakout_room_1)
print(breakout_room_2)
