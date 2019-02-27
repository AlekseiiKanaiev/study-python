#!/usr/bin/python3.5

try:
    usr_input = float(input("Enter number: "))
except:
    print("Enter only number!")
    exit(0)
if usr_input > 100: 
    print("greater")
elif usr_input == 100: 
    print("equal")
else:
    print("smaller")