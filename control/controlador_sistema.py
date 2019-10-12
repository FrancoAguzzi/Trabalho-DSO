from control.controlador_cadastro import ControladorCadastro
from control.controlador_movimentacao import ControladorMovimentacao
from view.tela_sistema import TelaSistema

class ControladorSistema:

    def __init__(self):
        self.__controladorCadastro = ControladorCadastro()
        self.__telaSistema = TelaSistema()

    def relatorio(self, filtro):
        pass

    def finalizar(self):
        exit(0)

    def inicia(self):
        print("Iniciando...")
        print("Criando usuários e seguranças padrão...")
        self.__controladorCadastro.inclui_usuario({"nome": "Fulano", "telefone": 123123, "matricula": "16207180"})
        self.__controladorCadastro.inclui_seguranca({"nome": "Zé", "telefone": 321321, "codigo": 1, "senha_especial": "senha"})
        print("Usuários e Seguranças criados!")
        self.__controladorCadastro.lista_usuarios()
        self.__controladorCadastro.lista_segurancas()
        print("Iniciou!")
        switcher = {0: self.finalizar,
                    1: self.__controladorCadastro.inclui_usuario,
                    2: self.__controladorCadastro.lista_usuarios}

        while True:
            opcao = self.__telaSistema.mostra_informacao({"input": "Selecione a opção: ", "mensagem": "Lista de opções:\n0 -> sair\n1 -> incluir usuario\n2 -> listar usuarios"})
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except KeyError:
                print("Opção inválida")
