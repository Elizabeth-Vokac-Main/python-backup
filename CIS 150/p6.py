
'''NAME: Liz Vokac Main
   DATE: 6-21-24 
   PROJ: Project 6 Random password generator with difficulty levels.
   DESC: Incorporates sequence, selection, repitition and random numbers.
         Length > 9, levels = (easy, medium, complex)
   DUE: 6-29
'''

import os
import random
os.system('cls')

#explaination for user
print("     This is a random password generator. \n    Choose the length and difficulty level.\n")

#prompt user to enter desired length of password
#validate user input for: length pos int > 9 and one of given difficulty levels chosen
#include error messages for the user
def get_int_input(prompt):
    while True:
        try:
            pass_length = int(input(prompt))
            return pass_length
        except ValueError:
            print("Please enter an integer value greater than eight. ")
pass_length = get_int_input("Enter your desired password length of minimum nine. ")
#make sure they enter length 10 or greater
while (pass_length < 10):
    print("Please enter a password length greater than 9. ")
    pass_length = get_int_input("Enter your desired password length of minimum nine. ")


#prompt user to enter desired difficulty level
def get_int_input(prompt):
    while True:
        try: 
            diff_level = int(input(prompt))
            return diff_level
        except ValueError:
            print("Please make sure to enter the number 1 or 2 or 3.")
diff_level = get_int_input("For your difficulty level please enter a 1 for easy, a 2 for medium, or a 3 for complex. ")

#check that they enter either 1, 2 or 3 using error message
while diff_level < 1 or diff_level > 3:
    print('The difficulty level must be 1, 2 or 3. ' )
    diff_level = get_int_input("For your difficulty level please enter a 1 for easy, a 2 for medium, or a 3 for complex. ")

print(f"You entered the length {pass_length}.")
print(f"You entered the difficulty level {diff_level}.")

#define the pass character options for each level
alphabet_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alphabet_low = list('abcdefghijklmnopqrstuvwxyz')
digits = list('0123456789')
special_chars = list("!@#$%^&*()_,-=+{<}>?")

#control list choices for difficulty levels
if diff_level == 1:
    characters = alphabet_low
elif diff_level == 2:
    characters = alphabet_low + alphabet_up + digits
elif diff_level == 3:
    characters = alphabet_low + alphabet_up + digits + special_chars

#generate the password
#empty string to hold ... and define the variable password?  I don't completely get line 68, rest makes sense.
password = ''
for i in range(1, pass_length + 1):
    password += random.choice(characters)
print(f"Your password is {password}.")







