import sqlite3

connection = sqlite3.connect("database.db")
connection.row_factory = sqlite3.Row # isso transforma em dict

cursor = connection.cursor()

data = cursor.execute("""
    SELECT * FROM movies;
""")
"""
print(data.fetchone())
print(data.fetchone())
print(data.fetchone())
print(data.fetchone())
print(data.fetchone())
print(data.fetchone())
"""
"""
for linha in data:
    print(linha)

    #não precisa de connection.commit() pois os dados já estão gravados só estamos obtendo
"""

print(dict(data.fetchone()))

connection.close()