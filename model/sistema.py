class Sistema:

    def __init__(self, cadastros, movimentacao):
        self.__cadastros = cadastros
        self.__movimentacao = movimentacao

    @property
    def cadastros(self):
        return self.__cadastros

    @cadastros.setter
    def cadastros(self, cadastros):
        self.__cadastros = cadastros

    @property
    def movimentacao(self):
        return self.__movimentacao

    @movimentacao.setter
    def movimentacao(self, movimentacao):
        self.__movimentacao = movimentacao
