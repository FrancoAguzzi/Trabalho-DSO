from model.pessoa import Pessoa


class Seguranca(Pessoa):

    def __init__(self, nome: str, telefone: int, senha_especial: str, codigo: int):
        super().__init__(nome, telefone)
        self.__senha_especial = senha_especial
        self.__codigo = codigo

    @property
    def senha_especial(self):
        return self.__senha_especial

    @senha_especial.setter
    def senha_especial(self, senha_especial):
        self.__senha_especial = senha_especial

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
