# Hackerrank Problem : String split and join
# Description : To join the string using a given delimeter

def split_and_join(line):
    a = line.split(" ")
    
    a = "-".join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)