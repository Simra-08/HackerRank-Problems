# Hackerrank Problem : Map and Lambda Function
# Description : To use map and lambda function

cube = lambda x: x*x*x
def fibonacci(n):
    fib = []
    if n == 1:
        return [0]
    if n == 0:
        return []    
    n1 = 0
    n2 = 1
    count = 0 
    fib.insert(0,0)
    fib.insert(1,1)   
    for i in range (0,n-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        
        fib.append(n3)
    return fib
        
        
    
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))