# NESSE MODO ABAIXO, PODE CONFUNDIR, QUANDO USARMOS >>  FALAR E ANDAR!


#class Vendedor:

#    def falar(self):
#        print("Olá, eu sou o vendedor!")


#    def andar(self):
#        print("Estou andando para mostrar os produtos!")

#    def vender(self):
#        print("Você gostaria de comprar algo?")

#class Cliente:

#    def falar(self):
#        print("Olá, eu sou o cliente!")

#    def andar(self):
#        print("Estou andando para encontrar o vendedor!")

#    def comprar(self):
#        print("Sim, eu gostaria de comprar algo!")

#  >>>>>>>>>>>>> MODO CORRETO

class Pessoa:


    def andar(self):
        print("Estou andando!")

    def falar(self):
        print("Olá, eu sou uma pessoa!")


class Cliente(Pessoa):

    def comprar(self):
        print("Sim, eu gostaria de comprar algo!")


class Vendedor(Pessoa):

    def vender(self):
        print("Você gostaria de comprar algo?")


c1 = Cliente()
v1 = Vendedor()

#c1.andar()
#c1.comprar()
#c1.falar()


#v1 = Vendedor()


#v1.andar()
#v1.vender()
#v1.falar()


v1.vender()
c1.comprar()

