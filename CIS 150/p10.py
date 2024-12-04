'''
NAME Liz Vokac Main
DATE 2024-8-9
PROJECT 10
DESCRIPTION Use the datetime module and have user choose date format.
'''
'''
PEP guidlines = 72 char per line max
{
    "editor.rulers": [72]
}
'''
import os
os.system("cls")

#datetime module gives class called datetime that has a date-time combo
from datetime import datetime

def display_us_format(date):
    #US formatted date
    return date.strftime("%m-%d-%Y")

def display_uk_format(date):
    #UK formatted date
    return date.strftime("%d-%m-%Y")

def display_is_format(date):
    #IS formatted date
    return date.strftime("%Y-%m-%d")

def get_user_input():
    # get the user to input one of the four accepted letters
    while True:
        date_format_input = input("Pick one letter for the date format:" 
                                  " A for US, B for UK, C for IS or "
                                  "X to exit. ").upper()
        if date_format_input in ["A", "B", "C", "X"]:
            return date_format_input
        else:
            print("Please choose only one of the four: A, B, C or X. ")

def main_date_loop():
    # the main part of program that calls values from above functions
    date = datetime.today()
    # get the current date from datetime module
    while True:
        # get the user choice as variable
        date_format = get_user_input()
        # get correct date format display from user's choice
        if date_format == "A":
            print("Today's date is", display_us_format(date) )
        if date_format == "B":
            print("Today's date is", display_uk_format(date) )
        if date_format == "C":
            print("Today's date is", display_is_format(date) )
        # take user out of the loop if they choose x for exit
        if date_format == 'X':
            print("Thank you for using the date generator, goodbye.")
            break

# starting the main program
if __name__ == "__main__":
    main_date_loop()
