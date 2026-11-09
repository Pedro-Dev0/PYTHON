frutas = ["maça", "banana"]
print(frutas)
frutas.append("laranja")
frutas.insert(2, "morango")
print(frutas)
#frutas.remove(nome da coisa)
frutas.pop(0)
print(frutas)
"""
index = input("Qual fruta deseja remover? \n")
fruta_removida = frutas.pop(int(index))
print(f"A fruta removida foi o(a) {fruta_removida}")
"""
frutas.sort(reverse=True)
print(frutas)

print(frutas.index("morango"))
print(frutas.count("morango"))

#lista em string
frutas_texto = ", ".join(frutas)
print(frutas_texto)

#transforma string em lista
frutas_texto2 = "maça, banana, abacaxi"
frutas2 = frutas_texto2.split(", ")
print(frutas2)
print(frutas2[0])

# juntando listas
frutas2_verde = ["limao", "123"]
frutas_juntas = frutas2_verde + frutas2
print(frutas2)

#tuplas
tupla = ("computador", "mouse", "monitor")
tupla2 = ("21",)
print(tupla2[0])

numeros = {5, 4, 4, 5, 3, 2, 3, 2, 1}
print(numeros)
numeros.add(99)
numeros.update({99, 99, 10})
print(numeros)
print(numeros)