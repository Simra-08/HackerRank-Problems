# Hackerrank Problem : Set Mutations
# Description : Solved HackerRank’s Set Mutations problem by taking a main set and performing multiple operations on it, such as intersection update, union/update, symmetric difference, 
# and difference update, then finding the sum of the final set.

A = list(map(int,input().split()))
set_A = set(map(int,input().split()))
N = int(input())


for i in range(N):
    operation , operation_number = input().split()
    operation_set = set(map(int,input().split()))
    
    if operation == "intersection_update":
        set_A.intersection_update(operation_set)
    elif operation == "update":
        set_A.update(operation_set)
    elif operation == "symmetric_difference_update":
        set_A.symmetric_difference_update(operation_set)
    elif operation == "difference_update":
        set_A.difference_update(operation_set)            

set_A = list(set_A)
count = 0
for i in set_A:
    count+=i
print(count)   