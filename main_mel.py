"""
Criar cadastro para alunos e depois listar os cadastros.

"""
from controllerMel import *





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
        dados_aluno["nome"] = input(("Digite o nome completo do aluno: "))
        dados_aluno["sobrenome"] = input(("Digite o ano em que o aluno se encontra: "))
        dados_aluno["idade"] = input(("Digite a matrícula do aluno: "))
        dados_aluno["notas"] = ()
        salvarAlunos(dados_aluno)
    print("Aluno cadastrado!")

    if escolha == "B":
        print(listarAlunos())
    
menu()