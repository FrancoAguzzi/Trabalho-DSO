from view.abstract_tela import AbstractTela
from getpass import getpass
from model.tipo import TipoPessoa

class TelaCadastro(AbstractTela):

    def __init__(self):
        pass

    def lista_pessoas(self, pessoas: []):
        print("Listando...")
        print("Nome\t-\tTelefone\t-\tId")
        for pessoa in pessoas:
            print(pessoa.nome
                  + "\t-\t"
                  + str(pessoa.telefone)
                  + "\t-\t"
                  + (str(pessoa.codigo) if hasattr(pessoa, "codigo") else pessoa.matricula))

    def cadastro(self, tipo: TipoPessoa, novo=True):
        respostas = {}
        if novo:
            print("Novo Cadastro...")
        else:
            print("Atualizando Cadastro...")

        if tipo == TipoPessoa.USUARIO:
            respostas["matricula"] = input("Matrícula: ")
        else:
            respostas["codigo"] = input("Código: ")
            respostas["senha_especial"] = getpass("Senha Especial: ")

        respostas["nome"] = input("Nome: ")
        respostas["telefone"] = input("Telefone: ")

        return respostas

    def excluir(self):
        respostas = {}
        respostas["id"] = input("Digite o identificador da pessoa a ser excluida (código/matrícula): ")
        return respostas

    def mostra_informacao(self, info):
        print(info)
