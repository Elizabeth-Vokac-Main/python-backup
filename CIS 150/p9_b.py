
"""Project 9 Grade Point Processing
    Liz Vokac Main
    Due July 27th Saturday
    Practice using files and calculating with their data.
"""

import csv   # comma separated value file
import math  # math operators
import os    # operating system
os.system("cls")

def page_header():
    print(" \n\n      -------------------     STUDENT GRADE POINT REPORT     -------------------"
          " \n\n                                 By: Liz Vokac Main                      ")


def print_col_header():  
    print()  
    print("Page      Student       Course      Cr.           Grade      Course     Cr.           Grade   Grade Pt.")
    print(page_number, "        Name          ID #1       Hrs    Grade    Pts       ID #2     Hrs    Grade    Pts    Average",)
    print( "___________________________________________________________________________________________________")
 
#def Earned Grade Points = credit hrs * grade, both courses
def earned_grade_points(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return round(num1 * num2, 1)
    

#def student's GPA = sum of grade points / sum of credit hours
def students_gpa(num_c, num_d, num_e, num_f):
    num_c = float(num_c)
    num_d = float(num_d)
    num_e = float(num_e)
    num_f = float(num_f)
    return round((num_c + num_d)/(num_e + num_f), 2)

def sum_column_variables(col_var_1, col_var_2):
    col_var_1 = float(col_var_1)
    col_var_2 = float(col_var_2)
    sum_col_1 = 0
    sum_col_2 = 0
    sum_col_1 += float(col_var_1)
    sum_col_2 += float(col_var_2)
    total_sum = sum_col_1 + sum_col_2
    return total_sum

'''if col_var_1 != 0:
            sum_col_1 += float(col_var_1)
    if col_var_2 != 0:
            sum_col_2 += float(col_var_2)
    total_sum = sum_col_1 + sum_col_2
    '''


#global variables go here
student_COUNTER = 0
line_COUNTER = 0
lines_per_PAGE = 20
total_credit_hours = 0
total_earned_grade_pts = 0
page_number = 1

page_header()        
print_col_header()
column_widths = [50, 15, 10, 10, 10, 15, 10, 10, 10, 10]

with open("C:\\Users\\lavok\Desktop\\Liz\\CIS 150\\GradePtsFile.txt") as file:   # open file
    for line in file:                                  # grabs entire line in file
        student_COUNTER += 1                           # adds one to counter
        current_line_string = line.strip()             # strips off the new line characters
        current_line = current_line_string.split(",")  # split the current line
        #columns = line.strip().split(',')
        #print(row_format.format(*columns))

        # pull individual data peices
        student_name = current_line[0]
        course_id_1 = current_line[1]
        credit_hrs_1 = float(current_line[2])
        grade_class_1 = float(current_line[3])
        course_id_2 = current_line[4]
        credit_hrs_2 = float(current_line[5])
        grade_class_2 = float(current_line[6])
    
        
        #grade_pts_1 = earned_grade_points(credit_hrs_1, grade_class_1) 
        #grade_pts_2 = earned_grade_points(credit_hrs_2, grade_class_2)
   
        #calc earned grade points 
        if (grade_class_1 != 0) and (grade_class_2 != 0):     
            grade_pts_1 = earned_grade_points(credit_hrs_1, grade_class_1)
            grade_pts_2 = earned_grade_points(credit_hrs_2, grade_class_2)
        else:
            continue
        
        line_COUNTER += 1
        if line_COUNTER % lines_per_PAGE == 0:
            page_number += 1

        # calc students GPA
        students_gradepointavg = students_gpa(grade_pts_1, grade_pts_2, credit_hrs_1, credit_hrs_2)

        # def accumulate final totals: total number of students, total of all credit hours, total of all earned grade points, overall GPA = total earned grade points / total credit hours
        number_students = student_COUNTER

        total_credit_hours += credit_hrs_1 + credit_hrs_2
        total_earned_grade_pts += grade_pts_1 + grade_pts_2

        overall_GPA = total_earned_grade_pts / total_credit_hours

        # print all items
        
        print(str(student_COUNTER).ljust(5), end=' ')
        print(str(student_name).ljust(15), end=' ')
        print(str(course_id_1).rjust(8), end=' ')
        print(str(credit_hrs_1).rjust(7), end=' ')
        print(str(grade_class_1).rjust(6), end=' ')
        print(str(grade_pts_1).rjust(8), end=' ')
        print(str(course_id_2).rjust(11), end=' ')
        print(str(credit_hrs_2).rjust(7), end=' ')
        print(str(grade_class_2).rjust(6), end=' ')
        print(str(grade_pts_2).rjust(8), end=' ')
        print(str(students_gradepointavg).rjust(8))
       

        # check that 20 students printed 
        # and if true, print header
        if (line_COUNTER % 20 == 0):
            print("\n\n\n")
            page_header()
            print_col_header()

    print('\n\n')
    print("The total number of students is", student_COUNTER)
    print("Total Credit Hours = ", total_credit_hours)
    print("Total Earned Grade Points = ", total_earned_grade_pts)
    print("Overall Grade Point Average = ", overall_GPA)      
    print('\n\n')
 

