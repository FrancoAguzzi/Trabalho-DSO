from control.controlador_cadastro import ControladorCadastro
from control.controlador_movimentacao import ControladorMovimentacao
from view.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controladorCadastro = ControladorCadastro()
        self.__controladorMovimentacao = ControladorMovimentacao(self.__controladorCadastro)
        self.__telaSistema = TelaSistema()

    def relatorio(self, filtro):
        pass

    def finalizar(self):
        exit(0)

    def retornar(self):
        print("retornando...")

    def menu_cadastro(self):
        switcher = {
            0: self.retornar,
            1: self.__controladorCadastro.inclui_usuario,
            2: self.__controladorCadastro.lista_usuarios,
            3: self.__controladorCadastro.atualiza_usuario,
            4: self.__controladorCadastro.exclui_usuario,
            5: self.__controladorCadastro.inclui_seguranca,
            6: self.__controladorCadastro.lista_segurancas,
            7: self.__controladorCadastro.atualiza_seguranca,
            8: self.__controladorCadastro.exclui_seguranca
        }
        opcao = -1
        while int(opcao) != 0:
            opcao = self.__telaSistema.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Lista de opções:"
                            "\n0 -> retornar"
                            "\n1 -> incluir usuário\n2 -> listar usuários\n3 -> atualizar usuário\n4 -> excluir usuário"
                            "\n5 -> incluir segurança\n6 -> listar seguranças\n7 -> atualizar segurança\n8 -> excluir segurança"
            })
            self.__telaSistema.limpar_tela()
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except (KeyError, ValueError):
                print("Opção inválida!")

    def menu_movimentacao(self):
        switcher = {
            0: self.retornar,
            1: self.__controladorMovimentacao.acesso,
            2: self.__controladorMovimentacao.atualiza_entrada,
            3: self.__controladorMovimentacao.atualiza_saida,
            4: self.__controladorMovimentacao.exclui_entrada,
            5: self.__controladorMovimentacao.exclui_saida,
        }
        opcao = -1
        while int(opcao) != 0:
            opcao = self.__telaSistema.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Lista de opções:"
                            "\n0 -> retornar\n1 -> acessar"
                            "\n2 -> atualizar entrada\n3 -> atualizar saída"
                            "\n4 -> excluir entrada\n5 -> excluir saída"
            })
            self.__telaSistema.limpar_tela()
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except (KeyError, ValueError):
                print("Opção inválida!")

    def inicia(self):
        print("Iniciando...")
        print("Criando usuários e seguranças padrão...")
        self.__controladorCadastro.inclui_usuario({"nome": "Fulano", "telefone": 12312300, "matricula": "123"})
        self.__controladorCadastro.inclui_seguranca({"nome": "Zé", "telefone": 32132100, "codigo": 1, "senha_especial": "senha"})
        print("Usuários e Seguranças criados!")
        print("Iniciou!")
        switcher = {
            0: self.finalizar,
            1: self.menu_cadastro,
            2: self.menu_movimentacao
        }

        while True:
            opcao = self.__telaSistema.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Lista de opções:"
                            "\n0 -> sair"
                            "\n1 -> menu cadastro"
                            "\n2 -> menu movimentação"
            })
            self.__telaSistema.limpar_tela()
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except (KeyError, ValueError):
                print("Opção inválida")