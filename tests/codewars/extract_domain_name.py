#!/usr/bin/python3.5

import re

def domain_name(url):
    result = re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
    print (result)
    # result2 = re.findall(r'[^www\.]([\w+-])', ''.join(result))
    # print (result2)
    return result

domain_name("http://github.com/carbonfive/raygun")
domain_name("http://www.zombie-bites.com")
domain_name("https://www.cnet.com")