#Modify the program to compute the voltage drop across each resistor, 
# store each in another list (voltage_drop), and print the results in 
# the following format:
# 1) 3.3
# 2) 1.5

num_resistors = 5
resistors = []
voltage_drop = []


print(f'{num_resistors} resistors are in the series.')
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)


print(f'Input ohms of {num_resistors} resistors')
for i in range(num_resistors):
    
    res = float(input(f'{i + 1}) '))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

print(resistors)
# Calculate voltage drop over each resistor
#voltage_drop1 = current * resistors[0]

# Print the voltage drop per resistor
# ....


