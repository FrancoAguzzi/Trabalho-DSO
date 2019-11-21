from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa
import PySimpleGUI as sg


class SelectTipo(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self):
        layout = [[sg.Button('Usuário', size=(10, 1)), sg.Button('Segurança', size=(10, 1))]]
        self.window = sg.Window('Selecionar Tipo').Layout(layout)

    def open(self):
        self.unhide()
        button, values = self.window.Read()
        self.hide()
        if button == "Usuário":
            return TipoPessoa.USUARIO
        else:
            return TipoPessoa.SEGURANCA
