# Hackerrank Problem : Find a String
# Description : To check for a sub string in a given string

def count_substring(string, sub_string):
    count = 0
    for i in range (0,len(string)+1):
        if sub_string == string[i:i+len(sub_string)]:
            count+=1
    return count            
    
  
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)