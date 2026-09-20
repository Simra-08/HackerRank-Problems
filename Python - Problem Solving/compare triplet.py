# Hackerrank Problem : Compare Triplets
# Description : To compare the triplets and reward marks accordingly 


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice_count = 0
    bob_count = 0
    for i in range (0,len(a)):
        
            if a[i] > b[i]:
                alice_count += 1
            elif a[i] < b[i]:
                bob_count += 1
            elif a[i] == b[i]:
                pass
                
    return [alice_count,bob_count]                                  
                
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
