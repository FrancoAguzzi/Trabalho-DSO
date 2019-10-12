from control.controlador_cadastro import ControladorCadastro
from control.controlador_movimentacao import ControladorMovimentacao


class ControladorSistema:

    def __init__(self):
        self.__controladorCadastro = ControladorCadastro()

    def relatorio(self, filtro):
        pass

    def inicia(self):
        print("Iniciando...")
        print("Criando usuários e seguranças padrão...")
        self.__controladorCadastro.inclui_usuario({"nome": "Fulano", "telefone": 123123, "matricula": "16207180"})
        self.__controladorCadastro.inclui_seguranca({"nome": "Zé", "telefone": 321321, "codigo": 1, "senha_especial": "senha"})
        print("Usuários e Seguranças criados!")
        self.__controladorCadastro.lista_usuarios()
        self.__controladorCadastro.lista_segurancas()
        print("Iniciou!")