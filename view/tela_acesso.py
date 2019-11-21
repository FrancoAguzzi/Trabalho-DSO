from abstract_tela import AbstractTela

class TelaAcesso(AbstractTela):

    def __init__(self):
        super().__init__

    def components(selfs):

        layout = [[sg.Text('Digite sua matrícula/código')],
                 [sg.Input(size=(10, 1), do_not_clear=True, justification='left', key='input')],
                 [sg.ReadButton('1'), sg.ReadButton('2'), sg.ReadButton('3')],
                 [sg.ReadButton('4'), sg.ReadButton('5'), sg.ReadButton('6')],
                 [sg.ReadButton('7'), sg.ReadButton('8'), sg.ReadButton('9')],
                 [sg.ReadButton('Limpar'), sg.ReadButton('0'), sg.ReadButton('Ir')],
                 [sg.Text('', size=(15, 1), font=('Helvetica', 18), text_color='blue', key='out')]]
        window = sg.Window('Acesso', default_button_element_size=(5, 2),
                auto_size_buttons=False, grab_anywhere=False).Layout(layout)

        keys_entered = ''
        while True:
            button, values = window.Read()
            if button is None:
                break
            if button == 'Clear':
                keys_entered = ''
            elif button in '1234567890':
                keys_entered = values['input']
            keys_entered += button
            elif button == 'Submit':
            keys_entered = values['input']
            window.FindElement('out').Update(keys_entered)
        window.FindElement('input').Update(keys_entered)