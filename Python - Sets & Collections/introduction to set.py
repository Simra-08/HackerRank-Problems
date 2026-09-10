# Hackerrank Problem : Introduction to set
# Description : To find the average of heights using set concept

def average(array):
    count = 0
    my_set = set(array)
    
    for i in my_set:
        count += i
    return(f"{count/len(my_set):.3f}")              
           

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)