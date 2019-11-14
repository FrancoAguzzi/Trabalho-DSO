from view.abstract_tela import AbstractTela
from model.tipo import TipoRegistro
from getpass import getpass


class TelaMovimentacao(AbstractTela):

    def __init__(self):
        super().__init__()

    def lista_registros(self, registros, tipo_registro: TipoRegistro):
        print("Lista " + tipo_registro.name + ": ")
        for registro in registros:
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