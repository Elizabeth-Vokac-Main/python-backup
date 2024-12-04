#sandbox scratch paper for base cons

#print('test'.__len__())
#print('supercalifragalistic'.__len__())


#octal_rep = oct(123)
#print(octal_rep)

rev_hexa_str = '9b1'
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






#then loop within the first for loop ? with n using equation??


