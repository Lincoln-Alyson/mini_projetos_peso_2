from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.vagas = capacidade
        self.assentos_normais = capacidade - qtdPrioritarios

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.capacidade - self.qtdPrioritarios

    def getPassageiroAssentoNormal(self, lugar):
        pass


    def getPassageiroAssentoPrioritario(self, lugar):
        return None

    def getVagas(self):
        return -1

    def subir(self, passageiro: Passageiro):
        return False

    def descer(self, nome):
        return True

    def toString(self):
        return None