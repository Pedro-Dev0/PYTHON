from conexão import get_connection

def atualizar_price(novo_preco: float, livro_id: int):
    query = """
    UPDATE books SET price = %s
    WHERE id = %s RETURNING title;
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (novo_preco, livro_id))

            if cursor.rowcount == 0:
                print(f"Nenhum livro encontrado com o #ID {livro_id}!")
                return
            
            book = dict(cursor.fetchone() or {})

            print(f"Livro {book["title"]} atualizou o preço para R${novo_preco:.2f} no #ID {livro_id}")
            
#atualizar_price(50, 1)

def excluir_livro(livro_id: int):
    query = """
    DELETE FROM books
    WHERE id = %s;
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (livro_id,))
    
            if cursor.rowcount == 0:
                print(f"Nenhum livro encontrado com o #ID {livro_id}!")
                return
            
            print(f"Livro de #ID {livro_id} excluido com sucesso!")

excluir_livro(2)
