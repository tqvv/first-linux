import sqlite3
con = sqlite3.connect('c:\sqlite\test.db')
cur = con.cursor()
cur.execute('select * from person')