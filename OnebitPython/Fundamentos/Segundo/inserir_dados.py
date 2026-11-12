import sqlite3

connection = sqlite3.connect("database.db")

print(connection.total_changes)

cursor = connection.cursor()
"""
nome = input("Nome do Filme:\n")
ano = int(input("Ano de lançamento:\n"))
score = float(input("Nota do Filme:\n"))

executemany para um lote e só execute para um unico registro
"""

movielist = [
    ('MASCARAA', 2009, 7.8),
    ('USURPADORA', 2000, 9.9)
]

cursor.executemany("""
    INSERT INTO movies (nome, ano, score)
    VALUES (?, ?, ?);
""", movielist)

connection.commit()

connection.close()