from crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.conta = 0
        self.caixa = 0
        self.filaDeEspera = []
        self.criancasNoPulaPula = []
    def getFilaDeEspera(self):
        return self.filaDeEspera

    def getCriancasPulando(self):
        return self.criancasNoPulaPula

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for crianca in self.criancasNoPulaPula:
            if crianca.nome == nome:
                return self.conta

    def entrarNaFila(self, crianca: Crianca):
        if crianca not in self.filaDeEspera and crianca not in self.criancasNoPulaPula:
            self.filaDeEspera.append(crianca)
            print(f'{crianca.nome} está na fila de espera')
            return True
        else:
            return False

    def entrar(self):
        if len(self.criancasNoPulaPula) < self.limiteMax and len(self.filaDeEspera) > 0:
            crianca = self.filaDeEspera.pop(0)
            self.criancasNoPulaPula.insert(0, crianca)
            self.conta += 2.50
            print(f'{crianca.nome} está no pulapula')
            return True
        else:
            print('Pulapula cheio!')
            return False

    def sair(self):
        if len(self.criancasNoPulaPula) > 0:
            crianca = self.criancasNoPulaPula.pop(0)
            self.filaDeEspera.append(crianca)
            print(f'{crianca.nome} não está mais no PulaPula')
            return True
        return False

    def papaiChegou(self, nome):
        for crianca in self.criancasNoPulaPula + self.filaDeEspera:
            if crianca.nome == nome:
                self.caixa += self.conta
                self.conta = 0
                if crianca in self.criancasNoPulaPula:
                    self.criancasNoPulaPula.remove(crianca)
                else:
                    self.filaDeEspera.remove(crianca)
                return True
        return False

    def fechar(self):
        self.criancasNoPulaPula.clear()
        self.filaDeEspera.clear()
        self.conta = 0
        return -1
