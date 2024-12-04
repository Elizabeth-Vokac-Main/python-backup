'''
Base Conversions and TDD
Directory :  Main folder --> test -> __init__.py and test_my_math.py
1. binary string to decimal value
2. octal string to decimal value
3. hexadecimal string to decimal value
4. base 5 string to decimal value

in python console write -m unittest and it will run the test from the
correctly written directory
'''
#****SEE MESSAGE FROM 10-29 1:20PM ON LINE 79*************

#BINARY*********************************************************
#reverse the string first with negative index 
#and use n range 0 to len(string)
bin_string = '1010101010101'
rev_bin_string = ''

for i in range(-1, -len(bin_string) - 1, -1):
    rev_bin_string += bin_string[i]
print(rev_bin_string)

decimal = 0
for n in range(0, len(rev_bin_string)):
    index = rev_bin_string[n]
    digits = int(2**n) * int((index)) 
    decimal += digits
print(decimal)

#OCTAL*********************************************************
octal_string = '173'
rev_octal_string = ''

for i in range(-1, -len(octal_string) - 1, -1):
    rev_octal_string += octal_string[i]
print(rev_octal_string)

decimal2 = 0
for n in range(0, len(rev_octal_string)):
    digits2 = int(8**n) * int(rev_octal_string[n])
    decimal2 += digits2
print(decimal2)


#HEXADECIMAL**************************************************
hexa_string = '369'
rev_hexa_str = ''

#reverse the string
for i in range(-1, -len(hexa_string) - 1, -1):
    rev_hexa_str += hexa_string[i]
print(rev_hexa_str)


lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
upper_alpha = [item.upper() for item in lower_alpha]


rev_hex_to_dec_list = []
for i in range(0, len(rev_hexa_str)):
    if rev_hexa_str[i].isdigit():
        digit = int(rev_hexa_str[i])
    elif rev_hexa_str[i] in lower_alpha:
        digit = ord(rev_hexa_str[i]) - 87    #getting ascii number for lowercase and adjusting
    elif rev_hexa_str[i] in upper_alpha:     
        digit = ord(rev_hexa_str[i]) - 55    #getting ascii number for upper
    print(digit)
    rev_hex_to_dec_list.append(digit)
    decimal_sum = 0
    for n in range(0, len(rev_hex_to_dec_list)):
        decimal = int(16**n) * rev_hex_to_dec_list[n] #get the integer from the list
        decimal_sum += decimal
print(decimal_sum)

'''
#BASE 5*********************************************************
base_5_string = '1234'
rev_base5_string = ''
#the variables are named oddly just because these four functions are 
#all on the same page so in indiv file variable names should be
#decimal_sum and decimal or digits etc w no numbers in names
for i in range(-1, -len(base_5_string) - 1, -1):
    rev_base5_string += base_5_string[i]
print(rev_base5_string)

decimal_sum2 = 0
for n in range(0, len(rev_base5_string)):
    digits3 = int(5**n) * int(rev_base5_string[n])
    decimal_sum2 += digits3
print(decimal_sum2)

'''





