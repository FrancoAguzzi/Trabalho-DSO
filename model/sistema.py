from cadastro import Cadastro
from movimentacao import Movimentacao

class Sistema:

    def __init__(self, cadastro = Cadastro(), movimentacao = Movimentacao()):
        self.__cadastro = cadastro
        self.__movimentacao = movimentacao

    @property
    def cadastro(self):
        return self.__cadastro

    @cadastro.setter
    def cadastro(self, cadastro):
        self.__cadastro = cadastro

    @property
    def movimentacao(self):
        return self.__movimentacao

    @movimentacao.setter
    def movimentacao(self, movimentacao):
        self.__movimentacao = movimentacao
