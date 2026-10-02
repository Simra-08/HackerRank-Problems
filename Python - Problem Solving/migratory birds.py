# Hackerrank Problem : Migratory Birds
# Description : To find out the bird type of highest count

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    frequency = {}
    for x in arr:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1
            
    highest = 0        
    for x in frequency:
        count = frequency[x]
        if count>highest:
            highest =count
            element = x
        elif count == highest and x<element:
            element = x
                        
    return element        
    
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
