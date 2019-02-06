#!/usr/bin/python3
""" Генератор последовательности Фибоначчи с помощью yield """

def fib(max):
    a, b = 0, 1          
    while a < max:
        yield a          
        a, b = b, a + b  

num = int(input("Enter max number: "))
# for n in fib(num):
#     print (n, end = ' ')
# print (list(fib(num))
l = list(fib(num))
print(l)