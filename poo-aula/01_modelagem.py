
# DEFINIÇÃO DE QUE UMA PESSOA TEM

class Pessoas:  # CLASS MINUSCULO E PESSOAS INICIANDO MAIÚSCULO
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


# CRIAR NOVO METODO DE LOGAR NO SISTEMA  >>> somente print

    def sistema(Self):
        print(f"{Self.nome} está logando no Sistema, através do CPF {Self.cpf}")

# INSTANCIA DE UM DETERMINADO OBJETO - CRIAR VÁRIAS PESSOAS

p1 = Pessoas("Diogo", 32, "12345678910")
p2 = Pessoas("João", 25, "98765432111")

p1.sistema()
p2.sistema()

print(p1.nome)

print(p2.idade)

print(p2.nome)



