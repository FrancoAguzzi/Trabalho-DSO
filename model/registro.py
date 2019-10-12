class Registro:

    def __init__(self, timestamp: Date, matricula = None, codigo = None):
        self.__timestamp = timestamp
        self.__matricula = matricula
        self.__codigo = codigo

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp

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
