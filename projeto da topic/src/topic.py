from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios):
        self.capacidade = capacidade
        self.qtdPrioritarios = qtdPrioritarios
        self.vagas = capacidade
        self.assentos_normais = self.capacidade - self.qtdPrioritarios
        self.psg_normal = [None] * self.assentos_normais
        self.psg_prioritario = [None] * qtdPrioritarios
        self.lista_strings = []

    def getNumeroAssentosPrioritarios(self):
        return self.qtdPrioritarios

    def getNumeroAssentosNormais(self):
        return self.assentos_normais

    def getPassageiroAssentoNormal(self, lugar):
        if lugar >= 0 and lugar < len(self.psg_normal):
            return self.psg_normal[lugar]
        else:
            return None


    def getPassageiroAssentoPrioritario(self, lugar):
        if lugar >= 0 and lugar < len(self.psg_prioritario):
            return self.psg_prioritario[lugar]
        else:
            return None

    def getVagas(self):
        return self.vagas

    def subir(self, passageiro: Passageiro):
        if passageiro.idade >= 65:
            if None in self.psg_prioritario:
                index = self.psg_prioritario.index(None)
                self.psg_prioritario[index] = passageiro
                self.vagas -= 1
                print(f"Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira preferencial {index}.")
                return True
            elif None in self.psg_normal:
                index = self.psg_normal.index(None)
                self.psg_normal[index] = passageiro
                self.vagas -= 1
                print(f"Não há cadeiras preferenciais disponíveis. Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira normal {index}.")
                return True
        else:
            if None in self.psg_normal:
                index = self.psg_normal.index(None)
                self.psg_normal[index] = passageiro
                self.vagas -= 1
                print(f"Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira normal {index}.")
                return True
            elif None in self.psg_prioritario:
                index = self.psg_prioritario.index(None)
                self.psg_prioritario[index] = passageiro
                self.vagas -= 1
                print(f"Não há cadeiras normais disponíveis. Passageiro {passageiro.nome} (Idade: {passageiro.idade}) inserido na cadeira preferencial {index}.")
                return True

        print("A topic está lotada. Não é possível inserir mais passageiros.")
        return False

    def descer(self, nome):
        for i, passageiro in enumerate(self.psg_prioritario):
            if passageiro and passageiro.nome == nome:
                self.psg_prioritario[i] = None
                self.vagas += 1
                print(f"Passageiro {nome} desceu da cadeira preferencial.")
                return True

        for i, passageiro in enumerate(self.psg_normal):
            if passageiro and passageiro.nome == nome:
                self.psg_normal[i] = None
                self.vagas += 1
                print(f"Passageiro {nome} desceu da cadeira normal.")
                return True

        print(f"Passageiro {nome} não encontrado na topic.")
        return False

    def toString(self):
        for passageiro in self.psg_prioritario:
            if passageiro:
                self.lista_strings.insert(0, '@' + passageiro.nome)
            else:
                self.lista_strings.append('@')

        for passageiro in self.psg_normal:
            if passageiro:
                self.lista_strings.append('=' + passageiro.nome)
            else:
                self.lista_strings.append('=')

        lista = ' '.join(self.lista_strings)
        return '[' + lista + ' ]'