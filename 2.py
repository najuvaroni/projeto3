class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print("Woof!")
meu_auau= Cachorro("nick", 1)

meu_auau.latir()