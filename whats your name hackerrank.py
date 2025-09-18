# Hackerrank Problem : What's your name
# Description : To print out the given input names with a given string
def print_full_name(first, last):
    print ("Hello " + first + " "+  last + "! You just delved into python. " )
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)