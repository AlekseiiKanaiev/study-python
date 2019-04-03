#!/usr/bin/python3.5
import sqlite3

def create_table():
    # Connect to a DB
    # if there is no file, it will create it
    con = sqlite3.connect('lite.db')

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
    con = sqlite3.connect('lite.db')
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
    con = sqlite3.connect('lite.db')
    # Create a cursor object
    cur = con.cursor()
    # selecting all (*) from DB
    cur.execute('SELECT * FROM store')
    # writing fetched data to variable
    rows = cur.fetchall()
    # Close DB connection
    con.close()
    return rows

# create_table()
# data = {'name': 'Wine glass', 'quantity': 8, 'price': 12.6}
# add_data(data)
print(view_db())