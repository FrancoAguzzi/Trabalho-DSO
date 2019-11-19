import pickle
from persistencia.abstract_dao import AbstractDAO
from model.seguranca import Seguranca

class SegurancaDAO(AbstractDAO):

    def __init__(self):
        super().__init__('segurancas.pkl')

    def add(self, seguranca: Seguranca):
        super().add(seguranca.codigo, seguranca)

    def get(self, codigo):
        if (isinstance(codigo, int)):
            return super().get(codigo)

    def remove(self, codigo):
        if (isinstance(codigo, int)):
            return super().remove(codigo)