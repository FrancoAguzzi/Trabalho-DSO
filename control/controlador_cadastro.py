from model.usuario import Usuario
from model.seguranca import Seguranca
from view.tela_cadastro import TelaCadastro
from model.cadastro import Cadastro
from model.tipo import TipoPessoa
from exception.exception_cadastro import *


class ControladorCadastro:

    def __init__(self):
        self.__cadastro = Cadastro()
        self.__telaCadastro = TelaCadastro()

    @property
    def cadastro(self):
        return self.__cadastro

    def inclui_usuario(self, respostas=None):
        try:
            if respostas is None:
                respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.USUARIO)
            usuario = Usuario(respostas["nome"], respostas["telefone"], respostas["matricula"])
            for user in self.__cadastro.usuarios:
                if usuario.matricula == user.matricula:
                    raise UsuarioDuplicadoException
            self.__cadastro.usuarios.append(usuario)
            return usuario
        except:
            print("Adicionar aqui uma except")

    def exclui_usuario(self):
        try:
            respostas = self.__telaCadastro.excluir()
            for usuario in self.__cadastro.usuarios:
                if usuario.matricula == respostas["id"]:
                    self.__cadastro.usuarios.remove(usuario)
                    return usuario
            print MatriculaInvalidaException
        except:
            print("Adicionar aqui uma except")

    def atualiza_usuario(self):
        atualizado = False
        try:
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
        except:
            print("Adicionar aqui uma except")

    def lista_usuarios(self):
        self.__telaCadastro.lista_pessoas(self.__cadastro.usuarios)

    def inclui_seguranca(self, respostas=None):
        try:
            if respostas is None:
                respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.SEGURANCA)
            seguranca = Seguranca(respostas["nome"], respostas["telefone"],
                                  respostas["senha_especial"], respostas["codigo"])
            for seg in self.__cadastro.segurancas:
                if seguranca.codigo == seg.codigo:
                    raise SegurancaDuplicadoException
            self.__cadastro.segurancas.append(seguranca)
            return seguranca
        except:
            print("Adicionar aqui uma except")

    def exclui_seguranca(self):
        try:
            respostas = self.__telaCadastro.excluir()
            for seguranca in self.__cadastro.segurancas:
                if seguranca.codigo == int(respostas["id"]):
                    self.__cadastro.segurancas.remove(seguranca)
                    return
            print CodigoInvalidoException
        except:
            print("Adicionar aqui uma except")

    def atualiza_seguranca(self):
        atualizado = False
        try:
            respostas = self.__telaCadastro.cadastro(tipo=TipoPessoa.SEGURANCA, novo = False)
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
        except:
            print("Adicionar aqui uma except")

    def lista_segurancas(self):
        self.__telaCadastro.lista_pessoas(self.__cadastro.segurancas)