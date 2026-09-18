# Hackerrank Problem : Any or All
# Description : To print boolean if all numbers are positive and contain any one 
# palindromic number using any and all

N = int(input())
integers = list(map(int,input().split()))

if all( i>0 for i in integers) and any (str(i)[0:]==str(i)[::-1]for i in integers):
    print(True)
else:
    print(False)    
