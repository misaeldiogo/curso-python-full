print("\nSomente numeros pares, começando do 0 até o número digitado")
n1 = int(input("\nDigite um número: "))

i = 1

for i in range(1, 21):   # forma 001
	if i % 2 == 0:
		print(i)
	i += 1
	
# FORMA 2
print("\nFORMA CERTA E MAIS RÁPIDA")
for i in range(2, 21, 2):
	print(i)