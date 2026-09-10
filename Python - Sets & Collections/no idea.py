# Hackerrank Problem : No Idea!
# Description : To add +1 if array element found in set A and -1 if found in set B


n, m = map(int, input().split())
arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

add = 0
count = 0
for i in arr:
    if i in A:
        add += 1
        
for i in arr:
    if i in B:
        count += 1
        
        
print(add - count)        
        