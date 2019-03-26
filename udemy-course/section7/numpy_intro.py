#!/usr/bin/python3.5

import numpy


# create simple array
n = numpy.arange(27)
print(n)
print(type(n))

# create 2 dimension array
n2 = n.reshape(3, 9)
print(n2)

# create 3 dimension array
n3 = n.reshape(3, 3, 3)
# print(n3)

l = [[123, 3213, 452, 4, 51],[],[]]
m = numpy.asarray(l)
print(m)
print(type(m) == type(l))