
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Costruindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de  {} do titular{}".format(self.__saldo, self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def saca(self, valor):
        if(valor <= self.__saldo + self.__limite):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
        print("transferido {} para {}".format(valor, destino))

    def get_saldo(self):
        return  self.__saldo

    def get_titular(self):
        return self._titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
            return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}


