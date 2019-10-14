class Cadastro:

    def __init__(self, usuarios=None, segurancas=None):
        if segurancas is None:
            segurancas = []
        if usuarios is None:
            usuarios = []
        self.__usuarios = usuarios
        self.__segurancas = segurancas

    @property
    def segurancas(self):
        return self.__segurancas

    @segurancas.setter
    def segurancas(self, segurancas):
        self.__segurancas = segurancas

    @property
    def usuarios(self):
        return self.__usuarios

    @usuarios.setter
    def usuarios(self, usuarios):
        self.__usuarios = usuarios
