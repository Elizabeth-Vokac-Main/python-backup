
'''Project 4: Automated Tuition Management System for Academy
   Liz Vokac Main
   6/6/2024
   Due: Jun 15th
   Week 4: Decision making and nested If statememtns
'''
#Specs:  21 classrooms, 3 classes per 7 grades (0-6th), 9 mo, 
#         K = 200 / mo, 1st-6th = 50*grade level
#         grade (0-6)    room number (1-3)  month (1-9)
#         Invoice shows: grade number, classromm number, month, tuition.


import os
os.system("cls")

#create reusable page header
def printPageHeader():
    print("Private Academy Tuition Calendar")
#print header labels for columns
def printColumnHeader():
    print("Grade____Classroom_____Month_____Tuition")

#    printPageHeader()

#def variable ranges and equations to find cost, organized by grade first, then classroom

grade = range(0, 7)
for index_g in range(len(grade)):
        grade_instance = grade[index_g]
        print(f"grade instance at index {index_g}: {grade_instance}")
        classroom = range(1, 4)
        for index_c in range(len(classroom)):
            classroom_instance = classroom[index_c]
        print("\n")
        month = range(1, 10)
        for index_m in range(len(month)):
            month_instance = month[index_m]
            if grade == 0:
                tuition = 200
            else:
                tuition = grade*50
            formatted_currency = f"${tuition:,.0f}"
index_input_grade = int(input("Choose a grade from 0 to 6"))
index_input_classroom = int(input("Choose a classroom from 1 to 3"))
index_input_month = int(input("Choose a month from 1 to 9"))






#            print("  ", grade, "_______", classroom, "_________", month, "______",formatted_currency)
           
           
#print each individual invoice,for example grade 0, class 1, month 1

    



printPageHeader()
print('\n')
print('Grade______', grade_instance, '\n\n', 'Classroom______', classroom_instance, '\n\n', 'Month______', month_instance, '\n\n', 'Tuition______', formatted_currency  )


