x = [i for i in range(0, 10)]
print(x)

# MODELO COMPLICADO 

y = []
for i in range(0, 10):
    y.append(i)
    print(y)

# REPETIR O 10 - 10 X

x = [10 for i in range(0, 10)]
print(x)

# ACRESCENTAR 2 PARA CADA NUMERO 

y = [1, 2, 3 , 4, 5]
x = [i*2 for i in y]
print(x)

# PEDINDO PARA SOLICITAR AO USUÁRIO

x = [input("Digite um nome: ") for i in range(0, 3)]
print(x)


# MATRIZ

x = [[j for j in range(4, 7)] for i in range(0, 3)]
print(x)

# MATRIZ COM INPUT

x = [[input() for j in range(4, 7)] for i in range(0, 3)]
print(x)

# CONDICIONAL

x = [i for i in range(0, 10) if i > 4]

print(x)
