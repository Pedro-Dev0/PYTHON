class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        novo_livro = {"titulo": titulo, "autor": autor}
        self.livros.append(novo_livro)

        return f"Registrado o livro {titulo}, de {autor} na {self.nome}"

    def buscar_livro(self, termo_busca):
        print(f"Acervo da {self.nome}")
        busca = termo_busca.lower()

        texto_resultados = f"--- Resultados para '{termo_busca}' ---\n"
        encontrou_algum = False

        for livro in self.livros:
            titulo_limpo = livro['titulo'].lower()
            autor_limpo = livro['autor'].lower()

            if busca in titulo_limpo or busca in autor_limpo:
                texto_resultados += f"\n {livro['titulo']} (Autor: {livro['autor']})"
                encontrou_algum = True

        if encontrou_algum == True:
            return texto_resultados
        else:
            return f"O livro não foi encontrado nas estantes da {self.nome}"

    def listar_acervo(self):
        print(f"Acervo da {self.nome}:")
        for livro in self.livros:
            print(f"- {livro['titulo']} de {livro['autor']} -")

    def remover_livro(self, titulo_para_remover):
        for livro in self.livros:
            if livro['titulo'] == titulo_para_remover:
                self.livros.remove(livro)

                return f"O livro '{titulo_para_remover}' foi removido da estante!"
                
        return f"Não foi possível remover: '{titulo_para_remover}'!"



bib = Biblioteca("Biblioteca Municipal")

print(bib.adicionar_livro("O PROCESSO", "FRANZ KAFKA"))
print(bib.adicionar_livro("A METAMORFOSE", "FRANZ KAFKA"))
print(bib.adicionar_livro("Harry Potter e a Pedra Filosofa", "J.K. ROWLING"))
print(bib.adicionar_livro("Harry Potter e a Câmara Secreta", "J.K. ROWLING"))
bib.listar_acervo()

print(bib.buscar_livro('kafka'))
print(bib.remover_livro('Harry Potter e a Pedra Filosofa'))
bib.listar_acervo()




