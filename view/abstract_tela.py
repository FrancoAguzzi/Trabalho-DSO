from abc import ABC, abstractmethod
import os
import PySimpleGUI as sg


class AbstractTela(ABC):

    def __init__(self):
        self.__window = None
        self.components()

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self, window):
        self.__window = window

    @abstractmethod
    def components(self):
        pass

    def hide(self):
        self.__window.Hide()

    def unhide(self):
        self.__window.UnHide()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
        self.__window = None

    def mostra_informacao(self, info):
        pass

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")
