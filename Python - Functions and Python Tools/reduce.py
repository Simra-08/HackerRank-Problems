# Hackerrank Problem : Reduce
# Description : To print the multiplication of fractions using reduce()
# that in a collection of numbers it repeatedly performs the operation


from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y : x*y,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
