import sqlite3

connection = sqlite3.connect("database.db")

print(connection.total_changes)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        score REAL NOT NULL
    );
""")

connection.close()