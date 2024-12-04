'''
   Liz Vokac Main
   5-14-2024
   Project 2
   Simple Calculator
''' 

#input section
#calculator allows user to input two numbers and multiply, divide, add, subrtact, modulus

class SpecificNumberError(Exception):
    def __init__(self, num2_int):
        self.num2_int = num2_int
        self.message = f"Error: Zero is not allowed."
        super().__init__(self.message)



def get_int_input(prompt):
    while True:
        try:
            num1_int = int(input(prompt))
            return num1_int
        except ValueError:
            print("Invalid input, enter an integer number")

num1_int = get_int_input("Enter an integer")
print(f"You enetered: {num1_int}")


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


num2_int = get_int_input("Enter a second integer")
print(f"You enetered: {num2_int}")




#processing
#perform calcs
#use a loop to make the calculator scroll through two ranges of numbers and output all calculations

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




