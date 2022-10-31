'''
cadastro cursos
relatorio cursos
notas
'''

import os

def salvar(curso):
    #sintax com funcao open para arquivo txt, variavel criada refenciando o arquivo
    with open('cursos.txt', 'a') as arquivo:

        #variavel que referencia arquivo recebendo funcao write que recebe como atributo para escrita o cliente
        arquivo.write(str(curso)+"\n")
        os.system('cls')
        print(f"Curso cadastrado:\n{curso}")
        
        
def listar_curso():
    
    with open('cursos.txt') as arquivo:  
        print(f"Lista de cursos cadastrados:\n{arquivo.read()}")

def cadastro_notas():
    pass

def media():
    pass