# Hackerrank Problem : Apples and Oranges
# Description : To find out how many apples and oranges fall in
# the surroundings of sam's house

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_list = []
    b_list = []
    
    
    
    for i in apples:
        a_distance = a + i
        a_list.append(a_distance)
        
        
    for i in oranges:
        b_distance = b + i
        b_list.append(b_distance)
        
    count1 = 0
    count2 = 0
    
    for i in a_list:
        if i in range(s,t+1):
            count1 += 1
            
    for i in b_list:
        if i in range(s,t+1):
            count2 += 1  
            
    print(count1)
    print(count2)              
        
        
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
