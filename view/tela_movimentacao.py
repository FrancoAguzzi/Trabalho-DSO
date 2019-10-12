from abstract_tela import AbstractTela
from model.movimentacao import Movimentacao
from control.controlador_movimentacao import ControladorMovimentacao

class TelaMovimentacao(AbstractTela):

    def __init__(self):
        pass

    def lista_entrada(self):
        print(Movimentacao.registro_entrada())

    def lista_saida(self):
        print(Movimentacao.registro_saida())

    def acesso_pessoa(self):
        print(ControladorMovimentacao.acesso())

    def mostra_informacao(self, info):
        print(info)