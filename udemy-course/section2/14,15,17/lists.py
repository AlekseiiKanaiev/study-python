#!/usr/bin/python3.5

address = ["Flat Floor Street", 18, "New York"]
print(address[0], address[1])
print(len(address))
string = "hello"
print(string[0], len(string))
# "New York"
print(address[-1])
# Slicing
print(address[0:2])
print(address[-2:])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# From first to second-to-last
print(days[:-1])

# METHODS like built-in function, but only for exactly types
print("LIST: \n", dir(list))
address.append("USA")
print(address)
address.remove("USA")
print(address)
address.pop()
print(address)
print("Hello"[-3:-1])