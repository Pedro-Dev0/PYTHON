frutas = ["maça", "banana", "uva"]

for fruta in frutas:
    print(fruta)

for index, fruta in enumerate(frutas):
    print(index, fruta)

"""for numero in range(0, 1001, 5):
    print(numero)
    if numero == 100:
        break"""

contador = 10

while contador > 0:
    print(contador)
    contador -= 1

print("Lançamento")


tabuada = 0
num = int(input("Digite um numero: "))

while tabuada < 11:
    print(f"{num} x {tabuada} = {num * tabuada}")
    tabuada += 1


for i in range(0, 11):
    resultado = num * i
    print(f"{i} x {num} = {resultado}")


produtos = [
    {"nome": "Mouse", "preco": 50},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Monitor", "preco": 300},
    {"nome": "Webcam", "preco": 80},
    {"nome": "Mousepad", "preco": 30}
]

produto_imposto = [f"{produto["nome"]} R${produto["preco"] * 1.10:.2f}" for produto in produtos if produto["preco"] < 100]
print(produto_imposto)

