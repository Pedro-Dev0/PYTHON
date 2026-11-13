from enum import Enum
import sqlite3

class Prioridade(str, Enum):
    BAIXA = "BAIXA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"

class StatusChamado(str, Enum):
    ABERTO = "ABERTO"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDO = "CONCLUIDO"

class ChamadosDB:
    def __init__(self, db_name: str = "chamados.db"):
        self.conn = sqlite3.connect(db_name)

        self.conn.row_factory = sqlite3.Row

        self._criar_tabela()

    def _criar_tabela(self) -> None:
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chamados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente VARCHAR(255) NOT NULL,
                descricao TEXT NOT NULL,
                prioridade TEXT NOT NULL CHECK (prioridade IN ('BAIXA', 'MEDIA', 'ALTA')),
                status TEXT NOT NULL DEFAULT 'ABERTO' CHECK (status IN ('ABERTO', 'EM_ANDAMENTO', 'CONCLUIDO'))
            );
            """)
        
        self.conn.commit()

    def abrir_chamado(self, cliente: str, descricao: str, prioridade: Prioridade) -> int:
        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO chamados (cliente, descricao, prioridade, status)
            VALUES (?, ?, ?, ?);
            """, (cliente, descricao, prioridade.value, StatusChamado.ABERTO.value))

        self.conn.commit()

        return cursor.lastrowid

    def listar_chamados(self):
        cursor = self.conn.cursor()
        
        cursor.execute("""
            SELECT * FROM chamados;
        """)

        return(cursor.fetchall())

    def busca_por_id(self, chamado_id: int):
        cursor = self.conn.cursor()
                
        cursor.execute("""
            SELECT * FROM chamados
            WHERE id = ?;
        """, (chamado_id,))

        resultado = cursor.fetchone()

        if resultado is None:
            print("ID não encontrado")
            return None
        else:
            return resultado

    def atualizar_status(self, chamado_id: int, novo_status: StatusChamado):
        cursor = self.conn.cursor()
                        
        cursor.execute("""
            UPDATE chamados SET status = ?
            WHERE id = ?;
        """, (novo_status.value, chamado_id))

        self.conn.commit()

        if cursor.rowcount == 0:
            print(f"Aviso: Nenhum chamado encontrado com o ID {chamado_id}")
        else:
            print(f"Status do chamado #{chamado_id} atualizado para {novo_status.value}!")

    def deletar_chamado(self, chamado_id: int):
        cursor = self.conn.cursor()
                                
        cursor.execute("""
            DELETE FROM chamados
            WHERE id = ?;
        """, (chamado_id,))

        self.conn.commit()

        if cursor.rowcount == 0:
            print(f"Aviso: Nenhum chamado encontrado com o ID {chamado_id}")
        else:
            print(f"Sucesso: chamado #{chamado_id} deletado do banco de dados")

if __name__ == "__main__":
# Instancia a sua classe
    app_db = ChamadosDB()
    print("Banco de dados criado e conectado com sucesso!\n")
    """
    #abrindo chamado
    id1 = app_db.abrir_chamado("Empresa KONECTA", "Servidor fora do ar", Prioridade.ALTA)
    print(f"chamado #{id1} criado com prioridade {Prioridade.ALTA.value}.")

    # Deletando um chamado
    id2 = app_db.deletar_chamado(2)
    print(f"chamado de #{id2} deletado do sistema")

    # 2. Testando Read (Listar todos)
    print("--- LISTANDO TODOS OS CHAMADOS ---")
    for chamado in app_db.listar_chamados():
        print(f"ID: {chamado['id']} | Cliente: {chamado['cliente']} | Status: {chamado['status']}")
    print()
    """
    try:
        with app_db.conn:
            app_db.conn.execute(
                "INSERT INTO chamados (cliente, descricao, prioridade, status) VALUES (?, ?, ?, ?)",
                ("empresa teste", "teste", "BAIXA", "SLA")
                )
    except sqlite3.IntegrityError as e:
        print(f"Sucesso: o banco barrou a inserção invalida com o erro: {e}")