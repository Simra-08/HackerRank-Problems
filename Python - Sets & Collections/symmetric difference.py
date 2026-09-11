# Hackerrank Problem : Syemmetric Difference
# Description : To print the symmmetric difference of two sets in an ascending
#               order

M = list((map(int,input().split())))
m_set = set(map(int,input().split()))
N = list(map(int,input().split()))
n_set = set(map(int,input().split()))

a = m_set.difference(n_set)
b = n_set.difference(m_set)


count1 = []
for x in a:
    count1.append(x)
    
    
count2 = []    
for y in b:
    count2.append(y)
    
final_count = count1+count2

final_count = sorted(final_count)
for z in final_count:
    print(z)
