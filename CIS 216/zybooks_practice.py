#zybooks_practice

'''
old_substring = 'a'
string_twister = 'abcabcabc'

if old_substring in string_twister:
    print(f'At:', string_twister.rfind(old_substring))
    string_twister = string_twister.replace(old_substring, '9', 3)
    print(string_twister)

'''

'''
for i in bin_string[-1: -(bin_string(len) - 1)]:
    binary = bin_string[i]
    
    for exp in range(len(bin_string) + 1, 0, -1):
        digit = (2**exp) * binary
        
print(bin_string)


#7.6the mad libs while loop
user_input = input('input word then number')
tokens = user_input.split()

user_word = tokens[0]
user_int = tokens[1]


while user_word != 'quit':
   
    print(f'If you find a {user_word}, you will have {user_int} years of good luck!')
    user_input = input('input another word then number')
    tokens = user_input.split()
    user_word = tokens[0]
    user_int = tokens[1]
    

#8.16 lab: varied amount of input data
#Statistics are often calculated with varying amounts of input data.
#  Write a program that takes any number of non-negative floating-point 
# numbers as input, and outputs the max and average, respectively.
#Output the max and average with two digits after the decimal point.
   
float_data = input('enter 4 float numbers')
tokens = float_data.split()

num_data_items = len(tokens)


float_data_items = [float(i) for i in tokens]
max_datum = max(float_data_items)
sum_data = sum(float_data_items)
data_mean = sum_data / num_data_items

print(f'The maximum value is {max_datum:.2f} and the average of the data set is {data_mean:.2f}.')

#print(max_datum)
#print(sum_data)


#Write a program that first gets a list of integers from input. 
# That list is followed by two more integers representing lower and 
# upper bounds of a range. Your program should output all integers from 
# the list that are within that range (inclusive of the bounds).
# output looks like 25,0,33,    

user_input = input('integers ')
tokens = user_input.split()
lower_bound = 21
upper_bound = 54

integers = [int(i) for i in tokens]

in_range_ints = [int for int in integers if lower_bound <= int <= upper_bound ]

for i in range(len(in_range_ints)):
    print(f'{in_range_ints[i]},',end='')

# below code went into zy and passed 
user_input1 = input()
user_input_bounds = input()

tokens = user_input1.split()
bounds = user_input_bounds.split()

integers = [int(i) for i in tokens]
int_bounds = [int(i) for i in bounds]

lower_bound = int_bounds[0]
upper_bound = int_bounds[1]

in_range_ints = [int for int in integers if lower_bound <= int <= upper_bound ]

for i in range(len(in_range_ints)):
    print(f'{in_range_ints[i]},',end='')

     '''


#8.14.1 iterating over a dictionary
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}
#ALL OF THE BELOW CAN BE DONE USING ONE LINE !!!
#SUNDAY 11-10 new idea on how to connect the max value to the name. 
#use the dict.items() to create another dictionary and do another 
# dict.items on the sum and then use sorted(new_list) with index[-1]

all_grades = list(student_grades.values())
#andrew_grades_sum = sum(all_grades[0])
#nisreen_grades_sum = sum(all_grades[1])
#alan_grades_sum = sum(all_grades[2])
#chang_grades_sum = sum(all_grades[3])
#tricia_grades_sum = sum(all_grades[4])

print(len(student_grades))

for name, grade_list in student_grades.items():
    print(f'{name}: {max(sum(grade_list))}')
    
    
grades_sums = [sum(all_grades[i]) for i in range(len(student_grades))]

print(max(grades_sums))


#USE THIS TO SOLVE THE ABOVE I THINK......
#Multiple key-value pairs, each representing a hotel room number and 
# the guest's name, are read from input and added to hotel_bookings. 
# In sorted order of the keys, output each key-value pair on one line

hotel_bookings = {}

input_line = input()
while input_line != 'end':
    room_number, guest = input_line.split()
    hotel_bookings[int(room_number)] = guest
    input_line = input()

room_num_sort = sorted(list(hotel_bookings.keys()))
for room in room_num_sort:    
    print(f'Room: {room}, Name: {hotel_bookings.get(room)}')

# zy lab 8.20 car wash
#Write a program to calculate the total price for car wash services. 
# A base car wash is $10. A dictionary with each additional service and 
# the corresponding cost has been provided. Two additional services can
#  be selected. A '-' signifies an additional service was not selected. 
# Output all selected services, according to the input order, along with 
# the corresponding costs and then the total price for all car wash services.


# zy 9.3.2 gumball mahchine
class VendingMachine:
    def __init__(self):
        self.money_deposited = 0

    def turn_knob(self):
        self.money_deposited += 0.75
        return self.money_deposited

gumball_dispenser1 = VendingMachine()
for i in range(int(input())):
    gumball_dispenser1.turn_knob()
print(f'The first gumball dispenser collected ${gumball_dispenser1.money_deposited:.2f}.')

gumball_dispenser2 = VendingMachine()
for i in range(int(input())):
    gumball_dispenser2.turn_knob()
print(f'The second gumball dispenser collected ${gumball_dispenser2.money_deposited:.2f}.')