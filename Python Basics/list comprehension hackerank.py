# Hackerrank Problem : List Comprehension
# Description : To print out the all possible [i,j,k] combinations within the given range except those where i+j+k == n
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    numbers = [x,y,z]
    elements = [[i,j,k] for i in range(0,x+1) for j in range(y+1) for k
    in range(0,z+1) if i+j+k!=n]
     
    print(elements)
    