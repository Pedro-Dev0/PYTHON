class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.avaliacao = 0.0
        self.total_avaliadores = 0

    def exibir_info(self):
        return f"""
          Titulo: {self.titulo}
          Diretor: {self.diretor}
          Ano: {self.ano}
          Avaliação: {self.avaliacao:.2f}
          Total de avalidadores: {self.total_avaliadores}
        """

    def avaliar(self, nota):
        if nota >= 0 and nota <= 10:    
            pontos_totais = self.avaliacao * self.total_avaliadores

            pontos_totais += nota

            self.total_avaliadores += 1

            self.avaliacao = pontos_totais / self.total_avaliadores
        else: 
            print(f"Erro: A nota {nota} é inválida! Dê uma nota de 0 a 10.")

meu_filme = Filme("legalzão", "Marcos", 1980)
meu_filme.exibir_info()

meu_filme.avaliar(0)

print(meu_filme.exibir_info())

meu_filme.avaliar(10)
print(meu_filme.exibir_info())

meu_filme.avaliar(10)
print(meu_filme.exibir_info())