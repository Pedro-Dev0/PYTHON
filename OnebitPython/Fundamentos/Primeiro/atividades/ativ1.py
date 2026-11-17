numero = input("Digite um numero: \n")
numero_novo = int(numero)

print(f"numero: {numero}")
print(f"antecessor: {numero_novo - 1}")
print(f"sucessor: {numero_novo + 1}")

# primeiro desafio acima de ver antecessor e sucessor, pode até mesmo fazer variaveis para armazenar, mas preferi fazer um mudança mesmo e manipulação de string

nota_1 = 10
nota_2 = 7
nota_3 = 4.5

media_calculo = (nota_1 + nota_2 + nota_3) / 3

print(f"""
Nota1: {nota_1}
Nota2: {nota_2}
Nota3: {nota_3}

Média: {media_calculo:.2f}
""")

#feito desafio 2 para media de nota do aluno


nome = "Pedro Henrique"

print(nome.upper())
print(nome.lower())
print(len(nome))
print(nome[:3])
print(nome[-3:])
print(nome.replace("Pedro Henrique", "Pedro_Henrique"))