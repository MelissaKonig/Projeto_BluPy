'''
cadastro cursos
relatorio cursos
notas
'''

import os

def cadastro_curso():
    print("CADASTRO DE CURSOS")
    curso = {}
    curso['nome'] = str(input("Digite o nome do curso: "))
    curso['carga_horaria'] = int(input("Digite a carga-horária : "))
    curso['modalidade'] = str(input("Digite a carga-horária : ")) 
    curso['investimento'] = float(input("Digite o valor da mensalidade : "))
    return salvar(curso)

def salvar(curso):
    pass


def listar_curso():
    pass


def cadastro_notas():
    pass


def media():
    pass