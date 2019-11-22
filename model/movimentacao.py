class Movimentacao:

    def __init__(self, vagas: int = 0):
        self.__vagas = vagas

    @property
    def vagas(self):
        return self.__vagas

    @vagas.setter
    def vagas(self, vagas):
        self.__vagas = vagas
