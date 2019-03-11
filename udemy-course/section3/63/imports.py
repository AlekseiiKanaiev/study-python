#!/usr/bin/python3.5

import os
# help (os)
print (dir(os))
print('Files in dirrectory: \n', os.listdir())

# using sudo pip3 install glob2
import glob2
help(glob2)
print (dir(glob2))
print(glob2.glob('*'))