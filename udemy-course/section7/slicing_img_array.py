#!/usr/bin/python3.5

import numpy
import sys
import cv2

img = cv2.imread(sys.path[0]+'/smallgray.png', 0)
print(img)
print(img.shape)
print(img[0:2, 2:4])
print(img[2, 4])
for i in img.T:
    print(i)
for i in img.flat:
    print(i)
    