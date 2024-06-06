

x = [i for i in range(12, 26)]

x = list(map(lambda x: 10, x))  # TRANSFORMOU TODOS VALORES EM 10

print(x)


# =============  COLOCANDO CONDIÇÕES

#  SE X FOR MENOR QUE 18 FAÇO A ALTERÇÃO

x = [i for i in range(12, 26)]

x = list(map(lambda x: 10 if x < 18 else(x), x))  # TRANSFORMOU TODOS VALORES EM 10 se for menor que 18

print(x)

# ============= FAZENDO COM DICIONÁRIOS

X = [{"nome": "Diogo", "idade": 22}]

x = list(map(lambda x: 50 if x < 22 else(x), x))  # TRANSFORMOU TODOS VALORES EM 10 se for menor que 18

print(x)