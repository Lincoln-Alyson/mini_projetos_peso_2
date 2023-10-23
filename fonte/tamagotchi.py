class Tamagotchi:

    def __init__(self, energiaMax:int, saciedadeMax:int, limpezaMax:int, idadeMax:int ):
        self.energia_maxima = energiaMax
        self.saciedade_maxima = saciedadeMax
        self.limpeza_maxima = limpezaMax
        self.idade_maxima = idadeMax
        self.energia = energiaMax
        self.saciedade = saciedadeMax
        self.limpeza = limpezaMax
        self.diamantes = 0
        self.idade = 0


    def getEnergiaMax(self):
        return self.energia_maxima

    def getSaciedadeMax(self):
        return self.saciedade_maxima

    def getLimpezaMax(self):
        return self.limpeza_maxima

    def getIdadeMax(self):
        return self.idade_maxima

    def getEnergiaAtual(self):
        return self.energia

    def getSaciedadeAtual(self):
        return self.saciedade

    def getLimpezaAtual(self):
        return self.limpeza

    def getIdadeAtual(self):
        return self.idade

    def getDiamantes(self):
        return self.diamantes

    def getEstaVivo(self):
        if self.energia > 0 and self.saciedade > 0 and self.limpeza > 0:
            return True
        else:
            self.energia = 0
            self.limpeza = 0
            self.saciedade = 0

    def brincar(self):
        if self.getEstaVivo():
            self.energia -= 2
            self.saciedade -= 1
            self.limpeza -= 3
            self.diamantes += 1
            self.idade += 1
            return True
        else:
            return False

    def comer(self):
        if self.getEstaVivo():
            self.energia -= 1
            self.saciedade += 4
            if self.saciedade > self.saciedade_maxima:
                self.saciedade = 10
            self.limpeza -= 2
            self.diamantes += 0
            self.idade += 1
            return True
        else:
            return False


    def dormir(self):
        if self.getEstaVivo():
            if self.energia == self.energia_maxima - 5:
                self.energia = self.energia_maxima
                self.saciedade -= 2
                return True
        else:
            return False



    def banhar(self):
        if self.getEstaVivo():
            self.energia -= 3
            self.saciedade -= 1
            self.limpeza = self.limpeza_maxima
            self.diamantes += 0
            self.idade += 2
            return True
        else:
            return False