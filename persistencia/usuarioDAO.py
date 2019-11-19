import pickle
from model.usuario import Usuario
from persistencia.abstract_dao import AbstractDAO

class UsuarioDAO(AbstractDAO):

    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        super().add(usuario.matricula, usuario)

    def get(self, matricula):
        if (isinstance(matricula, int)):
            return super().get(matricula)

    def remove(self, matricula):
        if (isinstance(matricula, int)):
            return super().remove(matricula)