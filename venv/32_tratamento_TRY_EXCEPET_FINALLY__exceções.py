n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

try: # TENTAR, NÃO TEM REGRA

    print(n1/n2)

except:  # NÃO CONSEGUIU FAZER ALGO

    print("Erro: Divisão por zero não é permitida!")

finally: # CONSEGUIU FAZER ALGO

    print("Obrigado por utilizar o programa!")