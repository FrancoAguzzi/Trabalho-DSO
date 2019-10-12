from abstract_tela import AbstractTela
from control.controlador_sistema import ControladorSistema

class TelaSistema(AbstractTela):

    def __init__(self):
        pass

    def lista_relatorio(self):
        print(ControladorSistema.relatorio())

    def mostra_informacao(self, info):
        print(info)