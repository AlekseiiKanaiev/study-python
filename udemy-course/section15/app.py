#!/usr/bin/python3.5
import cv2
import sys
print(cv2.__version__)
path = sys.path[0]+'/'
img_name = 'galaxy.jpg'

# second paramter is num: what color do you want to read your image 
# (0-for gray scale, 1-for rgb scale, -1 for gray scale but with transparancy)
img = cv2.imread(path+img_name, 0)

print(type(img))
# <class 'numpy.ndarray'>
print(img) 
# how many columns and rows
print(img.shape)
# number of dimentials
print(img.ndim)

cv2.imshow('Galaxy', img)
# time to window will be close
# 0-when the user press any button, the window will be close
# other value represents ms
cv2.waitKey(2000)
cv2.destroyAllWindows()