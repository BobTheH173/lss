import sqlite3

connection = sqlite3.connect("_ls10_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=4;")

connection.commit()

connection.close()
