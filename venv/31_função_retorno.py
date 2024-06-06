def soma_valores(n1, n2):
    soma = n1 + n2
    return soma


x = soma_valores(1, 2) + 4

print(x)

## COMPACTAR

def soma_valores(n1, n2):
    soma = n1 + n2
    return soma, 1, 2
    print("oi") #  <<<< APÓS O RETURN, ELE NÃO MOSTRA NADA 


x = soma_valores(1, 2)

print(x)