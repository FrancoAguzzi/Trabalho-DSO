import pickle
from abstract_dao import AbstractDAO
from model.seguranca import Seguranca

class SegurancaDAO(AbstractDAO):

    def __init__(self):
        super().__init__('segurancas.pkl')

    def add(self, seguranca: Seguranca):
        if (isinstance(usuario.matricula, int)) and (usuario is not None) \
            and (isinstance(usuario, Usuario)):
            super().add(usuario.matricula, usuario)

    def get(self, matricula):
        if (isinstance(matricula, int)):
            return super().get(matricula)

    def remove(self, matricula):
        if (isinstance(matricula, int)):
            return super().remove(matricula)