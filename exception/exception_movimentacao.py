class BicicletarioLotadoException(Exception):

    def __init__(self):
        super().__init__("Bicicletário Lotado")

class MatriculaInvalidaException(Exception):

    def __init__(self):
        super()__init__("Matrícula Inválida")

class CodigoSenhaInvalidoException(Exception):

    def __init__(self):
        super().__init__("Código e/ou Senha Inválido(a)")