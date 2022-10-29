from controller import cadastro_curso, listar_curso, cadastro_notas, media
import os

if __name__ == "__main__":    
    
    def menu():
        
        while True:      
            opcao = int(input("1. Cadastro de Curso\n2. Listar Cursos\n3. Cadastrar notas\n4. Mostrar média por aluno\nPor favor, digite o nr. da opção desejada: "))
            
            match opcao:
                case 1:
                    os.system('cls') 
                    cadastro_curso()
                    
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
