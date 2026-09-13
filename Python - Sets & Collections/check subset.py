# Hackerrank Problem : Check Subset
# Description : To check for subset based on given number of test cases

T = int(input())

for i in range(T):
    number_of_elements_in_a = int(input())
    set_A = set(map(int,input().split()))
    number_of_elements_in_b = int(input())
    set_B = set(map(int,input().split()))


    if set_A.issubset(set_B):
        print(True)
    else:
        print(False)    

