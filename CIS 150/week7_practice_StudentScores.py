
#parallel lists

#clear terminal
import os
os.system("cls")
#create name list
my_names = ['Wanda', 'Xena', 'Yana', 'Zaria']
#create scores list
scores = [[99, 98, 97, 96], [89, 88, 87, 86], [79, 78, 77, 76], [69, 68, 67, 66]]
#print all scores and average for each student
#average for each student
print(' Test    1   2   3   4   Average')
for i in range(len(scores)):
    #print name
    print(my_names[i] , end ='  ')
    #reset accumulator
    totalscore = 0
    for j in range(len(scores[i])):
        totalscore = totalscore + scores[i][j]
        print (str(scores[i][j]).rjust(6), end="  ")
    averagescore = totalscore / len(scores)
    #print average for each student
    print(" | ", end=" ")
    print(str(averagescore).rjust(6))

#print average score on each test
print("AVG   ", end = ' ')
for i in range(len(scores)):
    totalscore = 0
    for j in range(len(scores[i])):
        totalscore = totalscore + scores[j][i]
    averagescore = totalscore / len(scores)
    print(str(round(averagescore,1)).rjust(6), end=" ")

