from controller import listar_curso, media, salvar
from controller import salvarAlunos, listarAlunos
from controller import salvar_professor, exibir #puxando as minhas funcoes do outro arquivo
import os

if __name__ == "__main__":    
    
    def menu():
        
        while True:      
            opcao = int(input("1. Cadastro de Curso\n2. Listar Cursos\n3. Cadastrar notas\nPor favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    print("CADASTRO DE CURSOS")
                    curso = {}
                    curso['nome'] = str(input("Digite o nome do curso: "))
                    curso['carga_horaria'] = int(input("Digite a carga-horária : "))
                    curso['modalidade'] = str(input("Digite a modalidade (presencial ou EAD) : ")) 
                    curso['investimento'] = float(input("Digite o valor da mensalidade : "))
                    return salvar(curso)
                    
                case 2:
                    os.system('cls') 
                    listar_curso()
                
                case 3:
                    os.system('cls') 
                    nome = str(input('Digite o nome do aluno para cadastrar as notas: '))
                    n1 = float(input('Digite a primeira nota: '))
                    n2 = float(input('Digite a segunda nota: '))
                    n3 = float(input('Digite a terceira nota: '))
                    mediaAluno = (n1 + n2 + n3)/3
                    resultado = media(n1, n2, n3)
                    os.system('cls') 
                    print(f'O Calculo da Media do aluno: {nome} \nPrimeira nota: {n1} \nSegunda nota: {n2} \nTerceira nota: {n3}\nO Aluno esta com a média {mediaAluno:.2f}\nResultado: {resultado}')
                    break                                    
                                
                case _:
                    os.system('cls')
                    print("Exercício Inválido. Escolha entre 1 e xxxxxxx!\n")



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

            
        print("-"*25, "CADASTRO PROFESSOR", "-"*25) # imprimindo "CADASTRO PROFESSOR" com o polimorfismo ------ 
        
        opcao = int(input("Olá, você deseja cadastrar um professor(a)? \n1 - Sim\n2 - Não \n :>")) #aqui ele está salvando a minha opcao na variavel opcao e imprimindo o texto
        professores = {} #dicionario sem dados
        
        if opcao == 1: # um "if" para uma condição que esta pegando da variavel opcao
            professores['nome'] = str(input("Insira o nome do professor que queira cadastrar: ")) #exibindo uma informacao e salvando ela como 'nome'
            professores['idade'] = int(input("Insira a idade do professor que queira cadastrar: ")) #exibindo uma informacao e salvando ela como 'idade' 
            professores['salario'] = float(input("Insira o salario do professor que queira cadastrar: "))  #exibindo uma informacao e salvando ela como 'salario'     
            salvar_professor(professores) #salvando as informacoes no dicionario professores

        elif opcao == 2: # um "if" para uma condição que esta pegando da variavel opcao
            print("Finalizado!") #informando a finalizacao
            break #encerrendo o programa
    
    print(f"{exibir()}") #exibindo os dados





    menu()
