#!/usr/bin/python3.5
# SyntaxError
# print 4
# a = [1,2,3}
# int (4

# NameError
# print(d)

# ZeroDivisionError
# c = 4/0

# Handling Errors:

def divide(a,b):
    try: 
        return a/b
    except ZeroDivisionError:
        return 'Zero'

a = 1
b = 0
print(divide(a,b))