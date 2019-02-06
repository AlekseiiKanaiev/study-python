#!/usr/bin/python3.5
import sys
import os
from dictionary import Dictionary

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: enter name of text-file after name of your programm")
    dictionary_way = os.path.join(sys.path[0], "test.txt")
    text_way = os.path.join(sys.path[0], sys.argv[1])
    dictionary = Dictionary()
    if not dictionary.load(dictionary_way):
        sys.exit("Could not load dictionary")
    word = ""
    words, miss = 0, 0
    with open(text_way, "r") as text:
        for line in text:
            for letter in line:
                if letter.isalpha() or (letter == "\'" and len(word) > 0):
                    word += letter.lower()
                elif len(word) > 0:
                    words += 1
                    if not dictionary.check(word):
                        print(word)
                        miss += 1
                    word = ""
            
    print ("{}\n{}\n{}".format(miss, dictionary.size(), words))
if __name__ == "__main__":
    main()  
