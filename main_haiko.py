from controller_haiko import salvar_professor, exibir #puxando as minhas funcoes do outro arquivo


def menu(): #abrindo uma funcao
    professores = {} #dicionario sem dados
    
    while True:  #Abrindo o programa com while true
    
        print("-"*25, "CADASTRO PROFESSOR", "-"*25) # imprimindo "CADASTRO PROFESSOR" com o polimorfismo ------ 
        
        opcao = int(input("Olá, você deseja cadastrar um professor(a)? \n1 - Sim\n2 - Não \n :>")) #aqui ele está salvando a minha opcao na variavel opcao e imprimindo o texto
        
        if opcao == 1: # um "if" para uma condição que esta pegando da variavel opcao
            professores['nome'] = str(input("Insira o nome do professor que queira cadastrar: ")) #exibindo uma informacao e salvando ela como 'nome'
            professores['idade'] = int(input("Insira a idade do professor que queira cadastrar: ")) #exibindo uma informacao e salvando ela como 'idade' 
            professores['salario'] = float(input("Insira o salario do professor que queira cadastrar: "))  #exibindo uma informacao e salvando ela como 'salario'     
            salvar_professor(professores) #salvando as informacoes no dicionario professores

        elif opcao == 2: # um "if" para uma condição que esta pegando da variavel opcao
            print("Finalizado!") #informando a finalizacao
            break #encerrendo o programa
    
    print(f"{exibir()}") #exibindo os dados
    
menu() #apresentando na tela a funcao menu