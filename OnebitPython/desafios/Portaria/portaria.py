from datetime import datetime
from typing import Optional
import csv

class Convidado:
    def __init__(self, nome: str, status: str = "pendente", entrada_em: str = "", codigo: Optional[str] = None):
        self._nome = nome
        self._status = status
        self._entrada_em = entrada_em

        if codigo:
            self._codigo = codigo
        else:
            self._codigo = self._gerar_codigo(nome)

    def _gerar_codigo(self, nome: str) -> str:
        return (nome[:3] + nome[-2:]).upper()

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def status(self) -> str:
        return self._status

    @property
    def entrada_em(self) -> str:
        return self._entrada_em

    def confirmar_entrada(self):
        self._status = "Confirmado"

        self._entrada_em = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

class GerenciadorPortaria():
    def __init__(self):
        self._convidados = []

    def carregar_txt(self, caminho_arquivo: str):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

                linhas = arquivo.readlines()

                for linha in linhas:
                    nome_limpo = linha.strip()

                    novo_convidado = Convidado(nome_limpo)

                    self._convidados.append(novo_convidado)

    
        except FileNotFoundError as error:
            print(f"Erro ao encontrar arquivo | {error}")

    def salvar_csv(self, caminho_arquivo: str):
        with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow(["nome", "codigo", "status", "entrada_em"])

            for convidado in self._convidados:
                escritor.writerow([convidado.nome, convidado.codigo, convidado.status, convidado.entrada_em])

    def buscar_convidados(self, termo: str):
        resultados = []
        termo_minusculo = termo.lower()

        for convidado in self._convidados:
            nome_minusculo = convidado.nome.lower()

            if termo_minusculo in nome_minusculo:
                resultados.append(convidado)

        return resultados