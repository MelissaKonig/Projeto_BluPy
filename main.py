"""
Criar cadastro para alunos e depois listar os cadastros.

"""
from controller import *





def menu():

    print('''
        Seja bem-vindo! Como gostaria de prosseguir?
        [A] - Cadastrar Aluno.
        [B] - Relatório de Alunos.
    ''')

    escolha = str(input('Escolha uma das opções listadas: '))

    cadastroAluno = "A"
    relatorioAlunos = "B"

    if escolha == "A":
        dados_aluno = {}
        dados_aluno["nome"] = input(("Digite seu nome: "))
        dados_aluno["sobrenome"] = input(("Digite seu sobrenome: "))
        dados_aluno["idade"] = input(("Digite sua idade: "))
        salvar_alunos(dados_aluno)

    if escolha == "B":
        print(listarAlunos())