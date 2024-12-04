#compile class notes

#VARIABLES
# odd types are byte, bytearray, memoryview
#Python Casting
#strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1
#looping thru a sting
for x in "peaches":
    print(x)

#length of a string
a = "123456789"
print(len(a))

z = "a b c d e f g"
print("e" in z)
if "f" in z:
    print("Yes, f is in z!")
if "y" not in z:
    print("Nope, y is not in z")

#alternative print methods
message = f"You entered {a}."  
print(message)



#STRING METHODS
#slicing strings
#1 return charachters 2-4, it starts at zero and does not include the 6th place which is denoted by 5
b = "hello world"
print(b[2:5])

#slice from start
b = "hello world"
print(b[:7])

#slice to end
print(b[3:])

#negative indexing starts from the end and counting starts at -1 right to left
print(b[-7:-2])

print(b.upper())
      
x = "YOU'RE DOING GREAT"
print(x.lower())

y = "   YOU'RE DOING OK     "
print(y.strip())

print(y.replace("YOU'RE", "I'M"))

#this split function returns a list where items separated by commas
Z = "ONE, two, three, four, five six seven"
print(Z.split(","))

#concatenate
a = "Hi"
b = "Alice, "
c = "how are you today?"
d = a + " " + b + c
print(d)

# f-strings to concat string w variable - f = format
height = 67
txt = f"My height is {height} inches."
print(txt)

# Placeholders and Modifiers
price = 9
txt = f"The price is exactly {price:.2f} dollars."
print(txt)

txt = f"The sale price is {price*0.8}, reduced by 20%."
print(txt)


#escape characters
#use a \ and then the illegal character: double quotes,',\,\n,\r,\t,\b,\f,\ooo,\xhh
txt = "They are known as the \"cheetahs\" of the sea."
print(txt)

txt = "\110\145\154\154\157"
print(txt)

abc = "\101\102\103\104\105\106\107"
z = (abc.lower())
print(z)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
# string.find(value, start, end) finds first occurance, returns -1 if none
x = txt.find("l")
print(x)


#DATA TYPES
#integer methods
floating_point = 0.75
ratio = floating_point.as_integer_ratio()
print(ratio)

#string literals and transitions
def cipher(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted = "defghijklmnopqrstuvwxyzabc"
    table = str.maketrans(alphabet, shifted)
    return text.translate(table)
print(cipher("python"))

#convert each number which is the unicode 'code point' of the individual letter characters
byte_array = bytes([65, 66, 67])
string_rep = byte_array.decode('utf-8')
print(string_rep)

#call the code point (corresponding to the letter) using the built-in ord() function
code_point = ord('Q')
print(code_point)


#accumulators
num_list = [1, 2, 3, 5, 8, 13, 21]
total = 0
for num in num_list:
    total += num
    print(f"cumulative sum =", {total})
for num in num_list:
    count = 0
    if num % 2 == 0:
        count += num


# LISTS AND RANDOM ELEMENTS
import random
#one random item from list
numbers = [1, 2, 3, 4, 5, 6]
random_number = random.choice(numbers)
#shuffle
random.shuffle(numbers)
#mulitple unique items from a list without replacement
lottery_numbers = list(range(1, 50))
winning_numbers = random.sample(lottery_numbers, 6)
#sampling mulitple random elements with replacement
dice_rolls = [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(5)]
print(dice_rolls)
#generate a list of random numbers
numbers_intrand = [random.randint(1, 100) for _ in range(10)]
print(numbers_intrand)
numbers = [1, 2, 3, 4, 5, 6]
multi_dups = random.choices(numbers, k=5)
print(multi_dups)
#FILE HANDLING
#opens to read (r) is implied
f = open("demofile.txt")
#code above is same as
f = open("demofile.txt", "rt")
#open file on the server (assume we have the file located in the same folder as Python)
f = open("demofile.txt", "r")
print(f.read())
#file in different location than the python folder and return thr first 5 characters of file
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read(5))
#return one line of a file at a time
f = open("demofile.txt", "r")
print(f.readline())
#loop thru file line by line
f = open("demofile.txt", "r")
for x in f:
    print(x)
f = open("demofile.txt", "r")
f.close()
#append content to demofile, which adds this same line each time its run
f = open("demofile.txt", "a")
f.write("or it could be a psychosomatic disorder")
f.close()
f = open("demofile.txt", "r")
print(f.read())
#create new file and gives error if already exists
f = open("new file.txt", "x")
#creates a file if does not exist, but overwrites if does
f = open("old file.txt", "w")
#delete a file
import os
os.remove("old file.txt")
#check if file exists and then delete
import os
if os.path.exists("old file.txt"):
    os.remove("old file.txt")
else:
    print("file DNE")
#delete folder
import os
os.rmdir("nobodysfolder")
#__________________from p8 learning about doc stringss
def print_choices(user_choice, cpu_choice):
    """prints players choices"""      #practice the docstring
    print(f"You chose", {user_choice})
    print(f"CPU chose", {cpu_choice})  
def main_program():
    """this separates the main code from the defined function objects"""
    print("\x1b[2J")    #clears the screen
    print(print_choices.__doc__)    #prints the docstring """prints players choices"""
#________________________________________________________________________________________






















