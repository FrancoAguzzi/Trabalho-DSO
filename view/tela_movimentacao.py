from view.abstract_tela import AbstractTela


class TelaMovimentacao(AbstractTela):

    def __init__(self):
        pass

    def lista_entrada(self):
        print("Lista entrada")

    def lista_saida(self):
        print("Lista saida")

    def acesso_pessoa(self):
        print("Acesso pessoa")

    def mostra_informacao(self, info):
        print(info)