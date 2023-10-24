from src.passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        pass

    def getNumeroAssentosPrioritarios(self):
        return 0

    def getNumeroAssentosNormais(self):
        return 0

    def getPassageiroAssentoNormal(self, lugar):
        return None

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