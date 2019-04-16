#!/usr/bin/python3.5

import psycopg2
from psycopg2.extras import DictCursor
from tkinter import *
from difflib import get_close_matches as gcm

connection = "dbname = 'db2' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'"

def search_in_db(word = None):
    with psycopg2.connect(connection) as con:
        with con.cursor(cursor_factory = DictCursor) as cur:
            if word:
                cur.execute('SELECT dictionary.meaninig FROM dictionary WHERE word = %s', (word,))
                for el in cur:
                    return ''.join(el)
            else:
                cur.execute('SELECT dictionary.word FROM dictionary')
                return [''.join(i) for i in cur]


def find_meaning():
    t.delete(1.0, END)
    words = search_in_db()
    if word.get().lower() in words:
        t.insert(INSERT, search_in_db(word.get().lower()))
    elif word.get().capitalize() in words:
        t.insert(INSERT, search_in_db(word.get().capitalize()))
    elif word.get().upper() in words:
        t.insert(INSERT, search_in_db(word.get().upper()))
    else:
        c_word = ''.join(gcm(word.get(), words, n = 1, cutoff=0.6))
        if c_word:
            res = "Didn't find word, did you mean '{}' instead '{}'".format(c_word, word.get())
        else:
            res = "The word does not exist!"
        t.insert(INSERT, res)

window = Tk()

entlab = Label(window, text = 'Enter word')
entlab.grid(row =0, column = 0)

word = StringVar()
e1 = Entry(window, textvariable = word, width = 30)
e1.grid(row = 1, column = 0)

b = Button(window, text = 'Find', command = find_meaning)
b.grid(row = 1, column = 1)

tlab = Label(window, text = 'Meaning: ')
tlab.grid(row = 2, columnspan = 2)

t = Text(window)
t.grid(rowspan = 3, columnspan = 2)



# without it the window will open and close in 1s
window.mainloop()
