#!/usr/bin/python3.5

import pandas

print(type(pandas))
dir_pandas = dir(pandas)
print(dir_pandas)

df = pandas.DataFrame([[2,3,4], [10,20,30]])
print(type(df))
print(dir(df))

with open('udemy-course/section6/pandas/dir_pandas.py', 'w') as pf:
    for line in dir_pandas:
        pf.write(line+'\n')

with open('udemy-course/section6/pandas/dir_pandas_series.txt', 'w') as psf:
    for line in dir(df):
        psf.write(line+'\n')