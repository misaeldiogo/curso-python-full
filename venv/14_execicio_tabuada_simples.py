# Receba um numero inteiro do usuário e mostre a tabuada desse número.

n1 = int(input("\nDigite o número que deseja saber a tabuada: "))   # Comando para o usuário digitar

i = 1  # Começa aqui

print("\nSoma\n")

while i <= 10:
    print(f"{n1} + {i} = {n1+i}") # SOMA    
    i += 1

i = 1   # Começa aqui

print("\nMultiplicação\n")

while i <= 10:
    print(f"{n1} x {i} = {n1*i}") # MULTIPLICAÇÃO    
    i += 1
