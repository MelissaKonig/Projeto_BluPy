def salvar_alunos(dados_aluno):
    with open('nomes.txt','a') as arquivo:
        arquivo.write(str(dados_aluno)+"\n")  

def listaralunos():
    with open('alunosCadastrados.txt') as arquivo:  
        print(arquivo.read())