class UsuarioDuplicadoException(Exception):

    def __init__(self):
        super().__init__("Usuário já cadastrado")


class MatriculaInvalidaException(Exception):

    def __init__(self):
        super().__init__("Matricula Inválida")


class SegurancaDuplicadoException(Exception):

    def __init__(self):
        super().__init__("Segurança já cadastrado")


class CodigoInvalidoException(Exception):

    def __init__(self):
        super().__init__("Código Inválido")