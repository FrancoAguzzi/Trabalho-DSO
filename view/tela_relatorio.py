import PySimpleGUI as sg
from view.abstract_tela import AbstractTela

class TelaRelatorio(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self):
        layout = [[sg.InputCombo(('Sem filtro', 'Identificador', 'Tipo Pessoa', 'Tipo Registro', 'Data'), key="option")],
                  [sg.Button('Ir', size=(10, 1)), sg.Button('Início', size=(10, 1))]]

        self.window = sg.Window('Menu Relatório').Layout(layout)
