size = 5

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    print('Numbers: ', end ='')
    for num in numbers:
        print(num, end=' ')
    print()

def print_odd_numbers(numbers):
    print('Odd numbers: ', end=' ')
    for num in numbers:
        if num % 2 != 0:
            print(num, end=' ')
            num += 1
    print()

def print_negative_numbers(numbers):
    print('Negative numbers: ', end=' ')
    for num in numbers:
        if num < 0:
            print(num, end=' ')
            num += 1
    print()
    
nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)




'''
#How to get output from the above get_numbers function as input for the rest of the functions

user_numbers = get_numbers(numbers)
    
def print_odd_numbers(numbers):
    for i in 
    print(f'Odd numbers:')

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)
'''