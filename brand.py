from funcaoes import salvar_professor, exibir


def menu():
    professores = {}
    
    while True: 
    
        print("-"*25, "CADASTRO PROFESSOR", "-"*25)
        
        opcao = int(input("Olá, você deseja cadastrar um professor(a)? \n1 - Sim\n2 - Não \n :>"))
        
        if opcao == 1:    
            professores['nome'] = str(input("Insira o nome do professor que queira cadastrar: "))
            professores['idade'] = int(input("Insira a idade do professor que queira cadastrar: "))  
            professores['salario'] = float(input("Insira o salario do professor que queira cadastrar: "))      
            salvar_professor(professores)

        elif opcao == 2:
            print("Finalizado!")
            break
    
    print(f"{exibir()}")
    
menu()