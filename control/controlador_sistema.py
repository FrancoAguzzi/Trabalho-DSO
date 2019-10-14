from control.controlador_cadastro import ControladorCadastro
from control.controlador_movimentacao import ControladorMovimentacao
from view.tela_sistema import TelaSistema
from model.tipo import TipoPessoa, TipoRegistro
from model.registro import Registro
from datetime import *

class ControladorSistema:

    def __init__(self):
        self.__controladorCadastro = ControladorCadastro()
        self.__controladorMovimentacao = ControladorMovimentacao(self.__controladorCadastro)
        self.__telaSistema = TelaSistema()

    def aplica_filtro(self, filtro, registros):
        if filtro["chave"] == "identificador":
            return filter(lambda r: r.codigo == filtro["valor"] if r.codigo is not None else r.matricula == filtro["valor"], registros)
        if filtro["chave"] == "tipo_pessoa":
            return filter(lambda r:
                          r.matricula is not None if filtro["valor"] == TipoPessoa.USUARIO else r.codigo is not None,
                          registros)
        if filtro["chave"] == "timestamp":
            return filter(lambda r: r.timestamp.strftime("%d-%m-%Y") == filtro["valor"].strftime("%d-%m-%Y"), registros)

        return filter(lambda r: getattr(r, filtro["chave"]) == filtro["valor"], registros)

    def relatorio(self, filtro=None):
        registros = self.__controladorMovimentacao.registros
        if filtro is not None:
            registros = self.aplica_filtro(filtro, registros)
        self.__telaSistema.lista_relatorio(registros)

    def finalizar(self):
        exit(0)

    def retornar(self):
        print("retornando...")

    def menu_relatorio(self):
        opcao = self.__telaSistema.mostra_informacao({
            "input": "Selecione a opção: ",
            "mensagem": "Filtrar por:"
                        "\n0 -> Sem filtro"
                        "\n1 -> Identificador"
                        "\n2 -> Tipo pessoa"
                        "\n3 -> Tipo registro"
                        "\n4 -> Data"
        })
        self.__telaSistema.limpar_tela()
        if opcao == "0":
            self.relatorio()
        elif opcao == "1":
            valor = self.__telaSistema.mostra_informacao({
                "input": "Filtro por identificador: ",
                "mensagem": "Digite o identificador: "
            })
            self.relatorio({"chave": "identificador", "valor": valor})
        elif opcao == "2":
            valor = self.__telaSistema.mostra_informacao({
                "input": "Filtro por Tipo de Pessoa: ",
                "mensagem": "Filtrar por: "
                            "\n1 -> Usuário"
                            "\n2 -> Segurança"
            })
            self.relatorio({"chave": "tipo_pessoa", "valor": TipoPessoa(int(valor))})
        elif opcao == "3":
            valor = self.__telaSistema.mostra_informacao({
                "input": "Filtro por Tipo de Registro: ",
                "mensagem": "Filtrar por: "
                            "\n1 -> Entrada"
                            "\n2 -> Saída"
                            "\n3 -> Especial"
            })
            self.relatorio({"chave": "tipo", "valor": TipoRegistro(int(valor))})
        elif opcao == "4":
            valor = self.__telaSistema.mostra_informacao({
                "input": "Filtro por Data do Registro: ",
                "mensagem": "Informe a data no formato d-m-y: "
            })
            timestamp = datetime.strptime(valor, "%d-%m-%Y")
            print(timestamp)
            self.relatorio({"chave": "timestamp", "valor": timestamp})
        else:
            print("Opção inválida, retornando!")

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
        print("Criando registros padrão...")
        self.__controladorMovimentacao.registros.append(
            Registro(
                timestamp=datetime(2019, 9, 5, 11, 30, 5, 0),
                tipo=TipoRegistro.ENTRADA,
                matricula="123"
            ))
        self.__controladorMovimentacao.registros.append(
            Registro(
                timestamp=datetime(2019, 9, 6, 12, 50, 15, 0),
                tipo=TipoRegistro.SAIDA,
                matricula="123"
            ))
        self.__controladorMovimentacao.registros.append(
            Registro(
                timestamp=datetime(2019, 9, 5, 8, 10, 0, 0),
                tipo=TipoRegistro.ESPECIAL,
                codigo=1
            ))
        print("registros criados!")
        print("Iniciou!")
        switcher = {
            0: self.finalizar,
            1: self.menu_cadastro,
            2: self.menu_movimentacao,
            3: self.menu_relatorio
        }

        while True:
            opcao = self.__telaSistema.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Lista de opções:"
                            "\n0 -> sair"
                            "\n1 -> menu cadastro"
                            "\n2 -> menu movimentação"
                            "\n3 -> menu relatório"
            })
            self.__telaSistema.limpar_tela()
            try:
                funcao_escolhida = switcher[int(opcao)]
                funcao_escolhida()
            except (KeyError, ValueError):
                print("Opção inválida")