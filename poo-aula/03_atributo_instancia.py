class Pessoas:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} logou no sistema!')


p1 = Pessoas("Diogo Misael", 32)

p2 = Pessoas("Benjamin Bryant", 8)

p2.logar_sistema()
p1.logar_sistema()