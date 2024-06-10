class Animal:

    def andar(self):
        print("Estou andando...")

    def correr(self):
        print("Estou corriendo...")

    def pular(self):
        print("Estou pulando...")

class Felino:

    def saltar(self):
        print("Estou saltando!")

# OS ANIMAS VÃO  >>> HERDAR <<< DE  CLASS ANIMAL:

class Gato(Animal, Felino):  # ALEM DE HERDAR DE ANIMAL, ESTÁ HERDANDO DE FELINO
    
    def miar(self):
        print("Miau...")

class Cachorro(Animal):

    def latir(self):
        print("Woof...")

class Rato(Animal):

    def roer(self):
        print("Roendo...")

class Canguru(Animal):

    def bater(self):
        print("Batendo...")


 
c = Cachorro()
c.andar()

print("=============")

g = Gato()
g.andar()
g.miar()
        







