#!/usr/bin/python3.5

myfile = open('udemy-course/section3/67/sample.txt', 'w')
myfile.write('something')
myfile.close()

# but recomended
# we don't have to write close() method and all work with file are separate
with open('udemy-course/section3/67/sample.txt', 'w') as myfile:
    myfile.write('Else')
