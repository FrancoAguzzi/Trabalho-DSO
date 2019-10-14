class Movimentacao:

    def __init__(self, vagas: int = 0):
        self.__vagas = vagas
        self.__registros = []

    @property
    def registros(self):
        return self.__registros

    @property
    def vagas(self):
        return self.__vagas

    @vagas.setter
    def vagas(self, vagas):
        self.__vagas = vagas
