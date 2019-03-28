#!/usr/bin/python3.5

import numpy
import sys
import cv2

path = sys.path[0]+'/'
img = cv2.imread(path+'smallgray.png', 0)
print(img)

# stack(concatenate) horisontaly
ar1 = numpy.hstack((img, img))
print(ar1)
# stack verticaly
ar2 = numpy.vstack((img, img))
print(ar2)
# you cannot stack array with different 

# split array horisontaly
# can split only by equal division (we have 5 columns, and can divide only by 1 or 5)
ar3 = numpy.hsplit(ar2, 5)
print(ar3)
ar4 = numpy.vsplit(ar2, 3)
print(ar4)