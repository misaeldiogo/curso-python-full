# Receba um numero e mostre todos numeros pares

print("\nSomente numeros pares, começando do 0 até o número digitado")
n1 = int(input("\nDigite um número: "))

i = 1
while i <= n1:
	if i % 2 == 0:
		print(i)
	i += 1

