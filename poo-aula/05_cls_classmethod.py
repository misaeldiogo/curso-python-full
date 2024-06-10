class Pessoas:
    possui_olho = True
    possui_boca = True
    possui_pernas = True
    possui_raca = "Ser humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retornar_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f"{self.nome()} logou no sistema!")

    @classmethod
    def andar(cls): # CLS RECEBE O ESTADO DA CLASSE
        cls.pernas = 2
        return None

print(Pessoas.possui_pernas)
Pessoas.andar()
print(Pessoas.pernas)


