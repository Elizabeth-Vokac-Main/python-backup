#this is for practice and redoing projects#
#call the class for the number error
#define and initialize the integer to check for variable type
#define request for input parameters (there will be two for each)
#             int2 the denom will have the if statement

import os
import random
os.system("cls")

def get_integer_input(prompt):
    while True:
        try:
            pass_length = int(input(prompt))
            return pass_length
        except ValueError: 
            print("Please enter an integer greater than or equal to 10. ")
pass_length = get_integer_input("Enter an integer equal to or greater than 10. ")

while pass_length < 10:
    pass_length = get_integer_input("You must enter an integer value greater than or equal to 10. ")


def get_integer_input(prompt):
    while True:
        try:
            diff_level = int(input(prompt))
            return diff_level
        except ValueError:
            print("You must enter a 1, 2 or 3 only. ")
diff_level = get_integer_input("Enter a 1 for easy, 2 for medium, 3 for hard. ")
while diff_level < 1 or diff_level > 3:
    print('You must enter a 1, 2 or 3 only. ')
print(f"You entered the length {pass_length}.")
print(f"You entered the difficylty level {diff_level}.")

lower_alpha = list("abc")
upper_alpha = list('ABC')    
digits = list("12345")
specials = list('!@#$%^')

if diff_level == 1:
    characters = lower_alpha
elif diff_level == 2:
    characters = upper_alpha + digits
elif diff_level == 3:
    characters = lower_alpha + upper_alpha + digits + specials

password = ''

for i in range(1, pass_length + 1):
    password += random.choice(characters)

print(password)





"""
#accumulators
num_list = [1, 2, 3, 5, 8, 13, 21]
total = 0
for num in num_list:
    total += num
    print(f"cumulative sum =", {total})

num_list = [1, 2, 3, 5, 8, 13, 21]
count = 0
for num in num_list:
    if num % 2 == 0:
        count += 1
        print(count)
"""
'''
for i in range(1, 100):
    rand_numb = random.randint(1, 100)
print(rand_numb) 

for max_guesses in range(1, 11): 
    guess = int(input("Guess a number between and including one and 100."))
    if max_guesses == 10:
        print("Sorry, you are out of guesses.")
        break
    if guess == rand_numb:
       print("You got it!")
       break
    if guess > rand_numb:
        print("Too high, guess again.")
    else:
        print("Too low, guess again.")
'''
'''
byte_array = bytearray([0b00000001, 0b00000011, 0b00000111])
print(byte_array)

string_representation = byte_array.decode("utf-8")
print(string_representation)


int1 = 56
byte_array = int1.to_bytes()
print(byte_array)

(24).as_integer_ratio()
print()

for i in range(1, 5):
    for j in range (i, 5):
        print(i)


def cipher(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted = "defghijklmnopqrstuvwxyzabc"
    table = str.maketrans(alphabet, shifted)
    return text.translate(table)
cipher("python")
print(table)
'''
'''
float_number = 0.5
ratio = float_number.as_integer_ratio()
print(ratio)


floating_point = 0.75
ratio = floating_point.as_integer_ratio()
print(ratio)
'''

'''
for i in range(1,6):
    for j in range(i,6):
        print (i)
    print("\n")
'''
'''
def printPageHeader():
    print("private academy elementary school")

def printColumnHeader():
    print("\n Classroom Grade Month tuition\n")

printPageHeader()


for classroom in range(1,4):
    printColumnHeader()
    for grade in range(0,6):
        for month in range(1, 10):
            print ("    ", grade, end = '        ')
            print( "   ", classroom, end = '')
            print ("    ", str(month).rjust(2), end = '')
            if grade == 0:
                tuition = 200
            else:
                 tuition = grade * 55
            print ("   ", str(tuition).rjust(2))
'''
"""
            formatted_currency = f"${tuition:,.0f}"
            print(classroom, "_______", grade, "______", month, "___________", formatted_currency)
"""
'''
class SpecificNumberError(Exception):
    def __init__(self, int2):
        self.int2 = int2

def get_int_input(prompt):
    while True:
        try:
            int1 = int(input(prompt))
            return int1
        except ValueError:
            print("please enter an integer number")

int1 = get_int_input("Enter your first integer.")
message = f"You entered the number {int1}."
print(message)        

def get_int_input(prompt):
    while True:
        try:
            int2 = int(input(prompt))
            if int2 == 0:
                raise SpecificNumberError(int2)
            return int2
        except ValueError:
            print("Please enter an integer.")
        except SpecificNumberError:
            print("Please enter a second non-zero interger.")

int2 = get_int_input("Enter any non-zero integer.")
message = f'You entered the number {int2}.'
print(message)

'''     



