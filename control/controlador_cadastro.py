from model.usuario import Usuario
from model.seguranca import Seguranca
from view.tela_cadastro import TelaCadastro
from model.cadastro import Cadastro
from model.tipo import TipoPessoa
from exception.exception_cadastro import *
from persistencia.usuarioDAO import UsuarioDAO

class ControladorCadastro:

    def __init__(self):
        self.__cadastro = Cadastro()
        self.__telaCadastro = TelaCadastro()
        self.__usuario_dao = UsuarioDAO()

    @property
    def cadastro(self):
        return self.__cadastro

    def inclui_usuario(self, respostas=None):
        if respostas is None:
            respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.USUARIO)
        usuario = Usuario(respostas["nome"], respostas["telefone"], respostas["matricula"])
        for user in self.__cadastro.usuarios:
            if usuario.matricula == user.matricula:
                raise UsuarioDuplicadoException
        self.__usuario_dao.add(usuario)
        return usuario

    def exclui_usuario(self):
        respostas = self.__telaCadastro.excluir()
        for usuario in self.__cadastro.usuarios:
            if usuario.matricula == respostas["id"]:
                # Faltou validação se o usuário não está em um registro
                self.__cadastro.usuarios.remove(usuario)
                return usuario
        raise MatriculaInvalidaException

    def atualiza_usuario(self):
        atualizado = False
        respostas = self.__telaCadastro.cadastro(novo=False, tipo=TipoPessoa.USUARIO)
        for usuario in self.__cadastro.usuarios:
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
        for seg in self.__cadastro.segurancas:
            if seguranca.codigo == seg.codigo:
                raise SegurancaDuplicadoException
        self.__cadastro.segurancas.append(seguranca)
        return seguranca

    def exclui_seguranca(self):
        respostas = self.__telaCadastro.excluir()
        for seguranca in self.__cadastro.segurancas:
            if seguranca.codigo == int(respostas["id"]):
                # Faltou validação se o segurança não está em um registro
                self.__cadastro.segurancas.remove(seguranca)
                return
        raise CodigoInvalidoException

    def atualiza_seguranca(self):
        atualizado = False
        respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.SEGURANCA, novo=False)
        for seguranca in self.__cadastro.segurancas:
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
        self.__telaCadastro.lista_pessoas(self.__cadastro.segurancas)
