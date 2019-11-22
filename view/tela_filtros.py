import PySimpleGUI as sg
from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa


class TelaFiltro(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self, registros=None, cadastros=None):
        if registros is None:
            registros = []

        usuarios = []
        segurancas = []

        if cadastros:
            usuarios, segurancas = cadastros

        lista_registros = ["Timestamp  -  Ident.  -  Nome  -  Tipo Pessoa  -  Tipo"]

        for registro in registros:
            tipo_pessoa = TipoPessoa.USUARIO if registro.matricula is not None else TipoPessoa.SEGURANCA
            if tipo_pessoa == tipo_pessoa.USUARIO:
                identificador = registro.matricula
                pessoa = next(filter(lambda c: c.matricula == registro.matricula, usuarios), None)
                if pessoa is None:
                    nome = "Não encontrado"
                else:
                    nome = pessoa.nome
            else:
                identificador = str(registro.codigo)
                pessoa = next(filter(lambda c: c.codigo == registro.codigo, segurancas), None)
                if pessoa is None:
                    nome = "Não encontrado"
                else:
                    nome = pessoa.nome

            lista_registros.append(
                registro.timestamp.strftime("%d-%m-%Y %H:%M:%S")
                + "  -  "
                + identificador
                + "  -  "
                + nome
                + "  -  "
                + tipo_pessoa.name
                + "  - "
                + registro.tipo.name
            )

        layout = [[sg.Listbox(lista_registros, size=(50, 6))],
                  [sg.Button('Início', size=(10, 1))]]

        self.window = sg.Window('Relatório').Layout(layout)