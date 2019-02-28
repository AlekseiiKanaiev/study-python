#!/usr/bin/python3.5

myfile = open('udemy-course/section2/7/sample.txt')
print(type(myfile))
print(dir(myfile))

content = myfile.read()
print('Content:\n'+content)
print(type(content))

after = myfile.read()
print('After:\n '+after)
print(type(after))

myfile.seek(0)
print('After seek:\n'+myfile.read())
    
# good practice
myfile.close()

