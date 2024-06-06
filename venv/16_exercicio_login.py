# Definir usuário e senha
# login do usuário é valido

USUARIO = "diogo"
SENHA = "123"

while True:
    usuario_login = input("Digite seu nome de usuário: ")
    senha_login = input("Digite sua senha: ")

    if usuario_login == USUARIO and senha_login == SENHA:
        print("Login realizado com sucesso!")
        break
    else:
        print("Usuário ou senha invalidos. Tente novamente!")