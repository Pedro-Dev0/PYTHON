try:
    numeros = [1, 2, 3]
    print(numeros[10])
except IndexError as error:
    print("erro: {error}")

try:
    resultado = 10 / 0
except ZeroDivisionError as error:
    print("erro: {error}")