from dal import PessoaDal
from model import Pessoa

class PessoaController:
  @classmethod
  def cadastrar(cls, nome, idade: int, cpf):
      if len(nome) > 2 and (idade > 0 and idade < 200) and len(cpf) == 11:
          try:
              if PessoaDal.salvar(Pessoa(nome, idade, cpf)):
                  print("Usuário cadastrado com sucesso!")
                  return PessoaController.usuarios_cadastrados()
              else:
                  print("Erro ao cadastrar usuário!")
                  return False
          except Exception as e:
              print(f"Erro ao cadastrar usuário: {e}")
              return False
      else:
          print("Dados inválidos para cadastro.")
          return False
      
    

  @classmethod
  def usuarios_cadastrados(cls):
      return PessoaDal.ler_todos()

