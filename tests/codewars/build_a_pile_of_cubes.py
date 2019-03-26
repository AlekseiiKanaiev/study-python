#!/usr/bin/python3.5

# 

# def s(n):
#     r = 0
#     for i in range(n+1):
#         r += pow(i, 3)
#     print(r)

# s(45)
def findNb(num):
    r = 0
    while num > 0:
        num -= pow(r, 3)
        r += 1
    print(r-1 if num == 0 else -1)
    return r-1 if num == 0 else -1


findNb(1071225)
findNb(91716553919377)