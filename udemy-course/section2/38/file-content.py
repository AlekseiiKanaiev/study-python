#!/usr/bin/python3.5

myfile = open('udemy-course/section2/7/sample.txt')
content = myfile.read().splitlines()
print(content)
print(type(content))
myfile.close()
fruits = open('udemy-course/section2/38/fruits.txt')
print(fruits.read())
fruits.close()

