'''

def int_to_reverse_binary(integer_value):
    if integer_value > 0:
        parity = str(integer_value % 2)
        half_int_floor = integer_value // 2
        half_int_bin = bin(half_int_floor)[2:]
        half_int_str = str(half_int_bin)
        int_bin_back = parity + half_int_str
        return int_bin_back
    return '0' #replaces else return zero
        
def string_reverse(input_string):
    string_reverse = ''
    for i in range(-1, -len(input_string) - 1, -1):
        string_reverse += input_string[i]
    return string_reverse

if __name__ == '__main__':
    integer_value = 122
    reversed_string = string_reverse(int_to_reverse_binary(integer_value))
    print(reversed_string)


#int_to_reverse_binary(6)

#6.19 lab driving costs

def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    trip_cost = ((dollars_per_gallon / miles_per_gallon) * miles_driven)
    return trip_cost

mpg = float(input())
dpg = float(input())

trip_cost_10 = driving_cost(mpg, dpg, 10) 
trip_cost_50 = driving_cost(mpg, dpg, 50)
trip_cost_400 = driving_cost(mpg, dpg, 400)

print(f'{trip_cost_10:.2f}')
print(f'{trip_cost_50:.2f}')
print(f'{trip_cost_400:.2f}')

if __name__ == '__main__':
    pass # Type your code here.


oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person == 4) or (nth_person == 5):
    print(f'The {nth_person}th oldest person lived {oldest_people[nth_person-1]} years')
elif nth_person == 1:
    print(f'The oldest person lived {oldest_people[nth_person-1]} years')
elif nth_person == 2:
    print(f'The {nth_person}nd oldest person lived {oldest_people[nth_person-1]} years')
elif nth_person == 3:
    print(f'The {nth_person}rd oldest person lived {oldest_people[nth_person-1]} years')



#zybooks 8.2 lists

riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n'
        '(6) Find place in line.\n'
        '(7) Enter name to remove rider.\n\n'
        'Enter your choice here.  '
)
user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider 
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        vip_name = input('Enter VIP name:').strip().lower()
        print(vip_name)
        line.insert(num_vips, vip_name)
        num_vips += 1
        print(num_vips)
        # Add new rider behind last VIP in line
        # Hint: Insert the VIP into the line at position num_vips.
        #Don't forget to increment num_vips.

    elif user_input == '3':  # Dispatch ride
        #print(num_vips)
        if len(line) >= riders_per_ride:
            for i in range(riders_per_ride):
                line.pop(0)
        #print(line)
        if num_vips >= riders_per_ride:
            num_vips = num_vips - riders_per_ride
        else:
            num_vips = 0
        print(num_vips)
        # Remove last riders_per_ride from front of line.
        # Don't forget to decrease num_vips, if necessary.

    elif user_input == '4':  # Print riders waiting in line
        print(f'{len(line)} person(s) waiting: {line}')

    elif user_input == '5':
        print(f'Goodbye')
    
    elif user_input == '6': #find name place in line
        user_name = input('Enter your name.')
        place = line.index(user_name + 1)
        print(f' Your place in line is {place}.')
        
    elif user_input == '7': #remove name from line
        user_name - input('Enter your name.')
        line.remove(user_name)
        print(f'{user_name} you have been removed from the line.')
    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)

'''

num_lines = 4
data_2d = []
for row_index in range(num_lines):
    row_elements = []
    for x in input().split():
        row_elements.append(int(x))
    data_2d.append(row_elements)

for row_index in data_2d:
    for row_elements in row_index:
        print(f'{row_elements}, end='', '\n'')
              
