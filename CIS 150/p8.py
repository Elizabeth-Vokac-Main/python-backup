
"""Project 8 Rock Paper Scissors Lizard Spock
    Due July 20th Sat
    Liz Vokac Main
"""
import os
os.system("cls")
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

#generate a random number
def computer_plays():
        cpu_move = random.randint(1,5)
        if cpu_move == 1:
            print("CPU chooses, rock")
        if cpu_move == 2:
            print("CPU chooses, paper")      
        if cpu_move == 3:
            print("CPU chooses, scissors")
        if cpu_move == 4:
            print("CPU chooses, lizard")
        if cpu_move == 5:
            print("CPU chooses, spock")
        return cpu_move    
            

#player input validation
def validate_input(player_move):
    while player_move not in ["rock", "paper", "scissors", "lizard", "spock", "Rock", "Paper", "Scissors", "Lizard", "Spock", "ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK", 1, 2, 3, 4, 5]:
        player_move = (input("Please choose only one of Rock, Paper, Scissors, Lizard or Spock.  "))
    return player_move

#compare the moves to declare a winner
def find_winner(player_move, cpu_move):
    if player_move in ('rock', 'Rock', 'ROCK'):
        player_move = 1
    elif player_move in ('paper', 'Paper', 'PAPER'):
        player_move = 2
    elif player_move in ('scissors', 'Scissors', 'SCISSORS'):
        player_move = 3 
    elif player_move in ('lizard', 'Lizard', 'LIZARD'):
        player_move = 4
    elif player_move in ('spock', 'Spock', 'SPOCK'):
        player_move = 5  

    if player_move == cpu_move:
        print("It's a tie, play again!")
    if player_move == 1 and cpu_move == 2:
        print("You lose, paper covers rock!")
    if player_move == 1 and cpu_move == 3:
        print("You win, rock crushes scissors!")
    if player_move == 1 and cpu_move == 4:
        print("You win, rock crushes lizard!")
    if player_move == 1 and cpu_move == 5:
        print("You lose, spock vaporizes rock!")
    if player_move == 2 and cpu_move == 1:
        print("You win, paper covers rock!")
    if player_move == 2 and cpu_move == 3:
        print("You lose, scissors cut paper!")
    if player_move == 2 and cpu_move == 4:
        print("You lose, lizard eats paper!")
    if player_move == 2 and cpu_move == 5:
        print("You win, paper disproves spock!")
    if player_move == 3 and cpu_move == 1:
        print("You lose, rock crushes scissors!")
    if player_move == 3 and cpu_move == 2:
        print("You win, scissors cut paper!")
    if player_move == 3 and cpu_move == 4:
        print("You win, scissors decapitate lizard!") 
    if player_move == 3 and cpu_move == 5:
        print("You lose, spock smashes scissors!")          
    if player_move == 4 and cpu_move == 1:
        print("You lose, rock crushes lizard!")
    if player_move == 4 and cpu_move == 2:
        print("You win, lizard eats paper!")
    if player_move == 4 and cpu_move == 3:
        print("You lose, scissors decapitate lizard!") 
    if player_move == 4 and cpu_move == 5:
        print("You win, lizard poisons spock!") 
    if player_move == 5 and cpu_move == 1:
        print("You win, spock vaporizes rock!")
    if player_move == 5 and cpu_move == 2:
        print("You lose, paper disproves spock!")
    if player_move == 5 and cpu_move == 3:
        print("You win, spock smashes scissors!") 
    if player_move == 5 and cpu_move == 4:
        print("You lose, lizard poisons spock!") 

def play_game():
    print_instructions()
    while True:
        player_move = input("Enter your move from the case-insensitive list: rock, paper, scissors, lizard, spock  ")
        player_move = validate_input(player_move)
        print("You chose,", player_move)

        cpu_move = computer_plays()

        find_winner(player_move, cpu_move)

play_game()







    


