#!/usr/bin/python3.5

cor_pass = 'Python123'
user_name = input('Please, enter your name: ')
user_surname = input('Please, enter your surname: ')
user_input = input('Please enter password: ')

while cor_pass != user_input:
    user_input = input('Wrong password! Please enter password: ')

# print('Hi, %s, you are logged in' %user_name)
print ('Hi, {1} {0}, you are logged in'.format(user_name, user_surname))