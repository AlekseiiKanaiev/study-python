#!/usr/bin/python3.5
import sys
import json
import psycopg2
from psycopg2.extras import DictCursor
from difflib import get_close_matches as gcm

# sys.getdefaultencoding()
path = sys.path[0]+'/'
data = json.load(open(path + 'data.json'))
connection = "dbname = 'db2' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'"

def normalize_strs(arr):
    return '\n'.join(list(map(lambda s:\
        s.encode(encoding = 'ascii', errors = 'replace').decode('ascii'), arr)))

# norm_keys = normalize_strs(data.keys())
# norm_values = ['\n'.join(normalize_strs(value)) for value in data.values()]

def create_table():
    conn = psycopg2.connect(connection)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS dictionary (word TEXT, meaninig TEXT)')
    conn.commit()
    conn.close()

def add_data(word):
    conn = psycopg2.connect(connection)
    cur = conn.cursor()
    cur.execute('INSERT INTO dictionary VALUES (%s, %s)',\
        (word.encode(encoding = 'ascii', errors = 'replace').decode('ascii'), normalize_strs(data[word])))
    conn.commit()
    conn.close()

def view_data(word):
    with psycopg2.connect(connection) as conn:
        with conn.cursor(cursor_factory = DictCursor) as curs:
            cur1 = curs.execute('SELECT dictionary.meaninig FROM dictionary WHERE word = %s', (word,))
            cur2 = curs.execute('SELECT dictionary.word FROM dictionary')
            print(cur2)
word = 'do'
# print(normalize_strs(data[word]))
# create_table()
# for word in data.keys():
#     add_data(word)
view_data(word)