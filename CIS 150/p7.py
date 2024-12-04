
''' Liz Vokac Main
    Project 7 Tic Tac Toe game
    Due 7-13
    use 2D array to make text based game
    objective: 2 players, 3x3 grid, alternate turns, 
    verify wins & ties, handle invalid moves
'''
#1.Define Board: 2D array size 3x3, initialize array element ''
#2.Display the Board: function to show 2D array, 
   #iterate thorugh rows and columns, print cell contents (empty or X/O)
#3.Player input: function for input, prompt player moves (row & column)
   #validate input type and location (empty cell)
#4.Place Marker: with validated input, update array element w move
#5.Win Check: function(s) to check for wins
#6.Tie check: after move board full? no possible wins?
#7.Game Loop: Loop to control game flow, manage board display

#extras 8, 9, 10: single player mode (vs cpu), player choice X/O
   #tracking wins for players

import os
import random
os.system('cls')

#0.print instructions
def print_instructions():
    print("This two player game is called Tic Tac Toe and the objective is to")
    print("alternate turns marking an X or O on a 3x3 grid to get three in a ")
    print("row either horizontally, vertically or diagonally.")
    print("Be strategic and make sure to block the other player from winning.")
    print()

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

#1.Define Board: 2D array size 3x3, initialize array element ''
def print_board(board):
    print('     ',board[0][0], '|',board[0][1], '|',board[0][2])
    print('----------------------')
    print('     ',board[1][0], '|',board[1][1], '|',board[1][2])
    print('----------------------')
    print('     ',board[2][0], '|',board[2][1], '|',board[2][2])
    print()
 
#2.Validate the player chooses 1-9 inclusive for each turn
def validate_input(position):
    while (position < 1 or position > 9):
        position = int(input("Enter a value 1 - 9 to mark your move."))
    return position

#3.Make sure the player's position choice corresponds to the board (could this be done with i and j nested loops?)
def validate_position(board, position):
    if position == 1:
        if board[0][0] == 1:
            board[0][0] = 'x'
    if position == 2:
        if board[0][1] == 2:
            board[0][1] = 'x'
    if position == 3:
        if board[0][2] == 3:
            board[0][2] = 'x'
    if position == 4:
        if board[1][0] == 4:
            board[1][0] = 'x'
    if position == 5:
        if board[1][1] == 5:
            board[1][1] = 'x'
    if position == 6:
        if board[1][2] == 6:
            board[1][2] = 'x'
    if position == 7:
        if board[2][0] == 7:
            board[2][0] = 'x'
    if position == 8:
        if board[2][1] == 8:
            board[2][1] = 'x'
    if position == 9:
        if board[2][2] == 9:
            board[2][2] = 'x'
            return True
        else:
            print("\n" "That spot is already taken, select an open position.")
            return False
          
    
def computer_move(board):
    while True:
        position = random.randint(1,9)
        if position == 1:
            if board[0][0] == 1:
                board[0][0] = 'O'
                break
        if position == 2:
          if board[0][1] == 2:
              board[0][1] = 'O'
              break
        if position == 3:
            if board[0][2] == 3:
                board[0][2] = 'O'
                break
        if position == 4:
            if board[1][0] == 4:
                board[1][0] = 'O'
                break
        if position == 5:
            if board[1][1] == 5:
                board[1][1] = 'O'
                break
        if position == 6:
            if board[1][2] == 6:
                board[1][2] = 'O'
                break
        if position == 7:
            if board[2][0] == 7:
                board[2][0] = 'O'
                break
        if position == 8:
            if board[2][1] == 8:
                board[2][1] = 'O'
                break
        if position == 9:
            if board[2][2] == 9:
                board[2][2] = 'O'
                break

  

def check_for_winner(board):
    if (    ((board[0][0] == board[0][1]) and (board[0][1] == board[0][2])) or 
            ((board[1][0] == board[1][1]) and (board[1][1] == board[1][2])) or
            ((board[2][0] == board[2][1]) and (board[2][1] == board[2][2])) or
            ((board[0][0] == board[1][0]) and (board[1][0] == board[2][0])) or 
            ((board[0][1] == board[1][1]) and (board[1][1] == board[2][1])) or
            ((board[0][2] == board[1][2]) and (board[1][2] == board[2][2])) or
            ((board[0][0] == board[1][1]) and (board[1][1] == board[2][2])) or
            ((board[0][2] == board[1][1]) and (board[1][1] == board[2][0]))    ):
        return True
    else:
        return False
    print("Congratulations, that was the winning move!!")
        
    


#4.Define the game play
def play_game():
    print_instructions()

    board = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    print_board(board)
    """
    #set player to X
    player = 'X'
    """
    turns = 0
    
    #set Boolean value is_gameover
    is_gameover = False
   

    while True:
        position = input("Select a position on the board to place your mark.")
        position = validate_input(int(position))
        validate_position(board, position)
        turns +=1

        #check for a winner
        if (turns > 4):
            if (check_for_winner(board)):
                print_board(board)
                print("\nCongratuatlions, that was the winning move!")
                break
      
        #computer takes a turn
        computer_move(board)
        turns +=1
        """
        if (turns > 4):
            if (check_for_winner(board)):
                print_board(board)
                print("\nCongratuatlions, that was the winning move!")
                break
        """
        if (turns > 8):
            if check_for_winner == False:
                print_board(board)
                print("\n This game is a tie.")
        
        print("The number of turns has changed to", turns)
        print_board(board)

play_game()















