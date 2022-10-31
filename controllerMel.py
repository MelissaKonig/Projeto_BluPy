def salvarAlunos(dados_aluno):
    with open('alunosCadastrados.txt','a') as arquivo:
        arquivo.write(str(dados_aluno)+"\n")  

def listarAlunos():
    with open('alunosCadastrados.txt') as arquivo:  
        print(arquivo.read())