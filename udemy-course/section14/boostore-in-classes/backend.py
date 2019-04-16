import sqlite3


class Database():
    def __init__(self, table, db):
        self.db = db
        self.table = ''
        with sqlite3.connect(self.db) as con:
            tables = con.execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall()[0]
            self.table =  tables[tables.index(table)] if table in tables else self.create_table(table)

    def create_table(self, name):
        with sqlite3.connect(self.db) as con:
            con.execute('CREATE TABLE IF NOT EXISTS '+name+\
                ' (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
            con.commit()
            return name

    def view_data(self):
        if self.table:
            with sqlite3.connect(self.db) as con:
                return con.execute('SELECT * FROM '+self.table).fetchall()

    def add_data(self, data):
        if self.table:
            with sqlite3.connect(self.db) as con:
                try:
                    title = data['title']
                    author = data['author']
                    year = int(data['year'])
                    isbn = int(data['isbn'])
                except:
                    return False

                con.execute('INSERT INTO '+self.table+' VALUES (NULL, ?, ?, ?, ?)',\
                    (title, author, year, isbn))
                con.commit()
                return True

    def search_data(self, column, data):
        if self.table:
            with sqlite3.connect(self.db) as con:
                data = '%'+data+'%'
                return con.execute('SELECT * FROM '+self.table+' WHERE '+column+' LIKE ?', (data, )).fetchall()

    def delete_data(self, id):
        if self.table:
            with sqlite3.connect(self.db) as con:
                con.execute('DELETE FROM '+self.table+' WHERE id = ?', (id, ))
                con.commit()

    def update_data(self, id, data):
        if self.table and data:
            with sqlite3.connect(self.db) as con:
                for key, value in data.items():
                    con.execute('UPDATE '+self.table+' SET '+key+' = ? WHERE id = ?', (value, id))
                    con.commit()