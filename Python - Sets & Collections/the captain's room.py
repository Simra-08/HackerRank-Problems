# Hackerrank Problem : The Captain's Room
# Description : To find the room number of captain

K = list(map(int,input().split()))
room_number = list(map(int,input().split()))


frequency = {}
for i in room_number:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
        
        
for i in frequency:
    if frequency[i] == 1:
        print(i)     