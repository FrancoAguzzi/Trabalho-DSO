from control.controlador_cadastro import ControladorCadastro
from control.controlador_movimentacao import ControladorMovimentacao
from view.tela_sistema import TelaSistema
from view.select_tipo import SelectTipo
from model.tipo import TipoPessoa, TipoRegistro
from model.registro import Registro
from model.sistema import Sistema
from datetime import *
from exception.exception_cadastro import *
from exception.exception_movimentacao import *
from exception.exception_sistema import *
from view.popups import  Popups

class ControladorSistema:

    def __init__(self):
        self.__controladorCadastro = ControladorCadastro()
        self.__controladorMovimentacao = ControladorMovimentacao(self.__controladorCadastro)
        self.__telaSistema = TelaSistema()
        self.__selectTipo = SelectTipo()
        self.__sistema = Sistema(
            cadastro=self.__controladorCadastro.cadastro,
            movimentacao=self.__controladorMovimentacao.movimentacao
        )

    def aplica_filtro(self, filtro, registros):
        if filtro["chave"] == "identificador":
            return filter(lambda r:
                          r.codigo == filtro["valor"] if r.codigo is not None else r.matricula == filtro["valor"],
                          registros)
        if filtro["chave"] == "tipo_pessoa":
            return filter(lambda r:
                          r.matricula is not None if filtro["valor"] == TipoPessoa.USUARIO else r.codigo is not None,
                          registros)
        if filtro["chave"] == "timestamp":
            return filter(lambda r: r.timestamp.strftime("%d-%m-%Y") == filtro["valor"].strftime("%d-%m-%Y"), registros)
        return filter(lambda r: getattr(r, filtro["chave"]) == filtro["valor"], registros)

    def relatorio(self, filtro=None):
        registros = self.__sistema.movimentacao.registros
        if filtro is not None:
            registros = self.aplica_filtro(filtro, registros)
        self.__telaSistema.lista_relatorio(registros, self.__sistema.cadastro)

    def finalizar(self):
        exit(0)

    def retornar(self):
        self.inicia()

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
            raise OpcaoInvalidaException + '\n' + self.__telaSistema.retorna()

    def menu_cadastro(self):
        tipo_pessoa = self.__selectTipo.open()

        button, values = self.__controladorCadastro.menu(tipo_pessoa)

        switcher = {TipoPessoa.USUARIO: {
            'Início': self.retornar,
            'Novo': self.__controladorCadastro.inclui_usuario,
            'Editar': self.__controladorCadastro.atualiza_usuario,
            'Excluir': self.__controladorCadastro.exclui_usuario,
        }, TipoPessoa.SEGURANCA: {
            'Início': self.retornar,
            'Novo': self.__controladorCadastro.inclui_seguranca,
            'Editar': self.__controladorCadastro.atualiza_seguranca,
            'Excluir': self.__controladorCadastro.exclui_seguranca
        }}
        try:
            funcao_escolhida = switcher[tipo_pessoa][button]
            funcao_escolhida()
            self.menu_cadastro()
        except (KeyError, ValueError, OpcaoInvalidaException):
            raise OpcaoInvalidaException
        except MatriculaInvalidaException:
            raise MatriculaInvalidaException
        except UsuarioDuplicadoException:
            raise UsuarioDuplicadoException
        except CodigoInvalidoException:
            raise CodigoInvalidoException
        except SegurancaDuplicadoException:
            raise SegurancaDuplicadoException

    def menu_movimentacao(self):
        button, values = self.__controladorMovimentacao.menu()
        switcher = {
            'Início': self.retornar,
            'Acessar': self.__controladorMovimentacao.acesso,
            'Atualiza': self.__controladorMovimentacao.atualiza_acesso,
            'Exclui': self.__controladorMovimentacao.exclui_acesso,
        }
        try:
            funcao_escolhida = switcher[button]
            funcao_escolhida()
            self.menu_movimentacao()
        except (KeyError, ValueError, OpcaoInvalidaException):
            raise OpcaoInvalidaException
        except CodigoSenhaInvalidoException:
            raise CodigoSenhaInvalidoException
        except MatriculaInvalidaException:
            raise MatriculaInvalidaException
        except BicicletarioLotadoException:
            raise BicicletarioLotadoException

    def inicia(self):
        self.__telaSistema.unhide()
        button, values = self.__telaSistema.open()
        self.__telaSistema.hide()
        print(button)
        switcher = {
            'Sair': self.finalizar,
            'Cadastro': self.menu_cadastro,
            'Movimentação': self.menu_movimentacao,
            'Relatório': self.menu_relatorio
        }
        try:
            funcao_escolhida = switcher[button]
            funcao_escolhida()
        except (KeyError, ValueError, OpcaoInvalidaException):
                raise OpcaoInvalidaException
