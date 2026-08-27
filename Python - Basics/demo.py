# numbers = [1,2,3,4,5,6,7,8]

# elements = [i*i for i in numbers if i%2!=0]

# print(elements)

numbers = [1,2,3,4,5,6,7,8]

elements = [i*2 if i%2==0 else i*3 for i in numbers]

print(elements)