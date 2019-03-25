#!/usr/bin/python3.5

def count(string):
    if string:
        
        r = {i:string.count(i) for i in sorted(set(string))}
        # r = {i: string.count(i) for i in string}
        
        print(r)
        return r
    return {}

count('aba')

count('sdasd')