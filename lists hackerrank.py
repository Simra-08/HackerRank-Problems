# Hackerrank Probelem : Lists
# Description : To carry out the commands given by the user and print them

if __name__ == '__main__':
    N = int(input())
    arr=[]
    for _ in range (N):
        command = input().split()
        op = command[0]
        if op == "insert":
            arr.insert(int(command[1]) , int (command[2]))
        elif op == "print":
            print(arr)
        elif op == "remove":
            arr.remove(int(command[1]))
        elif op == "append":
            arr.append(int(command[1]))
        elif op == "sort" :
            arr.sort()
        elif op == "pop":
            arr.pop()
        elif op == "reverse":
            arr.reverse()     

