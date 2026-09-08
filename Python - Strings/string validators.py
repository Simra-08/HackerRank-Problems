if __name__ == '__main__':
    s = input()
    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False            
            
    
    for char in s:
        if char.isalnum():
            has_alnum = True
            
        if char.isalpha():
            has_alpha = True
            
        if char.isdigit():
            has_digit = True
            
         
        if char.islower():
            has_lower = True
           
            
        if char.isupper():
            has_upper = True
   
    if has_alnum:
        print("True")
    else:
        print("False")
    if has_alpha:
        print("True")
    else:
        print("False")
    if has_digit:
        print("True")
    else:
        print("False")
    if has_lower:
        print("True")
    else:
        print("False")
    if has_upper:
        print("True")
    else:
        print("False")
                                   
        