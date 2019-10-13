from model.usuario import Usuario
from model.seguranca import Seguranca
from view.tela_cadastro import TelaCadastro
from model.cadastro import Cadastro


class ControladorCadastro:

    def __init__(self):
        self.__cadastro = Cadastro()
        self.__telaCadastro = TelaCadastro()

    def inclui_usuario(self, respostas = None):
        try:
            if respostas is None:
                respostas = self.__telaCadastro.cadastro()
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

    def atualiza_usuario(self):
        atualizado = False
        try:
            respostas = self.__telaCadastro.cadastro(novo = False)
            for usuario in self.__cadastro.usuarios:
                if usuario.matricula == respostas["matricula"]:
                    atualizado = True
                    if respostas["nome"]:
                        usuario.nome = respostas["nome"]
                    if respostas["telefone"]:
                        usuario.telefone = respostas["telefone"]
            if not atualizado:
                print("criar uma except padrao e extender dela conforme exemplo do professor")
                #raise Exception("")
        except:
            print("Adicionar aqui uma except")

    def lista_usuarios(self):
        self.__telaCadastro.lista_pessoas(self.__cadastro.usuarios)

    def inclui_seguranca(self, respostas=None):
        try:
            if respostas is None:
                respostas = self.__telaCadastro.cadastro(tipo = "seguranca")
            seguranca = Seguranca(respostas["nome"], respostas["telefone"],
                                  respostas["senha_especial"], respostas["codigo"])
            self.__cadastro.segurancas.append(seguranca)
            return seguranca
        except:
            print("Adicionar aqui uma except")

    def exclui_seguranca(self, codigo):
        try:
            for seguranca in self.__cadastro.segurancas:
                if seguranca.codigo == codigo:
                    self.__cadastro.segurancas.remove(seguranca)
        except:
            print("Adicionar aqui uma except")

    def atualiza_seguranca(self):
        atualizado = False
        try:
            respostas = self.__telaCadastro.cadastro(tipo = "seguranca", novo = False)
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
                print("criar uma except padrao e extender dela conforme exemplo do professor")
                # raise Exception("")
        except:
            print("Adicionar aqui uma except")

    def lista_segurancas(self):
        self.__telaCadastro.lista_pessoas(self.__cadastro.segurancas)