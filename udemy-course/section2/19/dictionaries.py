#!/usr/bin/python3.5
# Dictionaries contains key and values
pins = {"Mike":1234, "Joe":1111, "Jack":2222}
print(pins["Mike"])
print(pins.keys())
print(pins.values())
print(dir(dict))
list1 = [1, 2, 3]
list2 = ['firsts', 'second', 'third']
d = dict(zip(list1, list2))
print(d)