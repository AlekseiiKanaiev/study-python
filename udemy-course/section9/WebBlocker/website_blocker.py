#!/usr/bin/python3.5

import sys
import time 
from datetime import datetime as dt
import re

# hosts_path = '/etc/hosts'
hosts_path = sys.path[0]+'/Hosts/hosts'
redirect = '127.0.0.1'

try:
    with open(sys.path[0]+'/blocked_websites.txt', 'r') as f:
        websites = f.read().splitlines()
except FileNotFoundError:
    print('Could not fint the file! Use standart lit of the websites!')
    websites = ['www.facebook.com', 'facebook.com', 'www.youtube.com', 'youtube.com', '1']
print(websites)

p = re.compile(r'\bfacebook\.com\b')
print("facebook.com" in websites)


while True:
    now = dt.now()
    if dt(now.year, now.month, now.day, 8) < dt.now() < dt(now.year, now.month, now.day, 16, 30):
        print(dt.strftime(dt.now(), "%H:%M:%S"))
        print('Working hours...')
        with open(hosts_path, 'r+') as f:
            content = f.read()
            
            for w in websites:
                if not w in content.split():
                    print(w)
                    f.write('\n'+redirect+' '+w)
                else:
                    f.seek(0)
                    for line in content.split('\n'):
                        if not w in line.split():
                            f.write(line+'\n')
                    f.truncate()
                    
    # delay in seconds!!!
    time.sleep(30)
