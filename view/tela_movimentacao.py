from view.abstract_tela import AbstractTela
from model.tipo import TipoRegistro
from getpass import getpass
import PySimpleGUI as sg
from persistencia.registroDAO import RegistroDAO


class TelaMovimentacao(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self):
        layout = [[sg.Button('Acessar', size=(34, 4))],
                  [sg.Button('Excluir', size=(10, 1)), sg.Button('Atualizar', size=(10 ,1)), sg.Button('Início', size=(10, 1))]]

        self.window = sg.Window('Menu Movimentação').Layout(layout)

    def lista_registros(self, tipo_registro: TipoRegistro):
        print("Lista " + tipo_registro.name + ": ")
        for registro in RegistroDAO.get_all():
            if registro.tipo == TipoRegistro:
                print(registro)

    def acesso_pessoa(self, tipo: str = "usuario"):
        print("Acesso de " + tipo)
        respostas = {}
        if tipo == "usuario":
            respostas["matricula"] = input("Informe sua matrícula: ")
            return respostas
        else:
            respostas["codigo"] = input("Informe seu código: ")
            respostas["senha_especial"] = getpass("Digite sua Senha Especial: ")
            return respostas

    def mostra_informacao(self, info):
        print(info["mensagem"])
        return input(info["input"])

    def movimenta_bicicleta(self, n=True):
        if n:
            print("Coloque sua bicicleta em um local disponível")
        else:
            print("Retire sua bicicleta")

    def libera_acesso(self, nome):
        print ("Acesso Liberado, " + nome)

    def modifica_registro(self, n=False):
        acao = "alterado"
        if n:
            acao = "removido"
        return "Registro " + acao + " com sucesso!"