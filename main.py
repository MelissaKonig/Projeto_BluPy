"""
Criar cadastro para alunos e depois listar os cadastros.

"""
from controller import *





def menu():
    
    while True:
        print('-'* 30)
        
        dados_aluno = {}
        dados_aluno["nome"] = input(("Digite seu nome: "))
        dados_aluno["sobrenome"] = input(("Digite seu sobrenome: "))
        dados_aluno["idade"] = input(("Digite sua idade: "))
        salvar_alunos(dados_aluno)