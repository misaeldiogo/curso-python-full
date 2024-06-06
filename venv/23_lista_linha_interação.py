idades = [25, 15, 7, 14, 150, 0, 2024, 60, 1.5, 2, 4 , 6 , 8 , 1, 12, 45, 47, 49, 53, 57 ,59 ,75 ]

idades_pares = []

for i in idades:
    if i % 2 == 0:
        idades_pares.append(i)

print(idades_pares)
