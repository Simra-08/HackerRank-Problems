# Hackerrank Problem : Word Count
# Description : To find the number of occurences of given n words


n = int(input())

words_list = []
for i in range(n):
    word = input()
    words_list.append(word)


words_set = set(words_list)
print(len(words_set))

words_dict = {}
count = 0
for i in words_list:
    if i in words_dict:
        words_dict[i] = words_dict[i] + 1
    else:
        words_dict[i] = 1        
        
for value in words_dict.values():
    print(value,end = " ")              
        