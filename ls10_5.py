import sqlite3

connection = sqlite3.connect("_ls10_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("DELETE FROM first_table WHERE rowid=4;")

connection.commit()

connection.close()
