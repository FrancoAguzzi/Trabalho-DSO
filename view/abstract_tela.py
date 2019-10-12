from abc import ABC, abstractmethod

class AbstractTela(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mostra_informacao(self, info):
        pass