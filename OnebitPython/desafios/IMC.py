"""
calculadora que faz o calculo de peso IMC

ela deve pegar a altura do usuário e peso

e calcular peso divido por altura vezes altura

deve aprensetar se o imc está baixo ou não e caso não coloque nada apresentar que faltou informações
"""
"""
altura = float(input(f"\nInforme sua altura: "))

peso = float(input(f"\nInforme seu peso: "))

imc = peso / (altura*altura)

if imc < 18.5:
    print(f"seu IMC é {imc:.2f} e ele mostra magreza extrema")
elif imc >= 18.5 and imc < 24.9:
    print(f"seu IMC é {imc:.2f} e ele mostra que está saudável")
elif imc >= 24.9 and imc <30:
    print(f"seu IMC é {imc:.2f} e ele mostra que está com sobrepeso se cuide")
elif imc >=30 and imc <=35:
    print(f"GORDO FUDIDO")
"""

def calcular_sobra(ganhos, gastos, guardado):
    sobra = ganhos - gastos
    sobra_apos_guardar = sobra - guardado

    if sobra < 0:
        print('Impossivel guardar pois você gastou tudo ou mais do que sobrou')
    elif guardado > sobra:
        print(f"impossivel guardar esse valor, só resta isso na conta: {sobra}")
    else:
        print(f"esse é o valor que sobra após gastos e guardar uma parte do que sobrou\nR${sobra_apos_guardar}")



calcular_sobra(1000, 1100, 500)