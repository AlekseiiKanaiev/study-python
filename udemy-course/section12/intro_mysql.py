#!/usr/bin/python3.5

import mysql.connector

word = input("Enter a eword in english and press Enter: ")
con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
result = cursor.fetchall()
if result:
    for r in result:
        print(r[1])
else:
    print("Couldn't find any result")