from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa
import PySimpleGUI as sg


class SelectTipo(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self):
        layout = [[sg.Button('Usuário', size=(10, 1)), sg.Button('Segurança', size=(10, 1))]]
        self.window = sg.Window('Selecionar Tipo').Layout(layout)