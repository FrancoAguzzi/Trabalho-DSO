from model.movimentacao import Movimentacao
from view.tela_movimentacao import TelaMovimentacao
from model.registro import Registro
from datetime import *
from model.tipo import TipoRegistro
from exception.exception_movimentacao import *
from exception.exception_cadastro import *
from exception.exception_sistema import *
from view.tela_acesso import TelaAcesso
from view.select_tipo import SelectTipoPessoa
from model.tipo import TipoPessoa
from control.controlador_cadastro import ControladorCadastro
from view.popups import Popups
from persistencia.registroDAO import RegistroDAO


class ControladorMovimentacao:

    def __init__(self, controlador_cadastro: ControladorCadastro):
        self.__movimentacao = Movimentacao(vagas=10)
        self.__controladorCadastro = controlador_cadastro
        self.__telaMovimentacao = TelaMovimentacao()
        self.__telaAcesso = TelaAcesso()
        self.__selectTipoPessoa = SelectTipoPessoa()
        self.__popups = Popups()
        self.__registros_dao = RegistroDAO()

    @property
    def movimentacao(self):
        return self.__movimentacao

    @property
    def registros(self):
        return self.__registros_dao.get_all()

    def controle_console(self, senha=False):
        self.__telaAcesso.components(senha)
        self.__telaAcesso.unhide()
        keys_entered = ''
        while True:
            button, values = self.__telaAcesso.open()
            if button == 'Ir':
                identificador = values['input']
                break
            if button == 'Limpar':
                print('Limpar')
                keys_entered = ''
            elif button in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                print('Button In')
                keys_entered = values['input']
                keys_entered += button
            self.__telaAcesso.window.FindElement('input').Update(keys_entered)
        self.__telaAcesso.hide()
        return identificador

    def acesso(self):
        tipo_pessoa = self.__selectTipoPessoa.open()

        identificador = self.controle_console()

        if tipo_pessoa == TipoPessoa.USUARIO:
            usuarios = self.__controladorCadastro.get_usuarios()
            for usuario in usuarios:
                if usuario.matricula == identificador:
                    for registro in reversed(self.__registros_dao.get_all()):
                        if registro.matricula == identificador:
                            if registro.tipo == TipoRegistro.ENTRADA:
                                self.__movimentacao.vagas += 1
                                self.__registros_dao.add(
                                    Registro(timestamp=datetime.now(),
                                             tipo=TipoRegistro.SAIDA,
                                             matricula=identificador
                                             ))
                                self.__popups.default(title="Sucesso", message="Retire sua bicicleta")
                            else:
                                if self.__movimentacao.vagas > 0:
                                    self.__movimentacao.vagas -= 1
                                    self.__registros_dao.add(
                                        Registro(timestamp=datetime.now(),
                                                 tipo=TipoRegistro.ENTRADA,
                                                 matricula=identificador
                                                 ))
                                    self.__popups.default(title="Sucesso", message="Coloque sua bicicleta em um local disponível")
                                else:
                                    raise BicicletarioLotadoException
                            self.__popups.default(title="Acesso Liberado", message=usuario.nome)
                            return
                    if self.__movimentacao.vagas > 0:
                        self.__movimentacao.vagas -= 1
                        self.__registros_dao.add(
                            Registro(timestamp=datetime.now(),
                                     tipo=TipoRegistro.ENTRADA,
                                     matricula=identificador
                                     ))
                        self.__popups.default(title="Sucesso", message="Coloque sua bicicleta em um local disponível")
                        self.__popups.default(title="Acesso Liberado", message=usuario.nome)
                        return
                    else:
                        raise BicicletarioLotadoException
            raise MatriculaInvalidaException
        elif tipo_pessoa == TipoPessoa.SEGURANCA:
            segurancas = self.__controladorCadastro.get_segurancas()
            senha = self.controle_console(senha=True)
            for seguranca in segurancas:
                if seguranca.codigo == int(identificador) and seguranca.senha_especial == senha:
                    self.__registros_dao.add(
                        Registro(timestamp=datetime.now(),
                                 tipo=TipoRegistro.ESPECIAL,
                                 codigo=identificador
                                 ))
                    self.__popups.default(title="Acesso Liberado", message=seguranca.nome)
                else:
                    raise CodigoSenhaInvalidoException
        else:
            raise OpcaoInvalidaException

    def atualiza_acesso(self):
        opcao = self.__telaMovimentacao.mostra_informacao({
            "input": "Selecione a opção: ",
            "mensagem": "Tipo de acesso:"
                        "\n1 -> Entrada"
                        "\n2 -> Saída"
        })
        if int(opcao) > 2 or int(opcao) < 1:
            raise OpcaoInvalidaException

        id_pessoa = self.__telaMovimentacao.mostra_informacao({
            "input": "Digite a matricula: ",
            "mensagem": "Alterar o acesso de:"
        })

        for registro in self.__registros_dao.get_all():
            if registro.tipo == TipoRegistro(int(opcao)):
                if registro.matricula == id_pessoa:
                    if registro.tipo == TipoRegistro.ENTRADA:
                        registro.tipo = TipoRegistro.SAIDA
                        self.__movimentacao.vagas += 1
                    elif registro.tipo == TipoRegistro.SAIDA:
                        if self.movimentacao.vagas > 0:
                            registro.tipo = TipoRegistro.ENTRADA
                            self.__movimentacao.vagas -= 1
                        else:
                            raise BicicletarioLotadoException
                    self.__telaMovimentacao.modifica_registro()
        raise MatriculaInvalidaException


    def exclui_acesso(self):
        opcao = self.__telaMovimentacao.mostra_informacao({
            "input": "Selecione a opção: ",
            "mensagem": "Tipo de acesso:"
                        "\n1 -> Entrada"
                        "\n2 -> Saída"
                        "\n3 -> Especial"
        })
        if int(opcao) > 3 or int(opcao) < 1:
            raise OpcaoInvalidaException

        id_pessoa = self.__telaMovimentacao.mostra_informacao({
            "input": "Digite o identificador: ",
            "mensagem": "Remover o acesso de:"
        })

        for registro in self.__registros_dao.get_all():
            if registro.tipo == TipoRegistro(int(opcao)):
                if registro.matricula == id_pessoa or registro.codigo == int(id_pessoa):
                    self.__registros_dao.remove(registro)
                    if registro.tipo == TipoRegistro.ENTRADA:
                        self.__movimentacao.vagas += 1
                    if registro.tipo == TipoRegistro.SAIDA:
                        if self.movimentacao.vagas > 0:
                            self.__movimentacao.vagas -= 1
                        else:
                            raise BicicletarioLotadoException
                    self.__telaMovimentacao.modifica_registro(True)
        if opcao == "3":
            raise CodigoInvalidoException
        else:
            raise MatriculaInvalidaException

    def menu(self):
        self.__telaMovimentacao.unhide()
        button, values = self.__telaMovimentacao.open()
        self.__telaMovimentacao.hide()
        return button, values
