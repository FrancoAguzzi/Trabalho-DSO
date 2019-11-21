from view.abstract_tela import AbstractTela
import os
import PySimpleGUI as sg


class Popups():

    def __init__(self):
        pass

    def default(self, title, message):
        return sg.Popup(title, message)

    def confirm(self, title, message):
        return sg.PopupYesNo(title, message)

    def error(self, title, message):
        return sg.PopupError(title, message)

    def simple_input(self, title, message):
        return sg.PopupGetText(title, message)