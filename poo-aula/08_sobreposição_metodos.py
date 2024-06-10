class Pessoa:    #CLASSE PAI  


    def andar(self):
        print("Estou andando!")

    def falar(self):
        print("Olá, eu sou uma pessoa!")


class Cliente(Pessoa):    #CLASSE FILHA

    def comprar(self):
        print("Sim, eu gostaria de comprar algo!")

    def correr (self):
        print("Vou correndo!")


class Vendedor(Pessoa): #CLASSE FILHA

    def vender(self):
        print("Você gostaria de comprar algo?")

    def brigar(self):

        super().brigar()   # Vai se referir sempre a classe PAI
        
        print("Você vai comprar algo ou vai ficar só olhando?")


c1 = Cliente()
v1 = Vendedor()

v1.vender()
c1.comprar()