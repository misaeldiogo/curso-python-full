#class Pessoas: 
 #   def __init__(self, nome, idade):
  #      self.nome = nome 
   #     self.idade = idade

    #def retornar_nome(self):
     #   return self.nome
    
    #def logar_sistema(self):
     #   print(f"{self.retornar_nome()} logou no sistema")


#p1 = Pessoas("Diogo Misael", 20)
#p2 = Pessoas("João Pedro", 25)

#p2.logar_sistema()
#p1.logar_sistema()

class Pessoas:
    possui_boca = True
    possui_olhos = True
    possui_ouvidos = True
    possui_pernas = True
    possui_raça =  "Ser Humano"


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f"{self.retorna_nome()} logou no sistema")

    @classmethod
    def andar(cls):
        cls.pernas = 2
        return None
print(Pessoas.possui_pernas)
Pessoas.andar()
print(Pessoas.possui_pernas)





