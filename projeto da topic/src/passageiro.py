class Passageiro:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    def ePrioridade(self):
        return True

    def getNome(self):
        return None