# Receba um numero e mostre a tabuada,
n1 = int(input("\nDigite o número que deseja saber a tabuada: "))   # Comando para o usuário digitar

i = 1 

for i in range(1, 11):
    print(f"{n1} x {i} = {n1*i}") # MULTIPLICAÇÃO    
    i += 1