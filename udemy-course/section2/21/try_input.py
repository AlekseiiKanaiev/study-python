#!/usr/bin/python3.5

user_input = input("Enter a number: ")
try:
    print(int(user_input)*2)
except:
    print("You enter not a number")