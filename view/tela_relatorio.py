import PySimpleGUI as sg
from view.abstract_tela import AbstractTela

class TelaRelatorio(AbstractTela):

    def __init__(self):
        super().__init__

    def components(selfs):

        layout = [[sg.InputCombo(('Sem filtro', 'Matrícula', 'Código', 'Tipo Pessoa', 'Tipo Registro', 'Data')), sg.Button(('Ir'), size=(10,2))]
                  [sg.Button(('Voltar'), size=(10,1))]]

        self.window = sg.Window('Menu Relatório').Layout(layout)
        self.open()