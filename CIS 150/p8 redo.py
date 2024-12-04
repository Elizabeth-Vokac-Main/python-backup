
"""
    Liz Vokac Main
    This is my p8 redo
    Due Sat 7-22
    rock paper etc using more lists, no number assignments, indeces, doc strings 
    and separation of objects as in using the main thingy for stand alone script
    vs imported modules.
"""

import os
import random

def print_instructions():
    print("""This is a variation on the game rock, paper, scissors that has two more choices, lizard or spock.
        Your input is not case sensitive, but you must enter one of the five words."
        \n Here are the rules for the winner: 
        Scissors beats paper
        Scissors decapitates lizard
        Paper beats rock
        Paper disproves Spock
        Rock crushes lizard
        Rock crushes scissors
        Lizard poisons Spock
        Lizard eats paper
        Spock smashes scissors
        Spock vaporizes rock""")

def cpu_chooses():
    """get the computers choice"""
    return random.randint(1, 5)

def user_chooses():
    """get the players choice"""
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    while True:
        user_choice = input("Choose one from the list: rock, paper, scissors, lizard or spock." ).lower()   #lower converts any cases/ combos into all lower
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid entry, please choose from the list: rock, paper, scissors, lizard or spock.")

def det_winner(user_choice, cpu_choice):
    """Determine who wins the game"""
    if user_choice == cpu_choice:
        print("It's a tie, play again!")
    elif ((user_choice == "rock") and (cpu_choice == "lizard" or cpu_choice == "scissors"))\
    or ((user_choice == "paper") and (cpu_choice == "scissors" or cpu_choice =="spock" ))\
    or ((user_choice == "scissors") and (cpu_choice == "paper" or cpu_choice =="lizard" ))\
    or ((user_choice == "lizard") and (cpu_choice == "spock" or cpu_choice =="paper" ))\
    or ((user_choice == "spock") and (cpu_choice == "rock" or cpu_choice =="scissors" )):
        print("You win!")
    else:
        print("Sorry, you lose")

def print_choices(user_choice, cpu_choice):
    """Print out the players' choices."""
    print(f"You chose", user_choice)
    print(f"CPU chose", cpu_choice)

def clear_screen():
    """Clears the screen for a windows user."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('clear')

def main_rock_paper_program():
    """This is a doc string to explain the use of the main program and
       show how the stand alone script operates vs imported modules """
    clear_screen()
    print_instructions()

    #print(print_choices.__doc__)    #prints the docstring """prints players choices"""

    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    cpu_choice = choices[cpu_chooses() - 1]   #calcs the index of list called choices using rand int minus 1
    user_choice = user_chooses()
    print_choices(user_choice, cpu_choice)
    det_winner(user_choice, cpu_choice)

if __name__== "__main__":
    main_rock_paper_program()



        

