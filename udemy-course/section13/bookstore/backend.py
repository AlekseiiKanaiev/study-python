#!/usr/bin/python3.5
import sys
import sqlite3

path = sys.path[0]+'/'
connection = path + 'books.db'
table = ''
columns = []

def get_table():
    con = sqlite3.connect(connection)
    cur = con.cursor()
    cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
    res = cur.fetchone()[0]
    con.close()
    return res

# def get_columns(table):
#     con = sqlite3.connect(path+'books.db')
#     cur = con.execute('SELECT * FROM '+table)
#     columns = [desc[0] for desc in cur.description]
#     con.close()
#     return columns

def view_data():
    if table:
        con = sqlite3.connect(connection)
        cur = con.cursor()
        cur.execute('SELECT * FROM '+table)
        res = cur.fetchall()
        con.close()
        return res
    return 'No table found'

def add_data(data):
    if table:
        con = sqlite3.connect(connection)
        cur = con.cursor()
        try:
            id_n = int(data['id'])
            title = data['title']
            author = data['author']
            year = int(data['year'])
            isbn = int(data['isbn'])
        except:
            con.close()
            return False

        cur.execute('INSERT INTO '+table+' VALUES (?, ?, ?, ?, ?)',\
            (id_n, title, author, year, isbn))
        con.commit()
        con.close()
        return True
    return 'No table found'

def search_data(column, data):
    if table:
        con = sqlite3.connect(connection)
        cur = con.cursor()
        data = '%'+data+'%'
        print(data)
        cur.execute('SELECT * FROM '+table+' WHERE '+column+' LIKE ?', (data, ))
        res = cur.fetchall()
        con.close()
        return res
    return 'No table found'

def delete_data(data):
    if table:
        con = sqlite3.connect(connection)
        cur = con.cursor()

table = get_table()
# colums = get_columns(table)
# print(colums)
# data = {'id': 7, 'title': 'Hello', 'author': 'World', 'year': 2019, 'isbn': 0000}
# add_data(data)
# delete_data('')
# print(view_data())
print(search_data('title', 'Hey'))

