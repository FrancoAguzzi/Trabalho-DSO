from view.abstract_tela import AbstractTela
from model.movimentacao import Movimentacao
from getpass import getpass


class TelaMovimentacao(AbstractTela):

    def __init__(self):
        pass

    def lista_entrada(self):
        print("Lista entrada")
        return Movimentacao.registro_entrada

    def lista_saida(self):
        print("Lista saida")
        return Movimentacao.registro_saida

    def acesso_pessoa(self, tipo: str = "usuario"):
        print("Acesso de " + tipo)
        respostas = {}
        if(tipo == "usuario"):
            respostas["matricula"] = input("Informe sua matrícula: ")
            return respostas
        else:
            respostas["codigo"] = input("Informe seu código: ")
            respostas["senha_especial"] = getpass("Digite sua Senha Especial: ")
            return respostas

    def mostra_informacao(self, info):
        print(info["mensagem"])
        return input(info["input"])