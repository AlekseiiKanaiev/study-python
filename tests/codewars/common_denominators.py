#!/usr/bin/python3.5

def convertFracts(lst):
    r = lst
    d = denominator([el[1] for el in r])
    for el in r:
        el[0] *= int(d/el[1])
        el[1] = d
    print(r)
    return r

def denominator(lst):
    lst.sort()
    d = lst.pop()
    r = d
    print(lst)
    # print(all(d % el == 0 for el in lst))
    while not all(d % el == 0 for el in lst):
        d += r
        # for el in lst:
        #     print(d, el)
        #     if d % el != 0:
        #         d += r
        #         s = False
        #         break
        #     s = True
    print(d)
    return d

# denominator([2,3,4])
a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
c = [[69, 130], [87, 1310], [3, 4]]
d = [[77, 130], [84, 131], [3, 4]]
convertFracts(a)