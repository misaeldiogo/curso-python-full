i = 0
print("\nProximo, até o 0\n")
while i < 10:
	print(i)
	break
	i = i + 1


i = 0
print("\nProximo, até o 2\n")
while i < 10:
	print(i)
	if i>= 2:
		break
	i = i + 1


i = 0
print("\nProximo, pula numeros pares, começando do 0 até o 19\n")
while i < 20:
	print(i)
	if i % 2 == 1:
		i = i + 2
		continue
	i = i + 1

	