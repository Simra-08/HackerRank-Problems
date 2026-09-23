# Hackerrank Problem : Plus Minus
# Description : To print the ratio of positive, negative and zero numbers present
# in the given array

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_list = []
    negative_list = []
    zero_list = []
    for i in arr:
        if i > 0 :
            positive_list.append(i)
    for i in arr:
        if i < 0 :
            negative_list.append(i)        
    for i in arr:
        if i == 0:
            zero_list.append(i)
    
    pos_ratio = len(positive_list)/len(arr)
    neg_ratio = len(negative_list)/len(arr)  
    zero_ratio = len(zero_list)/len(arr) 
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")         
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
