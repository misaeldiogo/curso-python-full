from controller import PessoaController

while True:

    try:

        opcao = int(input("\nDigite (1) para cadastrar. Digite (2) para ver usuários cadastrados: "))

    except ValueError:

        print("\nATENÇÃO: Digite apenas números, por favor! \n")

        continue

    if opcao == 3:

        break

    if opcao == 2 :

        print("\nNão há usuário cadastrado!\n")


    if opcao == 1:

        nome = input("Digite o nome do usuário: ")

        idade = int(input("Digite a idade do usuário: "))
        
        cpf = input("Digite o CPF do usuário: ")

        if PessoaController.cadastrar(nome, idade, cpf):

            print("Usuário cadastrado com sucesso!")

        else:

            print("Erro ao cadastrar usuário!")



    

