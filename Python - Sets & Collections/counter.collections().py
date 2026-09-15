# Hackerrank Problem : Counter.Collections()
# Description : To use the counter concept to determine the total price 
# obatined by the customers on buying a specific shoe size

X = int(input())
shoe_sizes = list(map(int,input().split()))
no_of_customers = int(input())
count = 0
for i in range(no_of_customers):
    shoe_size , price = list(map(int,input().split()))


       
    if shoe_size in shoe_sizes:
        count += price
        shoe_sizes.remove(shoe_size)
        
print(count)   


#counter version
# if shoe_sizes[shoe_size] > 0:
#     count += price
#     shoe_sizes[shoe_size] -= 1