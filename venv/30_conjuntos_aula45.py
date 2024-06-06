


# EXCLUI ITENS REPETIDOS - MOSTRA SOMENTE UM DE CADA  >>> set()

x = [1, 1, 1, 2, 2 , 3, 4, 5]
x = set(x)   # EXCLUI ITENS REPETIDOS - MOSTRA SOMENTE UM DE CADA

print(x)


# O PYTHON JA FAZ ISSO AUTOMATICAMENTE SE EU COLOCAR AS CHAVES >> {}

x = {1, 1, 1, 2, 2 , 3, 4, 5}


print(x)

# UNION DOIS CONJUNTOS E TIRA TUDO QUE É REPETIDO >>> .union()

x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

t = x.union(y)

print(t)

# MOSTRA SOMENTE NUMERO IGUAIS EM X E Y .intersection()

x = {1, 2, 3, 4, 5}
y = {5, 7, 8, 9, 10}

x = x.intersection(y)

print(x)

#  .DIFFERENCE()


x = {1, 2, 3, 4, 5}
y = {5, 7, 8, 9, 10}

x = x.difference(y)

print(x)

# .symetric_difference  >> EXCLUI O NUMERO QUE TEM NAS DUAS CHAVES

x = {1, 2, 3, 4, 5}
y = {5, 7, 8, 9, 10}

x = x.symmetric_difference(y)

print(x)

