from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa
import PySimpleGUI as sg


class FormCadastro(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self, tipo=TipoPessoa.USUARIO, novo=True):
        if tipo == TipoPessoa.USUARIO:
            layout = [[sg.Text('Matrícula:'), sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='matricula', disabled=(not novo))]]
        else:
            layout = [[sg.Text('Código:'), sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='codigo', disabled=(not novo))],
                      [sg.Text('Senha:'), sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='senha_especial')]]

        layout.append([sg.Text('Nome:'), sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='nome')])
        layout.append([sg.Text('Telefone:'), sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='telefone')])
        layout.append([sg.Button("Salvar")])

        self.window = sg.Window("Novo Cadastro " if novo else "Atualizando Cadastro " + tipo.name).Layout(layout)