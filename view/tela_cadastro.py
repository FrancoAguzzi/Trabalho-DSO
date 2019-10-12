from view.abstract_tela import AbstractTela

class TelaCadastro(AbstractTela):

    def __init__(self):
        pass

    def lista_pessoas(self, pessoas: []):
        print("Listando...")
        for pessoa in pessoas:
            print(pessoa.nome + " - " + str(pessoa.telefone))

    def cadastro(self, tipo: str = "usuario", novo=True):
        respostas = {}
        if novo:
            print("Novo Cadastro...")
        else:
            print("Atualizando Cadastro...")

        if tipo == "usuario":
            respostas["matricula"] = input("Matrícula: ")
        else:
            respostas["codigo"] = input("Código: ")
            respostas["senha_especial"] = input("Senha Especial: ")

        respostas["nome"] = input("Nome: ")
        respostas["telefone"] = input("Telefone: ")

        return respostas

    def mostra_informacao(self, info):
        print(info)
