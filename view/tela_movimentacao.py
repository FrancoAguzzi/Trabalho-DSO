from view.abstract_tela import AbstractTela
from model.movimentacao import Movimentacao


class TelaMovimentacao(AbstractTela):

    def __init__(self):
        pass

    def lista_entrada(self):
        print("Lista entrada")
        return Movimentacao.registro_entrada

    def lista_saida(self):
        print("Lista saida")
        return Movimentacao.registro_saida

    def mostra_informacao(self, info):
        print(info["mensagem"])
        return input(info["input"])