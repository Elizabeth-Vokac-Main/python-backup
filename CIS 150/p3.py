"""
Liz Vokac Main
Project 3 Sign cost calculator
CIS 150
Date = 6/3/24
Project 3 Cost of sign making calculator
base price 50, add 25 for oak and nothing for pine
Note: I did a version using string input and if statement instead that is quoted out at the bottom, just for me to compare. 
"""

print("Timberly's Sign Cost Calculator will help you get the cost of your wooden sign.")
print("Please tell us the tyep of wood to use for your sign.")
print("Your options are oak or pine.")
#assigns wood type as integer
oak = 1
pine = 0

#ensures integer input and defines the cost equation
def get_int_input(prompt):
    while True:
        try:
            wood = int(input(prompt))
            return wood
        except ValueError:
            print("Enter only one of the two: 1 for Oak or 0 for Pine.")

wood = get_int_input("Enter 1 for Oak or 0 for Pine. ")

cost = 50 + (25 * wood)

print("Your sign will cost","$", cost)


    
#_____________________________________________________________________
#using input string with if statements instead
'''
wood = input("Enter one wood type for the sign from the list: oak, pine.")

if wood == "oak":
    cost = 50 + 25
    print("The oak sign costs", + cost)
elif wood == "pine":
    cost = 50
    print("The pine sign costs", + cost)
else:
    print("Enter either oak or pine.")

'''
#way less code, but uses 2 equations
#Here I kept the else and if as a way to control for if the user entered the wrong input, probably a better way...
#might try to combine them 

