#!/usr/bin/python3.5
import sys
# import os
import numpy
import cv2
# 0 -meams you want to read image in grey scale, 1 - you want to read image in bgr
#OpenCV uses BGR instead RGB

# in gray scale 0 is black and 255 is white 
ig = cv2.imread(sys.path[0]+'/smallgray.png', 0)
print(ig)
print(type(ig))
print(ig[0][0])

# in bgr we get 3 dimension array, each subarray represents BGR respectively
ig_1 = cv2.imread(sys.path[0]+'/smallgray.png', 1)
print(ig_1)

cv2.imwrite(sys.path[0]+'/newsmallgray.png', ig)