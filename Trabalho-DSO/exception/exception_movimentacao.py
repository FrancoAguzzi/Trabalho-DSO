class BicicletarioLotadoException(Exception):

    def __init__(self):
        super().__init__("Bicicletário Lotado")


class CodigoSenhaInvalidoException(Exception):

    def __init__(self):
        super().__init__("Código e/ou Senha Inválido(a)")