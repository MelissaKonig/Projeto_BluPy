def salvar_professor(professores):
    with open('dadosProfessor.txt', 'a') as arquivo:
        arquivo.write(f'{professores}\n')

def exibir():
    with open('dadosProfessor.txt', 'r') as arquivo:
         print(arquivo.read())