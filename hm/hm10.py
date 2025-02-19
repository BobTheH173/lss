import sqlite3

connection = sqlite3.connect("../_hm10_DB.sl3", timeout=5)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Animals (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Type TEXT);")

cursor.executemany("INSERT INTO Animals (Name, Type) VALUES (?, ?);", [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
])

cursor.execute("UPDATE Animals SET Name = ? WHERE Name = ?;", ("Сокіл", "Орел"))

cursor.execute("SELECT * FROM Animals WHERE Type = ?;", ("Ссавець",))
print("Ссавці:", cursor.fetchall())

cursor.execute("SELECT * FROM Animals;")
print("Всі тварини:", cursor.fetchall())

connection.commit()

connection.close()
