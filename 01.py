class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


pessoa1 = pessoa('Anaju ', '16')
pessoa2 = pessoa("Sarah", "16")

print(pessoa1.nome, pessoa1.idade,'e', pessoa2.nome, pessoa2.idade )