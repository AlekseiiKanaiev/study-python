#!/usr/bin/python3.5
import sys
import json
from difflib import get_close_matches as gcm

# sys.getdefaultencoding()
path = sys.path[0]+'/'
data = json.load(open(path + 'data.json'))
print(len(data.keys()))


def normalize_strs(arr):
    return '\n'.join(list(map(lambda s:\
        s.encode(encoding = 'ascii', errors = 'replace').decode('ascii'), arr)))

def translate(word):
    words = (data.keys())
    # print(words)
    for el in words:
        if word.lower() == el:
            return normalize_strs(data[word.lower()])
        elif word.capitalize() == el:
            return normalize_strs(data[word.capitalize()])
        elif word.upper() == el:
            return normalize_strs(data[word.upper()])
    if gcm(word, words, n = 1, cutoff = 0.6):
        c_word = ''.join(gcm(word, list(data.keys()), n = 1, cutoff = 0.6))
        answer = input("Didn't find word, did you mean '{}' instead '{}'?\n"\
                .format(c_word.encode('ascii', errors='replace').decode('ascii'), word)\
                +"Y/N: ")
        return normalize_strs(data[c_word]) if answer.upper() == 'Y' else main()
    else: 
        return "The word does not exist!"

def main():
    word = input('Enter word: ')
    print(translate(word))
    exit('Thanks!')

if __name__ == "__main__":
    main()