# Hackerrank Problem : Zipped!
# Description : To find out the avegrage marks of students using zip() that 
# groups together elements at the same position from multiple iterables



N , X = list(map(int,input().split()))

numbers = []

for i in range(X) :
    row = list(map(float,input().split()))
    numbers.append(row)


x = (zip(*numbers))



for i in x:
    count = 0
    for j in i:
        count += j
    
    average = count/X
    
    print(average)