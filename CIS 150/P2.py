'''
   Liz Vokac Main
   5-14-2024
   Project 2
   Simple Calculator
''' 
#calculator allows user to input two numbers to run the operations: multiply, divide, add, subrtact, modulus.
#considers integer input and nonzero integer for number2 input


#input section
#This is for error control so the second number does not equal zero.  It needs to be defined / added as an exception to the try-except code.  

class SpecificNumberError(Exception):
    def __init__(self, num2_int):
        self.num2_int = num2_int
       


#Make sure the user enters an integer for the first number. 
def get_int_input(prompt):
    while True:
        try:
            num1_int = int(input(prompt))
            return num1_int
        except ValueError:
            print("Invalid input, enter an integer number")
#assigns the variable to the function that checks for an integer
num1_int = get_int_input("Enter an integer")
#this f string allows a string and variable to print together
print(f"you entered {num1_int}")

#For the second integer there is another exception added to make sure it does not equal zero. This uses the try / except function 
def get_int_input(prompt):
    while True:
        try:
            num2_int = int(input(prompt))
            if num2_int == 0:
                raise SpecificNumberError(num2_int)
            return num2_int
        except ValueError:
            print("Invalid input, enter an integer number")
        except SpecificNumberError:
            print('Error: your second number cannot equal zero.')


num2_int = get_int_input("Enter a nonzero second integer")
print(f"You enetered: {num2_int}")

#processing
#perform calcs


add = num1_int + num2_int
sub = num1_int - num2_int
mult = num1_int * num2_int
div = num1_int / num2_int
mod = num1_int % num2_int

#output

print(num1_int, " + ", num2_int, " = ", add)
print(num1_int, " - ", num2_int, " = ", sub)
print(num1_int, " * ", num2_int, " = ", mult)
print(num1_int, " / ", num2_int, " = ", div)
print(num1_int, " % ", num2_int, " = ", mod)




