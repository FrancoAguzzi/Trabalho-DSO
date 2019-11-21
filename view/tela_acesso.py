from view.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaAcesso(AbstractTela):

    def __init__(self):
        super().__init__()

    def components(self, senha=False):
        layout = [[sg.Text('Digite sua senha' if senha else 'Digite sua matrícula/código')],
                 [sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='input')],
                 [sg.ReadButton('1'), sg.ReadButton('2'), sg.ReadButton('3')],
                 [sg.ReadButton('4'), sg.ReadButton('5'), sg.ReadButton('6')],
                 [sg.ReadButton('7'), sg.ReadButton('8'), sg.ReadButton('9')],
                 [sg.ReadButton('Limpar'), sg.ReadButton('0'), sg.ReadButton('Ir')]]
        self.window = sg.Window('Acessar', default_button_element_size=(5, 2),
                auto_size_buttons=False, grab_anywhere=False).Layout(layout)