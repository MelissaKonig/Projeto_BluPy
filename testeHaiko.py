
# Criando form e usando botões
import PySimpleGUI as pg
from controller import *


# Passo 1: Setar o theme
pg.theme('SandyBeach')

# Passo 2: Criar layout

layout = [
    [pg.Text("Nome: ", size=(9,1), key='aluno_nome'),pg.InputText(do_not_clear=False)],

    [pg.Text("Idade: ", size=(9,1), key='aluno_idade'),pg.InputText(do_not_clear=False)],

    [pg.Text("CPF: ", size=(9,1), key='aluno_cpf'),pg.InputText(do_not_clear=False)],

    [pg.Text("Matrícula: ", size=(9,1), key='aluno_matricula'),pg.InputText(do_not_clear=False)],

    [pg.Text("Cursos: "),pg.Listbox(["Python", "Java", "JavaScript", "C++"], size=(30,5), select_mode=pg.LISTBOX_SELECT_MODE_MULTIPLE)],

    [pg.Button("Cadastrar"),pg.Button("Sair")]
]

# Passo 3: Criar Window
window = pg.Window("CADASTRO", layout)

# Passo 4: Event Loop
while True:
    event, values = window.read()

    if event == pg. WIN_CLOSED or event == "Sair":
        break

    elif event == "Cadastrar":
        
        print(f"Nome: {values[0]}")
        print(f"Idade: {values[1]}")
        print(f"CPF: {values[2]}")
        print(f"Matrícula: {values[3]}")
        print(f"Curso(s): {values[4]}")
        
        dados_aluno = {}                        
        dados_aluno['nome'] = values[0]
        dados_aluno['idade'] = values[1]
        dados_aluno['CPF'] = values[2]
        dados_aluno['matricula'] = values[3]
        dados_aluno['cursos'] = values[4]
        salvarAlunosTeste(dados_aluno) 


        for item in values:
            values[item]: None
              

# Passo 5: Close Windows
window.close()
exit()