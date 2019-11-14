from model.pessoa import Pessoa


class Usuario(Pessoa):

    def __init__(self, nome, telefone, matricula: str):
        super().__init__(nome, telefone)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
