class Pessoas:  # CLASS MINUSCULO E PESSOAS INICIANDO MAIÚSCULO

    def __init__(self, nome, idade, cpf):   # SEMPRE PARA INICIAR
        self.nome = nome
        self.idade = idade 
        self.cpf = cpf
        print("Olá!") 

    def logar_sistema(self):
        print(f"{p1.nome}, seu CPF: {p1.cpf} está correto, conseguimos comprovar a sua idade, realmente você tem {p1.idade} anos, desse modo, você já está logado em nosso sistema!")
    
p1 = Pessoas("Diogo", 32, "12345678910")

#p2 = Pessoas("João", 25, "98765432111")


p1.logar_sistema()

#p2 = Pessoas("João", 25, "98765432111")
#p2.logar_sistema()