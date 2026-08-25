# Hackerrank Problem : Nested Lists
# Description : To print out the name alphabetically with the second lowest score

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
        
    scores = [record[1] for record in records]
    first_lowest = min(scores)
    score2= [x for x in scores if x!= first_lowest]
    second_lowest= min(score2)
    names = [record[0] for record in records if record[1] == second_lowest]
    for name in sorted(names):
        print(name)
