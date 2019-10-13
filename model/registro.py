from model.tipo import TipoRegistro


class Registro:

    def __init__(self, timestamp, tipo: TipoRegistro, matricula=None, codigo=None):
        self.__timestamp = timestamp
        self.__matricula = matricula
        self.__codigo = codigo
        self.__tipo = tipo

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
