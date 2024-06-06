
nome = "Diogo Misael Paz da Silva Jr"
idade = 32

resultado = f"Olá {nome}, feliz aniversário, você está feliz em completar {idade} anos? "
print(resultado)

# pedir ao usuário para digitar a idade uso o input()

# Se eu deixar da forma que esta acima, não vai aparecer informação para o usuário saber o que deve ser feito. Vai ficar apenas um espaço para digitar qualquer coisa. 

# No caso preciso explicar ao usuário o que ele precisa fazer, logo, posso fazer de duas formas

# 1 - colocando print em cima >>> não é recomendado

print("Digite a sua idade: ")   #  Nesse caso não é recomenado, mas pode ser feito, vai funcionar.
idade = input()
print(f"Sua idade é {idade} anos")

# Observação: Aqui a resposta vai para a linha de baixo.

# 2 - colocando a pergunta dentro de INPUT

idade = input("Digite a sua idade: ")
print(f"Sua idade é {idade} anos")

# Observação: Aqui a resposta fica na mesma linha ||  Se eu quiser jogar para a linha de baixo, é só colocar >> \n