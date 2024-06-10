class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):

    def __init__(self, nome, cpf, endereco, telefone):
        super().__init__(nome, cpf)
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

class Vendedor(Pessoa):
    def __init__(self, nome, cpf, salario, comissao):
        super().__init__(nome, cpf)
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.comissao = comissao
        


c1 = Cliente("Diogo", 123, 15, "xx xxxx-xxxx")
v1 = Cliente("Misael", 321, "10", "Comissão de Mil Reais")

print(c1.nome)
print(c1.cpf)
print(c1.endereco)
print(c1.telefone)

print("\n=============\n")

print(v1.nome)
print(v1.cpf)
#print(v1.salario)
#print(v1.comissao)




    
