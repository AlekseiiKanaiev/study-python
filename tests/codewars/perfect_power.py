#!/usr/bin/python3.5

from math import log, floor

def isPP(n):
    for i in range(2, n):
#         print(i)
        # print (log(n, i))
        if round(log(n, i), 7).is_integer() and log(n, i) > 1:
            print ([i, int(round(log(n, i)))])
            return [i, int(round(log(n, i)))]
    print(1)
    return None
    #your code here

isPP(4)
n = 629763392149
r = isPP(n)
# print(r[0]**r[1])
print(pow(229, 5))
print(log(n, 229))
print(round(log(n, 229), 7))