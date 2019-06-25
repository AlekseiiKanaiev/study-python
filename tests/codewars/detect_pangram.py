#!/usr/bin/python3.5

import string

def is_pangram(s):
#     for l in string.ascii_lowercase:
#         if s.lower().find(l) == -1:
#             return False
#     return True
    return False if ([l for l in string.ascii_lowercase if s.lower().find(l) == -1]) else True

is_pangram("The quick brown fox jumps over the lazy dog")