# Hackerrank Problem : Grading Students
# Description : To grade the students and round off the numbers based on 
# given condition



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    
    result =[]
   
    for grade in grades:
        for i in range (0,10):
             added_grade = grade + i   
             
             if added_grade % 5 == 0:  
                result.append(added_grade)  
                break 
                
    final_result = []                  
    for grade, added_grade in zip(grades, result):
        if grade < 38:
            final_result.append(grade)  
        elif added_grade - grade<3:
            final_result.append(added_grade)
          
        else:
            final_result.append(grade) 
    return final_result               
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
