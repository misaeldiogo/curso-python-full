import os

##x = lambda: print("Olá")

####x = lambda: 10
#x()  # Output: Olá
#print(type(x))  # Output: <class 'function'>

####print(x())


# x = lambda: os.system("clear")

# ==========

x = lambda *idade: print(idade)
x("Oi", 23, "idade")  # Output: Olá 20 anos

print(x)

# ==============

def teste():
    return lambda *idade: print(idade)

x = teste()
x("Olá", 20, "anos")  # Output: Olá 20 anos

