arquivo = open("pessoal.txt", "a")
# arquivo.write("Pessoa 21 - 40 anos\n")

i = 0

while True:
    if i > 4:
        break
    arquivo.write(input("Digite o nome da pessoa: \n"))
    i += 1