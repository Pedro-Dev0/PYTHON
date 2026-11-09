numeros = range(1, 101)
dobrados = [numero for numero in numeros if numero % 2 == 0]

print(list(numeros))
print(dobrados)

produtos = [
    {"nome": "Mouse", "Preço": 50},
    {"nome": "Notebook", "Preço": 1000},
    {"nome": "Monitor", "Preço": 400}
]

produtos_caros = [produto["nome"] for produto in produtos if produto["Preço"] > 100]
print(produtos_caros)

notas = [1, 5, 8, 10 , 1, 7]
resultado = ["Passou" if nota >= 7 else "Reprovou" for nota in notas]
print(resultado)

