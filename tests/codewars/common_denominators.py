#!/usr/bin/python3.5
from functools import reduce

def convertFracts(lst):
    r = lst
    d = denominator([el[1] for el in r])
    # for el in r:
    #     el[0] *= int(d/el[1])
    #     el[1] = d
    r = [[num*int((d/den)), d] for num, den in r]
    print(r)
    return r

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    c =  a*b
    while b:      
        a, b = b, a % b
        print('while: ', a, b)
    print('gcd: ', a)
    return c // a

def denominator(lst):
    print(lst)
    d = reduce(gcd, lst)
    print(d)
    return d

# def denominator(lst):
#     lst.sort()
#     d = lst.pop()
#     print(lst)
#     r = d
#     print(d)
#     # print(all(d % el == 0 for el in lst))
#     while not all(d % el == 0 for el in lst):
#         d += r
#         # for el in lst:
#         #     print(d, el)
#         #     if d % el != 0:
#         #         d += r
#         #         s = False
#         #         break
#         #     s = True
#     return d

# denominator([3,3,4])


# def gcd(a, b):
#     """Return greatest common divisor using Euclid's Algorithm."""
#     while b:      
#         a, b = b, a % b
#         print('while: ', a, b)
#     print('gcd: ', a)
#     return a

# def lcm(a, b):
#     """Return lowest common multiple."""
#     print('lcm: ', a,b)
#     return a * b // gcd(a, b)

# def lcmm(*args):
#     """Return lcm of args."""
#     print(args)   
#     return reduce(lcm, args)

# def convertFracts(lst):
#     new_den = lcmm(*[den for num, den in lst])
#     print(new_den)
#     return [[num * (new_den / den), new_den] for num, den in lst]

a = [[1, 3], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
c = [[69, 130], [87, 1310], [3, 4]]
d = [[77, 130], [84, 131], [3, 4]]
e = [[8, 15], [7, 111], [4, 25]]
convertFracts(a)
# gcd(4, 1310)