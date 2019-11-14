class OpcaoInvalidaException(Exception):

    def __init__(self):
        super().__init__("Opção Inválida")
