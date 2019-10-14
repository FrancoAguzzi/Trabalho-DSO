from abc import ABC, abstractmethod
import os


class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_informacao(self, info):
        pass

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")
