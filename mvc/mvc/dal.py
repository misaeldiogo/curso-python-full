# salvar o objeto

from model import Pessoa

#import importlib

#module_name = "model"
#module = importlib.import_module(module_name)
#Pessoa = module.Pessoa


class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        # implementar a lógica para salvar o objeto Pessoa no banco de dados
        with open("pessoas.txt", "w") as arq:
            arq.write(pessoa.nome + "  " + str(pessoa.idade) + "  " + pessoa.cpf)

    @classmethod
    def ler(cls):
    #def ler (self):
        nome = "Diogo"
        idade = 32
        cpf = "12345678910"

        return Pessoa(nome, idade, cpf)
    
    
##p1 = Pessoa("Diogo Msiael", 32, "12345678910")
#print(PessoaDal.salvar(1))
##print(PessoaDal.ler().idade)