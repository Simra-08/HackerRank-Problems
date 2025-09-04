# Hackerrank Problem : if-else
# Description : Check if n is even or odd and print out certain texts

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    def checking():
            
            if n % 2 != 0 :
                return ("Weird")
            elif 2 <= n <= 5 and n % 2 == 0 :
                    return ("Not Weird")
            elif 6 <=n <=20 and n % 2 == 0 :
                        return ("Weird")
            elif n > 20 and n % 2 == 0 :
                            return ("Not Weird")
                            
    print (checking())   
    