import sqlite3

connection = sqlite3.connect("database.db")

print(connection.total_changes)

connection.close()