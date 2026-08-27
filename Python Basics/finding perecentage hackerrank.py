# Name : Finding percentage
# Description : To find out the average of the given person from a dictionary containing lists 
#                as values

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks:
        if i == query_name:
            wanted_marks = student_marks[query_name]
            average = (wanted_marks[0]+wanted_marks[1]+wanted_marks[2])/3
            print(f"{average:.2f}")
    