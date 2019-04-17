import sqlite3

class Database():
    def __init__(self, table, db):
        self.table = ''
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        tables = self.cur.execute('SELECT name FROM sqlite_master WHERE type = "table"').fetchall()[0]
        self.table =  tables[tables.index(table)] if table in tables else self.create_table(table)

    def create_table(self, name):
        self.cur.execute('CREATE TABLE IF NOT EXISTS '+name+\
            ' (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
        self.con.commit()
        return name

    def view_data(self):
        if self.table:
            return self.cur.execute('SELECT * FROM '+self.table).fetchall()

    def add_data(self, data):
        if self.table:
            try:
                title = data['title']
                author = data['author']
                year = int(data['year'])
                isbn = int(data['isbn'])
            except:
                return False

            self.cur.execute('INSERT INTO '+self.table+' VALUES (NULL, ?, ?, ?, ?)',\
                (title, author, year, isbn))
            self.con.commit()
            return True

    def search_data(self, column, data):
        if self.table:
            data = '%'+data+'%'
            return self.cur.execute('SELECT * FROM '+self.table+' WHERE '+column+' LIKE ?', (data, )).fetchall()

    def delete_data(self, id):
        if self.table:
            self.cur.execute('DELETE FROM '+self.table+' WHERE id = ?', (id, ))
            self.con.commit()

    def update_data(self, id, data):
        if self.table and data:
            for key, value in data.items():
                self.cur.execute('UPDATE '+self.table+' SET '+key+' = ? WHERE id = ?', (value, id))
                self.con.commit()

    # def close_app(self):
    #     self.con.close()

    def __del__(self):
        self.con.close()