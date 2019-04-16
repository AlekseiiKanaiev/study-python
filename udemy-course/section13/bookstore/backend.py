"""
The programm that stores book information:
Title, author, year and isbn

You can:
View all records
Search an entry
Add entry
Delete selected
Update selected
Close application
"""
#!/usr/bin/python3.5
import sys
import sqlite3

path = sys.path[0]+'/'
connection = 'books.db'
table = ''
columns = []

def create_table(name):
    with sqlite3.connect(connection) as con:
        con.execute('CREATE TABLE IF NOT EXISTS '+name+\
            ' (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
        con.commit()
        return name

def get_table(name):
    with sqlite3.connect(connection) as con:
        tables = con.execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall()[0]
        return tables[tables.index(name)] if name in tables else create_table(name)

# def get_columns(table):
#     con = sqlite3.connect(path+'books.db')
#     cur = con.execute('SELECT * FROM '+table)
#     columns = [desc[0] for desc in cur.description]
#     con.close()
#     return columns

def view_data():
    if table:
        with sqlite3.connect(connection) as con:
            return con.execute('SELECT * FROM '+table).fetchall()

def add_data(data):
    if table:
        with sqlite3.connect(connection) as con:
            try:
                title = data['title']
                author = data['author']
                year = int(data['year'])
                isbn = int(data['isbn'])
            except:
                return False

            con.execute('INSERT INTO '+table+' VALUES (NULL, ?, ?, ?, ?)',\
                (title, author, year, isbn))
            con.commit()
            return True

def search_data(column, data):
    if table:
        with sqlite3.connect(connection) as con:
            data = '%'+data+'%'
            return con.execute('SELECT * FROM '+table+' WHERE '+column+' LIKE ?', (data, )).fetchall()

def delete_data(id):
    if table:
        with sqlite3.connect(connection) as con:
            con.execute('DELETE FROM '+table+' WHERE id = ?', (id, ))
            con.commit()

def update_data(id, data):
    if table and data:
        with sqlite3.connect(connection) as con:
            for key, value in data.items():
                con.execute('UPDATE '+table+' SET '+key+' = ? WHERE id = ?', (value, id))
                con.commit()
        
table = get_table('book')
# print(table)
# columns = get_columns(table)
# print(columns)
# data = {'id': 5, 'title': 'Hello', 'author': 'World', 'year': 2019, 'isbn': 0000}
# add_data(data)
# delete_data('5')
# data = {'title': 'The sea'}
# update_data(1, data)
# print(view_data())
# print(search_data('title', 'Th'))


