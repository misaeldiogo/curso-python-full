

try:
    x = int(input("Digite algo: "))
    print(5/x)

except ValueError:
    print("Você não digitou um número!")

except ZeroDivisionError:
    print("Você não pode dividir por zero!")
    
