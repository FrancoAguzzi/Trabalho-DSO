from view.abstract_tela import AbstractTela
from model.tipo import TipoRegistro
from getpass import getpass
import PySimpleGUI as sg

class TelaMovimentacao(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self):
        layout = [[sg.Button('Acessar', size=(30, 4), pad=(25,0))],
                  [sg.Button('Excluir', size=(10, 1)), sg.Button('Atualizar', size=(10 ,1)), sg.Button('Início', size=(10, 1))]]

        self.window = sg.Window('Menu Movimentação').Layout(layout)
