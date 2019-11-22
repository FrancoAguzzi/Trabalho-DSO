from view.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(selfs):
        layout = [[sg.Button('Cadastro', size=(15, 2)), sg.Button('Relatório', size=(15, 2))],
                  [sg.Button('Movimentação', size=(15, 2)), sg.Button('Sair', size=(15, 2))]]

        selfs.window = sg.Window('Menu Inicial').Layout(layout)