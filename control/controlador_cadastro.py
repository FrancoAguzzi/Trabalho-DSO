from model.usuario import Usuario
from model.seguranca import Seguranca
from view.tela_cadastro import TelaCadastro
from model.cadastro import Cadastro
from model.tipo import TipoPessoa
from exception.exception_cadastro import *
from persistencia.usuarioDAO import UsuarioDAO
from persistencia.segurancaDAO import SegurancaDAO

class ControladorCadastro:

    def __init__(self):
        self.__telaCadastro = TelaCadastro()
        self.__cadastro = Cadastro()
        self.__usuario_dao = UsuarioDAO()
        self.__seguranca_dao = SegurancaDAO()


    ### CONTROLADOR CADASTRO NÃO FAZ MAIS USO DE CADASTRO()
    @property
    def cadastro(self):
        return self.__cadastro

    def inclui_usuario(self, respostas=None):
        if respostas is None:
            respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.USUARIO)
        usuario = Usuario(respostas["nome"], respostas["telefone"], respostas["matricula"])
        for user in self.__usuario_dao.get_all():
            if usuario.matricula == user.matricula:
                raise UsuarioDuplicadoException
        self.__usuario_dao.add(usuario)
        return usuario

    def exclui_usuario(self): #NOT WORKING
        respostas = self.__telaCadastro.excluir()
        for usuario in self.__usuario_dao.get_all():
            if usuario.matricula == respostas["id"]:
                # Faltou validação se o usuário não está em um registro
                self.__usuario_dao.remove(usuario)
                return usuario
        raise MatriculaInvalidaException

    def atualiza_usuario(self):
        atualizado = False
        respostas = self.__telaCadastro.cadastro(novo=False, tipo=TipoPessoa.USUARIO)
        for usuario in self.__usuario_dao.get_all():
            if usuario.matricula == respostas["matricula"]:
                atualizado = True
                if respostas["nome"]:
                    usuario.nome = respostas["nome"]
                if respostas["telefone"]:
                    usuario.telefone = respostas["telefone"]
        if not atualizado:
            raise MatriculaInvalidaException

    def lista_usuarios(self):
        self.__telaCadastro.lista_pessoas(self.__usuario_dao.get_all())

    def inclui_seguranca(self, respostas=None):
        if respostas is None:
            respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.SEGURANCA)
        seguranca = Seguranca(respostas["nome"], respostas["telefone"],
                              respostas["senha_especial"], respostas["codigo"])
        if self.__seguranca_dao.get(respostas["codigo"]):
            raise SegurancaDuplicadoException
        self.__seguranca_dao.add(seguranca)
        return seguranca

    def exclui_seguranca(self): #NOT WORKING
        respostas = self.__telaCadastro.excluir()
        if self.__seguranca_dao.get(int(respostas["id"])):
            print(self.__seguranca_dao.get((respostas["id"])))
            # Faltou validação se o segurança não está em um registro
            self.__seguranca_dao.remove(seguranca)
            return
        raise CodigoInvalidoException

    def atualiza_seguranca(self):
        atualizado = False
        respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.SEGURANCA, novo=False)
        for seguranca in self.__seguranca_dao.get_all():
            if seguranca.codigo == respostas["codigo"]:
                atualizado = True
                if respostas["nome"]:
                    seguranca.nome = respostas["nome"]
                if respostas["telefone"]:
                    seguranca.telefone = respostas["telefone"]
                if respostas["senha_especial"]:
                    seguranca.senha_especial = respostas["senha_especial"]
        if not atualizado:
            raise CodigoInvalidoException

    def lista_segurancas(self):
        self.__telaCadastro.lista_pessoas(self.__seguranca_dao.get_all())

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
