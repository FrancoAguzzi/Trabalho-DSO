from abstract_tela import AbstractTela
from model.cadastro import Cadastro

class TelaCadastro(AbstractTela):

    def __init__(self):
        pass

    def lista_usuario(self):
        print(Cadastro.usuarios())

    def lista_seguranca(self):
        print(Cadastro.segurancas())

    def novo_cadastro(self):
        respostas = {}
        respostas.nome = input("Nome: ")
        respostas.telefone = input("Telefone: ")
        respostas.matricula = input("Matrícula: ")
        return respostas

    def mostra_informacao(self, info):
        print(info)
