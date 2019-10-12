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

    def retuornar(self):
        print("retornando...")

    def menu_cadastro(self):
        switcher = {
            0: self.retuornar,
            1: self.__controladorCadastro.inclui_usuario,
            2: self.__controladorCadastro.lista_usuarios,
            3: self.__controladorCadastro.atualiza_usuario,
            4: self.__controladorCadastro.inclui_seguranca,
            5: self.__controladorCadastro.lista_segurancas,
            6: self.__controladorCadastro.atualiza_seguranca
        }
        opcao = -1
        while int(opcao) != 0:
            opcao = self.__telaSistema.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Lista de opções:"
                            "\n0 -> retornar"
                            "\n1 -> incluir usuário\n2 -> listar usuários\n3 -> atualizar usuário"
                            "\n4 -> incluir segurança\n5 -> listar seguranças\n6 -> atualizar segurança"
            })
            self.__telaSistema.limpar_tela()
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except KeyError:
                print("Opção inválida!")

    def inicia(self):
        print("Iniciando...")
        print("Criando usuários e seguranças padrão...")
        self.__controladorCadastro.inclui_usuario({"nome": "Fulano", "telefone": 123123, "matricula": "123"})
        self.__controladorCadastro.inclui_seguranca({"nome": "Zé", "telefone": 321321, "codigo": 1, "senha_especial": "senha"})
        print("Usuários e Seguranças criados!")
        print("Iniciou!")
        switcher = {
            0: self.finalizar,
            1: self.menu_cadastro
        }

        while True:
            opcao = self.__telaSistema.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Lista de opções:"
                            "\n0 -> sair"
                            "\n1 -> menu cadastro"
            })
            self.__telaSistema.limpar_tela()
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except KeyError:
                print("Opção inválida")
