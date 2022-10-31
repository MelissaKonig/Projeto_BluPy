"""
Parte Mel:
1. Criar cadastro Alunos.
2. Reproduzir listagem Alunos.

"""
#Import das funções constantes no controller.
from controllerMel import salvarAlunos, listarAlunos


#Função menu de alunos (única que consta na main)
def menu():

    print('''
        Seja bem-vindo! Como gostaria de prosseguir?
        [A] - Cadastrar Aluno.
        [B] - Relatório de Alunos.
    ''')
    
    cadastroAluno = "A"
    relatorioAlunos = "B"

    escolha = str(input('Escolha uma das opções listadas: '))

    #Dicionário save cadastro alunos.
    if escolha == "A":
        dados_aluno = {}
        dados_aluno["nome"] = input(str("Digite o nome completo do aluno: "))
        dados_aluno["ano"] = input(str("Digite o ano em que o aluno se encontra: "))
        dados_aluno["matricula"] = input(int("Digite a matrícula do aluno: "))
        dados_aluno["CPF"] = input(int("Digite o CPF do aluno: "))
        salvarAlunos(dados_aluno)
    
    print("Aluno cadastrado!")

    #Escolha do usuário para listagem dos alunos cadastrados.
    if escolha == "B":
        print(listarAlunos())
    
menu() #Fim função menu.