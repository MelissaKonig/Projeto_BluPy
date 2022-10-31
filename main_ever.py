from controller_ever import listar_curso, media, salvar
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
    menu()
