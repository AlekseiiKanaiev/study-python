#!/usr/bin/python3.5

import json
from difflib import get_close_matches as gcm

# help(json)
# print (dir(json))

data = json.load(open('data.json'))
# print(data['rain'])
# print(data.keys())
# with open('example.txt', 'w') as f:
#     for line in list(data.keys()):
#         f.write(line+'\n')

def translate(word):
    if word in data:
        return '\n'.join(data[word])
    elif word.capitalize() in data:
        return '\n'.join(data[word.capitalize()])
    elif gcm(word, list(data.keys()), n = 1, cutoff = 0.8):
        c_word = ''.join(gcm(word, list(data.keys()), n = 1, cutoff = 0.8))
        answer = input("Didn't find word, did you mean '{}' instead '{}'?\n".format(c_word, word)\
                       +"Y/N: ") 
        return '\n'.join(data[c_word]) if answer.upper() == 'Y' else main()
    else: 
        return "The word does not exist!"

def main():
    word = input('Enter word: ')
    print(translate(word.lower()))
    exit('Thanks!')

if __name__ == "__main__":
    main()