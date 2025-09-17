# Hackerrank Problem : Swap Case 
# Description : To sawp the upper and lower cases of a given input

def swap_case(s):
    return s.swapcase()

    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)