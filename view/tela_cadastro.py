from view.abstract_tela import AbstractTela
from getpass import getpass
from model.tipo import TipoPessoa
import PySimpleGUI as sg


class TelaCadastro(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self, tipo=TipoPessoa.USUARIO, pessoas=None):
        if pessoas is None:
            pessoas = {}
        lista = ["Nome - Telefone - ID"]
        for pessoa in pessoas:
            identificador = pessoa.codigo if hasattr(pessoa, "codigo") else pessoa.matricula
            lista.append((pessoa.nome
                          + " - "
                          + str(pessoa.telefone)
                          + " - "
                          + str(identificador)))

        layout = [[sg.Listbox(lista, size=(50, 6))],
                  [sg.Button('Novo', size=(10, 1)), sg.Button('Editar', size=(10, 1)),
                   sg.Button('Excluir', size=(10, 1)), sg.Button('Início', size=(10, 1))]]
        self.window = sg.Window('Menu Cadastro ' + tipo.name).Layout(layout)
