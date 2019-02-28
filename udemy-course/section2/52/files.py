#!/usr/bin/python3.5

# help(open)

myfile = open('udemy-course/section2/52/employee.txt', 'w')
myfile.write('Henry')
myfile.writelines(['Jack', 'Sam'])
myfile.close()
# rewriting file
myfile = open('udemy-course/section2/52/employee.txt', 'w')
myfile.write('Henry')
myfile.close()
# adding file
myfile = open('udemy-course/section2/52/employee.txt', 'a')
myfile.write('Sam')
myfile.close()
# but we cannot read this files
# solution
myfile = open('udemy-course/section2/52/employee.txt', 'a+')
# first we go to first line
myfile.seek(0)
print(myfile.read())
# if we now add smth it append to the end of the file
myfile.write('Joe')
myfile.close()