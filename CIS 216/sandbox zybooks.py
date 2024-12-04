# sandbox zybooks

'''
num_resistors = 5
resistors = [3.3, 1.5, 2.0, 4.0, 2.2]
voltage_drops = []


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
for i in range(1, num_resistors):
    voltage_diff = input_voltage - voltages[0]
    voltage_diff -= voltages[i]
voltage_diffs = [(input_voltage - voltages[i]) for i in range(len(resistors))]
#for i in range(num_resistors):
#    voltage_drops.append(volt_drops)

voltage_drops = [float(item) for item in voltage_diffs]
for i in range(num_resistors):
    print(f'{voltage_drops[i]:.3f},', end=' ')


favorite_food = {}

input_line = input('enter mia orange ina coffee')
while input_line != 'stop':
    name, food = input_line.split()
    favorite_food[name] = food
    input_line = input('enter more')

print(favorite_food)

names = list(favorite_food.keys())
print(names)

sorted_names = sorted(names)
print(sorted_names)


 #   names = list(favorite_food.keys())
 #   sorted_keys = names.sort()
 #   print(sorted_keys)


'''
class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):
        pay = float(self.wage * self.hours_worked)
        return pay

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice:\n Net pay: {alice.calculate_pay():.2f}')

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print(f'Barbara:\n Net pay: {barbara.calculate_pay():.2f}')
