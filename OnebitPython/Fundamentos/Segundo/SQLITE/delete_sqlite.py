import sqlite3

conexao = sqlite3.connect("database.db")
conexao.row_factory = sqlite3.Row

cursor = conexao.cursor()

cursor.execute("""
    UPDATE movies SET ano = ?
    WHERE ano = ?;
""", (2000, 2001))

filme_excluido = cursor.execute("""
    DELETE FROM movies
    WHERE id = ? 
    RETURNING id, nome;
""", (7,)).fetchone()

print(cursor.rowcount)

conexao.commit()

if not filme_excluido:
    print("Nenhum filme encontrado")
else:
    print(f"O filme {filme_excluido["nome"]} foi excluido. (ID {filme_excluido["id"]})")

conexao.close()