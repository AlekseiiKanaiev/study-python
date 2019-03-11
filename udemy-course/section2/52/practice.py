#!/usr/bin/python3.5

mylist = [1,2,3]
myfile = open('udemy-course/section2/52/practice.txt', 'a+')
myfile.writelines(map(lambda x: str(x)+'\n', mylist))
myfile.close()
# print(dir(list))