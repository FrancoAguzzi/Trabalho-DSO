from model.usuario import Usuario
from model.seguranca import Seguranca
from view.tela_cadastro import TelaCadastro
from model.cadastro import Cadastro


class ControladorCadastro:

    def __init__(self):
        self.__cadastro = Cadastro()
        self.__telaCadastro = TelaCadastro()

    def inclui_usuario(self, respostas=None):
        try:
            if respostas is None:
                respostas = self.__telaCadastro.novo_cadastro()
            usuario = Usuario(respostas["nome"], respostas["telefone"], respostas["matricula"])
            self.__cadastro.usuarios.append(usuario)
            return usuario
        except:
            print("Adicionar aqui uma except")

    def exclui_usuario(self, matricula):
        try:
            for usuario in self.__cadastro.usuarios:
                if usuario.matricula == matricula:
                    self.__cadastro.usuarios.remove(usuario)
                    return usuario
        except:
            print("Adicionar aqui uma except")

    def atualiza_usuario(self, nome, telefone, matricula):
        pass

    def lista_usuarios(self):
        self.__telaCadastro.lista_pessoas(self.__cadastro.usuarios)

    def inclui_seguranca(self, respostas=None):
        try:
            if respostas is None:
                respostas = self.__telaCadastro.novo_cadastro("seguranca")
            seguranca = Seguranca(respostas["nome"], respostas["telefone"],
                                  respostas["senha_especial"], respostas["codigo"])
            self.__cadastro.segurancas.append(seguranca)
            return seguranca
        except:
            print("Adicionar aqui uma except")

    def exclui_seguranca(self, codigo):
        try:
            for seguranca in self.__cadastro.segurancas:
                print("s " + str(seguranca.codigo))
                if seguranca.codigo == codigo:
                    self.__cadastro.segurancas.remove(seguranca)
        except:
            print("Adicionar aqui uma except")

    def atualiza_seguranca(self, nome, telefone, codigo):
        pass

    def lista_segurancas(self):
        self.__telaCadastro.lista_pessoas(self.__cadastro.segurancas)