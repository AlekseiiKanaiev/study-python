#!/usr/bin/python3.5

def string_len(s):
    print(type(s))
    return len(s) if type(s) is str else 'Not a string'

print(string_len(2))