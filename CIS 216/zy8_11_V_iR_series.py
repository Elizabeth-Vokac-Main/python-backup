#Modify the program to compute the voltage drop across each resistor, 
# store each in another list (voltage_drop), and print the results in 
# the following format:
# 1) 3.3
# 2) 1.5

num_resistors = 5
resistors = [3.3, 1.5, 2.0, 4.0, 2.2]
voltage_drops = []


print(f'{num_resistors} resistors are in the series.')
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)


print(f'Input ohms of {num_resistors} resistors')

'''
for i in range(num_resistors):
    
    res = float(input(f'{i + 1}) '))
    print(res)
    resistors.append(res)
'''
#  Calculate current
current = input_voltage / sum(resistors)


# Calculate voltage drop over each resistor

volts = [(current * resistors[i]) for i in range(len(resistors))]
voltage_drops = [float(item) for item in volts]
print(f'Voltage drop per resistor is')
for i in range(num_resistors):
    print(f'{i+1}) {voltage_drops[i]:.1f} V')




# Print the voltage drop per resistor
# ....


