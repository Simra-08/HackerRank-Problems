# Hackerrank Problem : Runner Up Score
# Description : To find out the second runner up score in an array 

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    
    my_set =sorted(arr,reverse=True)
    my_list = list(my_set)
    
    

    print(my_list[1])
    
    
   