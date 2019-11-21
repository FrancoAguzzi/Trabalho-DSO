import PySimpleGUI as sg
from view.abstract_tela import AbstractTela

class TelaFiltro(AbstractTela):

    def __init__(self):
        super().__init__

    def components(self):

        layout = [[sg.Text('Filtro'), sg.InputText()],
                  [sg.Listbox(lista_registro, size=(50, 6))],
                  [sg.Button('Voltar'), size=(10,1)]]

        self.window = sg.Window('Relatório').Layout(layout)
        self.open()