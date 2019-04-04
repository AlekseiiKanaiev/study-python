#!/usr/bin/python3.5
import sys
import json
from difflib import get_close_matches as gcm

# path = sys.path[0]+'/'
# data = json.load(open(path + 'data.json'))
# # print(data.keys())

# def translate(word):
#     for el in data.keys():
#         print(el)
#         if word.lower() == el:
#             return '\n'.join(data[word.lower()])
#         elif word.capitalize() == el:
#             return '\n'.join(data[word.capitalize()])
#         elif word.upper() == el:
#             return '\n'.join(data[word.upper()])
#     if gcm(word, list(data.keys()), n = 1, cutoff = 0.6):
#         c_word = ''.join(gcm(word, list(data.keys()), n = 1, cutoff = 0.6))
#         answer = input("Didn't find word, did you mean '{}' instead '{}'?\n".format(c_word, word)\
#                     +"Y/N: ")
#         return '\n'.join(data[c_word]) if answer.upper() == 'Y' else main()
#     else: 
#         return "The word does not exist!"

# def main():
#     word = input('Enter word: ')
#     print(translate(word))
#     exit('Thanks!')

# if __name__ == "__main__":
#     main()

path = sys.path[0]+'/'
data = json.load(open(path + 'data.json'), encoding = 'utf-8')

b = b'hello'
l = [b, 'hello']
for el in l:
    print(el)