# Hackerrank Problem : Breaking the Record
# Description : To find out how many times has highest and lowest record score
# been broken

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    count1 = 0
    count2 = 0
    highest = scores[0]
    lowest = scores[0]
    for i in scores:
        if i > highest:
            count1 += 1
            highest = i
        
        if i < lowest:
            count2 += 1
            lowest = i  
    return count1 , count2                                   
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
