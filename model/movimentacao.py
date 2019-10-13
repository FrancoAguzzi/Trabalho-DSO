class Movimentacao:

    def __init__(self, registro_entrada = [], registro_saida = [], vagas: int = 0):
        self.__registro_entrada = registro_entrada
        self.__registro_saida = registro_saida
        self.__vagas = vagas
        self.__registros = []

    @property
    def registros(self):
        return self.__registros

    @property
    def registro_entrada(self):
        return self.__registro_entrada

    @registro_entrada.setter
    def registro_entrada(self, registro_entrada):
        self.__registro_entrada = registro_entrada

    @property
    def registro_saida(self):
        return self.__registro_saida

    @registro_saida.setter
    def registro_saida(self, registro_saida):
        self.__registro_saida = registro_saida

    @property
    def vagas(self):
        return self.__vagas

    @vagas.setter
    def vagas(self, vagas):
        self.__vagas = vagas


