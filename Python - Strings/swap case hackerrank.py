# Hackerrank Problem : Swap Case
# Description : To swap the upper case to lower case and vice versa

def swap_case(s):
    result = ""
    for i in s:
        if i.isupper():
            i = i.lower()
        elif i.islower():
            i = i.upper()  
        
        result += i
    return(result)
              
            
            
           

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)