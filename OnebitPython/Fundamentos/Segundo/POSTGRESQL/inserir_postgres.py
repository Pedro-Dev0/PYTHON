from conexão import get_connection
import psycopg

try:
    with get_connection() as connection:
        with connection.cursor() as cursor:
            query = """
            INSERT INTO books (title, author, price)
            VALUES (%s, %s, %s);
            """

            cursor.execute(query, ("Dom Casmurro", "Machado de Assis", 39.90))
            print("Livro adicionado com sucesso!")

            """
            cursor.execute("""
            """CREATE TABLE books(
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                price NUMERIC(10, 2) NOT NULL
            );"""
            """)
            """
except psycopg.Error as e:
    pass