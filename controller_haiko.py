def salvar_professor(professores):#criando funcao e pegando os dados dos professores
    with open('dadosProfessor.txt', 'a') as arquivo: #abrindo o arquivo txt
        arquivo.write(f'{professores}\n') #salvando tudo no arquivo txt os dados que tinham no professor

def exibir(): #criando uma funcao 
    with open('dadosProfessor.txt', 'r') as arquivo: #abrindo o arquivo txt
         print(arquivo.read())# exibindo todas as informacao do arquivo txt