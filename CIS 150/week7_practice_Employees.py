#week 7 practice_Employees 

#print from lists the employee, hours worked and payrate and amount paid. 


import os
os.system('cls')

employees = ['11', '22', '33', '44', '55']
hoursWorked = [8, 7, 9, 5, 3]
payRate = [100.5, 101.5, 102.5, 103.5, 104.5]

for i in range(len(employees)):
    print(employees[i] + ' worked ' + str(hoursWorked[i]) + ' hours at a payrate of ' + str(payRate[i]) + ' dollars per hour. ')

yourEmpNum = int(input('what is your employee number? '))
formatted_currency = (hoursWorked[i])*(payRate[i])
print('You earned ' + f"${formatted_currency:,.2f}.")

