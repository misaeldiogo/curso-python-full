# Escreva um programa que receba notas de um aluno (0 a 10), 
# caso a nota digitada esteja fora do intervalo, peça ao usuário para digitar novamente.


while True:
    nota_aluno = int(input("Digite a nota do Aluno: "))

    if nota_aluno >= 0 and nota_aluno <= 100:
        print(f" A nota {nota_aluno} é válida!")
        break
    
    print("Nota invalida, digite novamente!")