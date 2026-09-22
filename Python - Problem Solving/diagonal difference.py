# Hackerrank Problem : Diagonal Difference
# Description : To get the absolute difference by the sum of left and right
# diagonal elements

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    count1 = 0
    count2 =0
    for i in range (len(arr)):
        
        count1 += arr[i][i]
        count2 += arr[i][len(arr)-1-i]
    return abs(count1-count2)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
