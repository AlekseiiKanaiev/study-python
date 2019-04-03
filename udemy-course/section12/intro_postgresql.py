#!/usr/bin/python3.5
# library used to connect to postgreSQL DB
import psycopg2

# use " '' " only style
connection = "dbname = 'db1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'"

def create_table():
    # Connect to a DB

    con = psycopg2.connect(connection)

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
    con = psycopg2.connect(connection)
    # Create a cursor object
    cur = con.cursor()
    # add some data to DB
    # that record is risky because of possible db injection
    # cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" %(data['name'], data['quantity'], data['price']))
    # proper record is:
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (data['name'], data['quantity'], data['price']))

    # Commit a changes
    con.commit()

    # Close DB connection
    con.close()

def view_db():
    # Connect to a DB
    con = psycopg2.connect(connection)
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
    con = psycopg2.connect(connection)
    # Create a cursor object
    cur = con.cursor()
    # you must write coma after 'item' because thre is only 1 item, otherwise you will get an error
    cur.execute('DELETE FROM store WHERE item = %s', (item,))
    # Commit a changes
    con.commit()
    # Close DB connection
    con.close()

def update_data(data):
    # Connect to a DB
    con = psycopg2.connect(connection)
    # Create a cursor object
    cur = con.cursor()
    cur.execute('UPDATE store SET quantity = %s, price = %s WHERE item = %s', (data['quantity'], data['price'],  data['name'],))
    # Commit a changes
    con.commit()
    # Close DB connection
    con.close()

# create_table()
data = {'name': 'Tea cup', 'quantity': 221, 'price': 12.3}
# add_data(data)
new_data = {'name': 'Tea cup', 'quantity': 2, 'price': 12.6}
# delete_data('Wine glass')
# update_data(new_data)
print(view_db())