import pickle   # PEGAR ALGO QUE ESTÁ NA MEMORIA PARA UTILIZAR

class Pessoa:
    nome: "Diogo"  # type: ignore
    idade: 32

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas("Misael", 33)

#x = [1, 2, 3, 4]

arq = open("arquivo.pkl", "wb") # WB ESCRITA BINÁRIA

pickle.dump(p1, arq)

arq = open("arquivo.pkl", "rb")  #   RB  LEITURA BINARIA

retornou = pickle.load(arq)

print(retornou.idade)

