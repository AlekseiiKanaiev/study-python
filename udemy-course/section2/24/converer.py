#!/usr/bin/python3.5

def converter(unit, coef=0.56):
    return unit*coef

print(converter(5))
print(converter(2,4))

def temp_conv(t):
    return t*9/5+32

print(temp_conv(25))
