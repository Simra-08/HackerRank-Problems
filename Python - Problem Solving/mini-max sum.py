# Hackerrank Problem : Mini Max Sum
# Description : To get the max and min possible sum of elements in an array

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    asc_sum = arr[0]+arr[1]+arr[2]+arr[3]
    
    
    desc_sum = arr[4]+arr[3]+arr[2]+arr[1]
    
    print(asc_sum , desc_sum)
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
