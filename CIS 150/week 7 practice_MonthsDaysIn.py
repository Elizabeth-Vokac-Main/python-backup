#week 7 practice
#print from list months and total days in month

import os
os.system("cls")

months = ['J', 'F', 'M', 'A', 'MY', 'JN', 'JL', 'AG', 'S', 'O', 'N', 'D']

daysIn = [31, 28, 30, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(len(months)):
    print(str(months[i]) + " has " + str(daysIn[i]) + " days.")


yourMonth = int(input('what day of the month do you want to enter from 1-12?')) - 1
print(str(months[yourMonth]) + ' has ' + str(daysIn[yourMonth]) +' days.')

