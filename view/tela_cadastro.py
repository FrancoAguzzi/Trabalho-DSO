from abstract_tela import AbstractTela
from .. import

class TelaCadastro(AbstractTela):

    def __init__(self):
        pass

    def lista_usuario(self):
        print(Cadastro.usuarios())

    def lista_seguranca(self):
        print(Cadastro.segurancas())

    def novo_cadastro(self):
        print(info)
        respostas = {}
        respostas.nome = input("Nome: ")
        respostas.telefone = input("Telefone: ")
        respostas.matricula = input("Matrícula: ")

    def mostra_informacao(self, info):
        print(info)
