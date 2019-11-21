from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa
import PySimpleGUI as sg


class TelaSistema(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(selfs):
        print("components sistema")
        layout = [[sg.Button('Cadastro', size=(15, 2)), sg.Button('Relatório', size=(15, 2))],
                  [sg.Button('Movimentação', size=(15, 2)), sg.Button('Sair', size=(15, 2))]]

        selfs.window = sg.Window('Menu Inicial').Layout(layout)

    def lista_relatorio(self, registros, cadastros):
        print("Timestamp\t\t-\tIdent.\t-\tNome\t-\tTipo Pessoa\t-\tTipo")
        for registro in registros:
            tipo_pessoa = TipoPessoa.USUARIO if registro.matricula is not None else TipoPessoa.SEGURANCA
            if tipo_pessoa == tipo_pessoa.USUARIO:
                identificador = registro.matricula
                nome = next(filter(lambda c:
                                   c.matricula == registro.matricula, cadastros.usuarios
                                   ), "Não encontrado").nome
            else:
                identificador = str(registro.codigo)
                nome = next(filter(lambda c:
                                   c.codigo == registro.codigo, cadastros.segurancas
                                   ), "Não encontrado").nome

            print(
                registro.timestamp.strftime("%d-%m-%Y %H:%M:%S")
                + "\t-\t"
                + identificador
                + "\t-\t"
                + nome
                + "\t-\t"
                + tipo_pessoa.name
                + " \t-\t"
                + registro.tipo.name
            )

    def mostra_informacao(self, info):
        print(info["mensagem"])
        return input(info["input"])

    def retorna(self):
        print("Retornando...")