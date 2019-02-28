#!/usr/bin/python3.5

fruits = open('udemy-course/section2/43/fruits.txt')
for i in fruits.readlines():
    print(len(i.strip()))
fruits.close()

def temp_conv(temp):
    return temp*9/5+32

temperatures = [10, -20, 100]
for t in temperatures:
    print(temp_conv(t))