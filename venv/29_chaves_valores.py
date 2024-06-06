
# MOSTRA SOMENTE O QUE ESTA ANTES DOS DOIS PONTOS

pessoa = {"nome": "diogo", "idade": 21, "altura": 180}

print(pessoa.keys())

# MOSTRA TUDO QUE ESTA DENTRO DA CHAVE & VALOR >>> COMANDO items

print(pessoa.items())

# USANDO FOR  >>>> for   >>> items

for i in pessoa.items():
    print(i)


# USANDO FOR  >>>> for   >>> keys

for i in pessoa.keys():
    print(i)

# USANDO FOR  >>>> for   >>> values

for i in pessoa.values():
    print(i)
