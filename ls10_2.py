import sqlite3

connection = sqlite3.connect("_ls10_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
cur.execute("INSERT INTO first_table (name) VALUES ('Anna');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")

connection.commit()

connection.close()
