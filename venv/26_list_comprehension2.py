
# REPETIÇÃO DE NUMEROS DIVERSAS VEZES

x = [10 for i in range(0, 10)]

print(x)

# Y QUANTIDADE DE VEZES, X REGRA PARA PULA DE 2 EM 2

y = [1, 2, 3, 4, 5, 6]
x = [i*2 for i in y]

print(x)

# PERGUNTANDO AO USUÁRIO - repetição  de perguntas iguais - no exemplo abaixo vai fazer a mesma pergunta 3 vezes

x = [input("Digite um nome: ") for i in range(0, 3)]

print(x)

# MATRIZES LISTAS E  LISTAS - COLUNA E LINHA

# PARA CADA VALOR EU TENHO UMA LISTA

x = [[] for i in range(0, 3)]

print(x)

# UMA LISTA DENTRO DE OUTRA LISTA

x = [[j for j in range(4, 7)] for i in range(0, 3)]

print(x)



