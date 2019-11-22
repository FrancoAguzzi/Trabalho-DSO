from control.controlador_cadastro import ControladorCadastro
from control.controlador_movimentacao import ControladorMovimentacao
from view.tela_sistema import TelaSistema
from view.select_tipo import SelectTipoPessoa, SelectTipoRegistro
from model.tipo import TipoPessoa, TipoRegistro
from model.registro import Registro
from model.sistema import Sistema
from datetime import *
from exception.exception_cadastro import *
from exception.exception_movimentacao import *
from exception.exception_sistema import *
from view.popups import  Popups
from view.tela_relatorio import TelaRelatorio
from view.tela_filtros import TelaFiltro

class ControladorSistema:

    def __init__(self):
        self.__controladorCadastro = ControladorCadastro()
        self.__controladorMovimentacao = ControladorMovimentacao(self.__controladorCadastro)
        self.__telaSistema = TelaSistema()
        self.__telaRelatorio = TelaRelatorio()
        self.__telaFiltros = TelaFiltro()
        self.__selectTipoPessoa = SelectTipoPessoa()
        self.__selectTipoRegistro = SelectTipoRegistro()
        self.__popups = Popups()
        self.__sistema = Sistema(
            cadastros=self.__controladorCadastro.cadastros(),
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
        registros = self.__controladorMovimentacao.registros
        if filtro is not None:
            registros = self.aplica_filtro(filtro, registros)
        self.__telaFiltros.unhide()
        self.__telaFiltros.components(registros, self.__sistema.cadastros)
        self.__telaFiltros.open()
        self.__telaFiltros.hide()
        self.retornar()

    def finalizar(self):
        exit(0)

    def retornar(self):
        self.inicia()

    def menu_relatorio(self):
        self.__telaRelatorio.unhide()
        button, values = self.__telaRelatorio.open()
        self.__telaRelatorio.hide()

        if button == 'Início':
            self.retornar()
        elif values["option"] == "Sem filtro":
            self.relatorio()
        elif values["option"] == "Identificador":
            text = self.__popups.simple_input("Identificador", "Filtro")
            if text is None:
                self.retornar()
            self.relatorio({"chave": "identificador", "valor": text})
        elif values["option"] == "Tipo pessoa":
            tipo_pessoa = self.__selectTipoPessoa.open()
            self.relatorio({"chave": "tipo_pessoa", "valor": tipo_pessoa})
        elif values["option"] == "Tipo registro":
            tipo_registro = self.__selectTipoRegistro.open()
            self.relatorio({"chave": "tipo", "valor": tipo_registro})
        elif values["option"] == "Data":
            valor = self.__popups.simple_input("Data (d-m-y)", "Filtro")
            timestamp = datetime.strptime(valor, "%d-%m-%Y")
            self.relatorio({"chave": "timestamp", "valor": timestamp})
        else:
            raise OpcaoInvalidaException

    def menu_cadastro(self):
        tipo_pessoa = self.__selectTipoPessoa.open()

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
            self.__popups.error("Erro", "Opção Inválida")
            self.retornar()
