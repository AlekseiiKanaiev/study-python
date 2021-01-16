#!/usr/bin/python3.5
import sqlite3
path = 'udemy-course/section12/lite.db'

def create_table():
    # Connect to a DB
    # if there is no file, it will create it
    con = sqlite3.connect(path)

    # Create a cursor object
    cur = con.cursor()

    # Write an SQL query (create table with 3 columns)
    # if you run code twice, you will get an error
    # to avoid this you shoud and a condition to SQL code
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INT, price REAL)')

    # Commit a changes
    con.commit()

    # Close DB connection
    con.close()

def add_data(data):
    # Connect to a DB
    con = sqlite3.connect(path)
    # Create a cursor object
    cur = con.cursor()
    # add some data to DB
    cur.execute('INSERT INTO store VALUES (?,?,?)', (data['name'], data['quantity'], data['price']))

    # Commit a changes
    con.commit()

    # Close DB connection
    con.close()

def view_db():
    # Connect to a DB
    con = sqlite3.connect(path)
    # Create a cursor object
    cur = con.cursor()
    # selecting all (*) from DB
    cur.execute('SELECT * FROM store')
    # writing fetched data to variable
    rows = cur.fetchall()
    # Close DB connection
    con.close()
    return rows

def delete_data(item):
    # Connect to a DB
    con = sqlite3.connect(path)
    # Create a cursor object
    cur = con.cursor()
    # you must write coma after 'item' because thre is only 1 item, otherwise you will get an error
    cur.execute('DELETE FROM store WHERE item = ?', (item,))
    # Commit a changes
    con.commit()
    # Close DB connection
    con.close()

def update_data(data):
    # Connect to a DB
    con = sqlite3.connect(path)
    # Create a cursor object
    cur = con.cursor()
    s = 'quantity'
    command = f'UPDATE store SET {s} = ?, price=? WHERE item = ?'
    cur.execute(command, (data['quantity'], data['price'],  data['name'],))
    # Commit a changes
    con.commit()
    # Close DB connection
    con.close()

# create_table()
data = {'name': 'Wine glass', 'quantity': 24, 'price': 123.6}
new_data = {'name': 'Wine glass', 'quantity': 2, 'price': 12.6}
# add_data(data)
# delete_data('Wine glass')
update_data(new_data)
print(view_db())
