from controller_ever import listar_curso, cadastro_notas, media, salvar
import os

if __name__ == "__main__":    
    
    def menu():
        
        while True:      
            opcao = int(input("1. Cadastro de Curso\n2. Listar Cursos\n3. Cadastrar notas\n4. Mostrar média por aluno\nPor favor, digite o nr. da opção desejada: "))
            
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
                    cadastro_notas()
                
                case 4:
                    os.system('cls') 
                    media()                     
                    
                                                                                                                                 
                case 9:
                    os.system('cls')
                    print("\nAtendimento encerrado.\n") 
                    break                            
                
                                
                case _:
                    os.system('cls')
                    print("Exercício Inválido. Escolha entre 1 e xxxxxxx!\n")
    menu()
