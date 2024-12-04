#compile class notes

#VARIABLES
# odd types are byte, bytearray, memoryview
#Python Casting
#strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1
#looping thru a sting

'''
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
    print(f"You chose", user_choice)
    print(f"CPU chose", cpu_choice)  
def main_program():
    """this separates the main code from the defined function objects"""
    print("\x1b[2J")    #clears the screen
    print(print_choices.__doc__)    #prints the docstring """prints players choices"""
#________________________________________________________________________________________
'''
'''
import os
os.system('cls')

#control break example
sales_data = [['north', 10], ['south', 20], ['east', 30]
              ['north', 12], ['south', 22], ['east', 32]
              ['north', 15], ['south', 25], ['east', 35]]

#sort the data
sorted_sales_data = sorted(sales_data)

#initialize variables
current_region = None
total_sales = 0

#control break detection
for each_element in sorted_sales_data:
    if each_element[0] != current_region:
        if current_region is not None:
            print(f"Total sales for, {current_region}: {total_sales}")
            print("_________________________________________________")
        current_region = each_element[0]
        total_sales = 0
    total_sales += each_element[1]

print(f"Total Sales for {current_region}: {total_sales}")


# BEGIN CIS 216

#dictionaries use {} directions for below = 
Dictionary user_ages contains four key-value pairs, each representing a 
student's name and age. Read a student name from input. 
Then, output the corresponding age from user_ages. 
Finally, delete that pair from user_ages.

user_ages = {'Ana': 39, 'Val': 68, 'Huy': 23, 'Gus': 74}
student_name = input()  #for this to work it has to be a dict name.
print(user_ages[student_name])
del user_ages[student_name]

print('Remaining pairs:')
print(user_ages)

name_age_pairs = {'Ava': 50, 'Kim': 60, 'Meg': 28, 'Cam': 32}
print('Original:')
print(name_age_pairs)

name1 = input()
name_age_pairs[name1] = name_age_pairs[name1] - 1

print('Updated:')
print(name_age_pairs)

#Dictionary word_to_num contains ten key-value pairs. 
Read strings word1 and word2 from input. 
Strings word1 represents a two-digit number and word2 reps a one-digit 
number. Use word_to_num to access the numerical equivalent value of the 
two words. Then, output the two-digit number represented
by the two words together.

word_to_num = {
	'eighty': 80, 'one': 1, 'two': 2, 'three': 3,
	'four': 4, 'five': 5, 'six': 6, 'seven': 7,
	'eight': 8, 'nine': 9
}
word1 = input()
word2 = input()

two_digs = word_to_num[word1] // 10
one_digs = word_to_num[word2]

print(f'{two_digs}{one_digs}')

STRING METHODS

dans_number = input().split()

customized_number = '}-{'.join(dans_number)

customized_number = "{" + customized_number + "}"
print(f"Dan's number: {customized_number}")


Strings 8.1 - 8.xx

#zy 8.2 LISTS Integer num_input is read from input, representing the 
# number of integers to be read next. Read the remaining integers from
#  input and append each integer to input_list.

num_input = int(input())

input_list = []

for integer in range(num_input):
    integer = int(input())
    input_list.append(integer)

print(input_list)
'''

#zy 8.3 iterating through list - find max even number
user_input = input('Enter numbers')
tokens = user_input.split()

#convert strings to integers - first two loops could be combined into 1
nums = []
for token in tokens:
    nums.append(int(token))
#print each position and number
print() # print a new line
for index in range(len(nums)):
    value = nums[index]
    print(f'{index}: {value}')
#determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        #first even number found
        max_num = num
    elif (max_num != None) and (num > max_num) and (num % 2 == 0):
        #max is a number, num (next) is larger than max and num is even
        max_num = num

print(f'Max even number is {max_num}')

#zy 8.3.1 find sum of numbers in a list
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print(f'{pos}: {token}')

sum = 0
for num in nums:
    sum += num

print(f'Sum: {sum}')
print(f'Average: {sum/len(nums)}')
#The built-in enumerate() function iterates over a list and provides an 
# iteration counter. The program above uses the enumerate() function, 
# which results in the variables pos and token being assigned the current 
# loop iteration element's index and value, respectively. 

#zy 8.3
# Read input and split input into tokens
tokens = input().split()

experiment_data = []
for token in tokens:
    experiment_data.append(int(token))

print(f'All data: {experiment_data}')

all_accepted = True
for index in range(len(experiment_data)):
    if (index % 2) != 0:
        print(f'Sample at index {index} is {experiment_data[index]}')
        if experiment_data[index] <= 60:
            all_accepted = False

if all_accepted:
    print('All integers at odd indices are greater than 60.')
else:
    print('At least one integer at an odd index is less than or equal to 60.')

#zy 8,5
ttt_board = [
  input().split(),
  input().split(),
  input().split()
]

if (ttt_board[0][1] == 'o') and (ttt_board[1][1] == 'o') and (ttt_board[2][1] == 'o'):
    print(f'A win at column 1.')
else:
    print('No win at column 1.')
            

#zy 8.5.1 list nesting
num_lines = int(input())
data_2d = []
for row_index in range(num_lines):
    row_elements = []
    for x in input().split():
        row_elements.append(int(x))
    data_2d.append(row_elements)

for row_index in data_2d:
    for row_elements in row_index:
        print(row_elements, end=' ')
    print() 
        
#zy 8.5.1 list nesting
grid_size = int(input())

pattern_2d = []
for m in range(grid_size):
    row = []
    for n in range(grid_size):
        row.append(0)
    pattern_2d.append(row)

for m in range(grid_size):
     for n in range(grid_size):
        pattern_2d[m][n] = m + n - 2
        pattern_2d[n][m] = m + n - 2
        

for row in pattern_2d:
    for cell in row:
        print(cell, end=' ')
    print()

    # dictionaries dictionary search values and keys separately
grades = {'a': 90, 'b': 80}
my_grade = 80
if my_grade not in grades.values():
    print('not in there')
else:
    print('it is there!!!!')

    
   
grades = {'a': 90, 'b': 80}
key_to_find = 'a'
value_to_find = 90

# Search for both the key and value together
if (key_to_find, value_to_find) in grades.items():
    print("Found the key-value pair!")
else:
    print("Key-value pair not found.")

    