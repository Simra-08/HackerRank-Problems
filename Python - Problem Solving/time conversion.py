# Hackerrank Problem : Time Conversion
# Description : To convert 12 hour format into 24 hour format



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0:2])
    minute = s[3:5]    
    second = s[6:8]
    period = s[8:10]
    
    
        
    if period == "AM" and hour == 12:
        return '00' + ":" + minute + ":" + second 
   
    elif period == "PM" and hour == 12:
        return '12' + ":" + minute + ":" + second      
        
    elif period == "AM":
        return f"{hour:02d}:{minute}:{second}"        
        

        
    else:
        return str(hour+12) + ":" + minute + ":" + second   
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
