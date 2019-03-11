#!/usr/bin/python3.5

import glob2
from datetime import datetime
content = ''

def reader(f_path):
    with open(f_path, 'r') as rfile:
        return rfile.read()

def writer(content, f_name):
    with open('udemy-course/section3/71/{}.txt'.format(f_name), 'w') as myfile:
        myfile.write(content)

f_list = glob2.glob('udemy-course/section3/71/file*.txt')
f_list.sort()
f_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')

for f in f_list:
    content += reader(f) + '\n'

writer(content, f_name)
