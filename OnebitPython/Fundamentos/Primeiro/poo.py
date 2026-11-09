#classes são muito importantes na POO

class Caneta:
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo
        pass
caneta_azul = Caneta("azul", "bic")

print(caneta_azul.cor)
print(caneta_azul.tipo)

"""
class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def somar(self, x, y):
        self.resultado = x + y
        return self.resultado
    
    def subtrair(self, x, y):
        self.resultado = x - y
        return self.resultado

calc = Calculadora()
print(calc.somar(10, 5))      # 15
print(calc.subtrair(10, 3))   # 7
print(calc.resultado)         # 7
"""

#@classmethod é para criar outra instancia que puxe direto da classe sem precisar de self
#@staticmethod só um modo auxiliar para que psosa ajudar na classe


