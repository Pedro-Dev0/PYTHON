def contar_letras(texto):
    contador = 0
    for caracter in texto:
        if caracter.isalpha():
            contador += 1


    print(f"esse texto tem {contador} letras!")

contar_letras("Olá Mundo!")  # 8
contar_letras("Python")       # 6
contar_letras("A B C")        # 3

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
filtra_pares = [numero for numero in numeros if numero % 2 == 0]  # [2, 4, 6, 8]
filtra_impares = [numero for numero in numeros if numero % 2 != 0] # [1, 3, 5, 7]

print(filtra_pares)
print(filtra_impares)

produtos = [
    {"nome": "Notebook", "preco": 2500},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 800}
]

produtos_com_desconto = [f"{produto["nome"]} R${produto["preco"] * 0.80:.2f}" for produto in produtos]
print(produtos_com_desconto)
