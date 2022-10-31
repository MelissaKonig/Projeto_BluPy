'''
cadastro cursos
relatorio cursos
notas
'''

import os

def salvar(curso):
    
    with open('cursos.txt', 'a') as arquivo:        
        arquivo.write(str(curso)+"\n")
        os.system('cls')
        print(f"Curso cadastrado:\n{curso}")
        
        
def listar_curso():    
    with open('cursos.txt') as arquivo:  
        print(f"Lista de cursos cadastrados:\n{arquivo.read()}")

def media(n1, n2, n3):

    media = (n1 + n2 + n3) / 3
    if media >= 7:
        media = f'Aprovado'
    elif media >= 5:
        media = f'Em recuperação'
    else:
        media = f'Reprovado'
    return media