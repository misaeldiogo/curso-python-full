idades = [25, 15, 7, 14, 150, 0, 2024, 60, 1.5, 2, 4 , 6 , 8 , 1, 12, 45, 47, 49, 53, 57 ,59 ,75 ]

for i in range(0, len(idades)):
    print(idades[i], i)

# MODO MAIS FACIL DE FAZER

for i in idades:
    print(i)


# ENUMERATE

x = list(enumerate(idades))
print(x)

# ENUMERATE + MODO FACIL >> for

for i in enumerate(idades):
    print(i)

# enumerate com divisão

for i,j in enumerate(idades):
    print(f"i = {i} j = {j}")

# 