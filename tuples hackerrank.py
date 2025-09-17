# Hackerrank Problem : Tuples
# Description : To read the integers, convert them to tuple and print their hash value

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
    