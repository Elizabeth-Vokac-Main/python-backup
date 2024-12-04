'''
Liz Vokac Main
Project 5
Due date 6-22
Number guessing game
Use a random number generator to give the player 10 guesses for a number between 1 and 100 inclusive. 
Say whether the number is too great or small after each guess.
Use the code random.randint(1,100), nested loops,conditional statements.
'''
#Hi Marty, the issue I had was being unable to stop the message "your guess is too low" from being printed even after the 10th attempt, 
# so I moved the if attempt code up to the top of the for loop.  However, I'm wondering if that creates too much memory
# like you said in the video where the computer has to ask itself if attempt equals 10 a bunch of times unnecessarily?
# Also, is it weird to have the first if statement followed by the elif...?

import os   #import operating system to clear the screen
import random  #import the random number generator
os.system("cls")  #clear pc screen

#print out a header for the user
print("This is a number guessing game.")
print("You have 10 attempts to guess one number between one and 100.""\n""One and 100 are included.")

#define the for loop using the random number generator.
for i in range(1, 100):
    target_number = random.randint(1, 100)

#input from user
for attempt in range(1, 11):
    guess = int(input("Guess an integer number. "))
    if attempt == 10:
        print("Sorry, you are out of attempts!")
        print(f"The correct number was", target_number)
        break
    if guess == target_number:
            print("You guessed it correctly!")
            break
    elif guess < target_number:
        print("Your guess is too low, guess again.")
    else:  
        print("Your guess is too great, guess again.")
   

