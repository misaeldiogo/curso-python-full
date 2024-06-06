
# INCLUINDO OPÇÕES QUE NÃO ESTAVAM DENTRO DAS CHAVES

pessoa = {"nome": "diogo", "idade": 21, "altura": 180}
pessoa.update({"cep": "123", "CPF": "145"})

print(pessoa)
