from conexão import get_connection


with get_connection() as connection:
    with connection.cursor() as cursor:
        query = """
        SELECT * FROM books;
        """

        cursor.execute(query)
        print(tuple(dict(cursor.fetchmany(2)[1]).values()))
        cursor.execute(query)
        print(tuple(dict(cursor.fetchmany(2)[0]).values()))