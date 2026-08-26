# Hackerrank Problem : Nested Lists
# Description : To print out the name alphabetically with the second lowest score

if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name,score])
        
        
    for i in students:
        scores.append(i[1])
        my_set = sorted(set(scores))
        my_list = list(my_set)
            
    second_lowest = my_list[1]
    
    names = []
    for i in students:
        if i[1] == second_lowest:
            names.append(i[0])
    names.sort()
    
    for name in names:
        print(name)        
            