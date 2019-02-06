#!/usr/bin/python3.5

class Dictionary():
    def __init__(self):
        self.dictionary = set()
    def load(self, dictionary):
        with open(dictionary, "r") as fp:
            for line in fp:
                self.dictionary.add(line.lower().strip())
        return True
    def check(self, word):
        return word in self.dictionary
    def size(self):
        return len(self.dictionary)