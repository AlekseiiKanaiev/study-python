#!/usr/bin/python3.5
# import datetime object from datetime module
from datetime import datetime
print (dir(datetime))
delta = datetime.now() - datetime(1990, 10, 15)
print (delta.days, delta.seconds)
then = datetime.strptime('2004-12-31', '%Y-%m-%d')
print (then)
then = datetime.strptime('2004:12:31:12:40:15', '%Y:%m:%d:%H:%M:%S')
print (then)
print (then.strftime('%Y'), then.strftime('%m'), then.year, then.month)