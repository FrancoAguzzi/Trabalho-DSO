from abstract_dao import AbstractDAO
import pickle
from model.registro import *

class RegistroDAO(AbstractDAO):

    def __init__(self):
        super().__init__('registros.pkl')

    def add(self, registro: Registro):
        super.add(registro.tipo, registro)

    def get(self, filtro):
        return super().get(tipo)

    def remove(self, filtro):
        return super().remove(tipo)