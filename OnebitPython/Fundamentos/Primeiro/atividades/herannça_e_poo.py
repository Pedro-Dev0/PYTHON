class Conta:
    def __init__(self, titular, saldo):
        self.__saldo = saldo  # Privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    
    def obter_saldo(self):
        return self.__saldo

conta = Conta("João", 1000)
conta.depositar(500)
print(conta.obter_saldo())  # 1500
conta.sacar(200)
print(conta.obter_saldo())  # 1300