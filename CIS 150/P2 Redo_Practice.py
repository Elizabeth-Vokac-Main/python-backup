'''Practicing rewriting project 2 doing the 5 calcs'''

#call the class for the specific number error to add expection to the try / except function

class SpecificNumberError(Exception):
    def __init__(self, num2_int):
        self.num2_int = num2_int




def get_int_input(prompt):
    while True:
        try:
            num1_int = int(input(prompt))
            return num1_int
        except ValueError:
            print("Wrong input type, please choose an integer")
num1_int = get_int_input("Enter any integer")
print("you entered" + num1_int)


def get_int_input(prompt):
    while True:
        try:
            num2_int = int(input(prompt))
            if num2_int == 0:
                raise SpecificNumberError(num2_int)
            return num2_int
        except ValueError:
            print("please enter an integer")
        except SpecificNumberError:
            print("Please enter an integer that is not zero.")

num2_int = get_int_input("Please enter a nonzero integer")
print("You entered" + num2_int)            

        

    



add = num1_int + num2_int
sub = num1_int + num2_int
mult = num1_int * num2_int
div = num1_int / num2_int
mod = num1_int % num2_int


print (num1_int, "+", num2_int, "=", add)
