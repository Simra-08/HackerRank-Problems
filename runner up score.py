# Hackerrank Problem : Runner Up Score
# Description : To find out the second runner up score in an array 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = max(arr)
    arr = [x for x in arr if x != max_score]
    max_score = max(arr)
    print(max_score)
   