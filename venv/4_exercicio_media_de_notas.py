print("========= MÉDIA DAS NOTAS ==============\n")

nota_um = float(input("Digite a nota do primeiro Bimestre: "))
nota_dois = float(input("Digite a nota do Segundo Bimestre: "))
nota_tres = float(input("Digite a nota do Terceiro Bimestre: "))
nota_quatro = float(input("Digite a nota do Quarto Bimestre: "))
aprovacao = 5

media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4  # Prioridade no cauculo >> coloco entre parenteses
print(f"A média do Aluno é: {media}")
