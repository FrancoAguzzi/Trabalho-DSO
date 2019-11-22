from model.usuario import Usuario
from model.seguranca import Seguranca
from view.tela_cadastro import TelaCadastro
from view.form_cadastro import FormCadastro
from view.popups import Popups
from model.cadastro import Cadastro
from model.tipo import TipoPessoa
from exception.exception_cadastro import *
from persistencia.usuarioDAO import UsuarioDAO
from persistencia.segurancaDAO import SegurancaDAO

class ControladorCadastro:

    def __init__(self):
        self.__telaCadastro = TelaCadastro()
        self.__formCadastro = FormCadastro()
        self.__cadastro = Cadastro()
        self.__usuario_dao = UsuarioDAO()
        self.__seguranca_dao = SegurancaDAO()
        self.__popups = Popups()

    @property
    def cadastros(self):
        return self.__usuario_dao.get_all(), self.__seguranca_dao.get_all()

    def get_usuarios(self):
        return self.__usuario_dao.get_all()

    def get_segurancas(self):
        return self.__seguranca_dao.get_all()

    def inclui_usuario(self):
        self.__formCadastro.unhide()
        self.__formCadastro.components(tipo=TipoPessoa.USUARIO)
        button, values = self.__formCadastro.open()
        self.__formCadastro.hide()
        usuario = Usuario(values["nome"], values["telefone"], values["matricula"])
        for user in self.__usuario_dao.get_all():
            if usuario.matricula == user.matricula:
                raise UsuarioDuplicadoException
        self.__usuario_dao.add(usuario)
        return usuario

    def exclui_usuario(self):
        text = self.__popups.simple_input("Identificador", "Excluir")

        if text is None:
            return

        button = self.__popups.confirm("Confirmar", "Deseja excluir o usuário com matrícula: " + text)

        if button == "Yes":
            usuario = self.__usuario_dao.get(text)
            if usuario:
                self.__usuario_dao.remove(usuario.matricula)
                return
            raise MatriculaInvalidaException

    def atualiza_usuario(self):
        atualizado = False

        self.__formCadastro.unhide()
        self.__formCadastro.components(tipo=TipoPessoa.USUARIO, novo=False)
        button, values = self.__formCadastro.open()
        self.__formCadastro.hide()

        for usuario in self.__usuario_dao.get_all():
            if usuario.matricula == values["matricula"]:
                atualizado = True
                if values["nome"]:
                    usuario.nome = values["nome"]
                if values["telefone"]:
                    usuario.telefone = values["telefone"]
        if not atualizado:
            raise MatriculaInvalidaException

    def inclui_seguranca(self):
        self.__formCadastro.unhide()
        self.__formCadastro.components(tipo=TipoPessoa.SEGURANCA)
        button, values = self.__formCadastro.open()
        self.__formCadastro.hide()
        seguranca = Seguranca(values["nome"], values["telefone"],
                              values["senha_especial"], values["codigo"])
        if self.__seguranca_dao.get(values["codigo"]):
            raise SegurancaDuplicadoException
        self.__seguranca_dao.add(seguranca)
        return seguranca

    def exclui_seguranca(self):
        text = self.__popups.simple_input("Identificador", "Excluir")
        if text is None:
            return

        button = self.__popups.confirm("Confirmar", "Deseja excluir o usuário com matrícula: " + text)

        if button == "Yes":
            seguranca = self.__seguranca_dao.get(int(text))
            if seguranca:
                self.__seguranca_dao.remove(seguranca.codigo)
                return
            raise CodigoInvalidoException

    def atualiza_seguranca(self):
        atualizado = False

        self.__formCadastro.unhide()
        self.__formCadastro.components(tipo=TipoPessoa.SEGURANCA, novo=False)
        button, values = self.__formCadastro.open()
        self.__formCadastro.hide()

        for seguranca in self.__seguranca_dao.get_all():
            if seguranca.codigo == values["codigo"]:
                atualizado = True
                if values["nome"]:
                    seguranca.nome = values["nome"]
                if values["telefone"]:
                    seguranca.telefone = values["telefone"]
                if values["senha_especial"]:
                    seguranca.senha_especial = values["senha_especial"]
        if not atualizado:
            raise CodigoInvalidoException

    def menu(self, tipo):
        if tipo == TipoPessoa.USUARIO:
            pessoas = self.__usuario_dao.get_all()
        else:
            pessoas = self.__seguranca_dao.get_all()

        self.__telaCadastro.components(tipo=tipo, pessoas=pessoas)
        self.__telaCadastro.unhide()
        button, values = self.__telaCadastro.open()
        self.__telaCadastro.hide()
        return button, values
