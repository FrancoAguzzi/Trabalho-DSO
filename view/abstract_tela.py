from abc import ABC, abstractmethod
import os
import PySimpleGUI as sg

class AbstractTela(ABC):

    def __init__(self):
        self.__window = None
        self.components()
        print("Abstract Tela")

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    @abstractmethod
    def components(selfs):
        pass

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_informacao(self, info):
        pass

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")
