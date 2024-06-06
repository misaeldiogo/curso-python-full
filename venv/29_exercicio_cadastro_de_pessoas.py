
pessoas = []

while True:
    decisao = int(input("\nDigite (1) para fazer o seu cadastro. Digite (2) para sair: "))
    if decisao == 2:
        break
    
    nome = input("\nDigite o nome: ")
    cpf = input("\nDigite o CPF: ")
    idade = input("\nDigite a idade: ")
    pessoa = {"nome": nome, "CPF": cpf, "idade": idade}
    pessoas.append(pessoa)

print(pessoas)

