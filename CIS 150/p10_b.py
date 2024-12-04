
import os
os.system("cls")

#datetime module gives class called datetime that has a date-time combo
from datetime import date
date = date.today()

def display_us_format(date):
    #US formatted date
    print(date.strftime("%m-%d-%Y"))

def display_uk_format(date):
    #UK formatted date
    print(date.strftime("%d-%m-%Y"))

def display_is_format(date):
    #IS formatted date
    print(date.strftime("%Y-%m-%d"))

def get_user_input():
    
    date_format_choice = input("Choose one letter for the date format: " 
                               "A for US, B for UK, C for IS, "
                               "or chhose X to exit. ")  
    while date_format_choice == "A" or "B" or "C":
        if date_format_choice == "A":
            print("You chose the US date format.")
            display_us_format(date)
        if date_format_choice == "B":
            print("You chose the UK date format.")
            display_uk_format(date)
        if date_format_choice == "C":
            print("You chose the IS date format.")
            display_is_format(date)
    if date_format_choice != "A" or "B" or "C" or "X":
        print("Please enter only on of four choices: A, B, C or X. ")
    if date_format_choice == "X":
        print("Thank you for using the date generator, goodbye.")
get_user_input()