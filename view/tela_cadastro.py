from view.abstract_tela import AbstractTela

class TelaCadastro(AbstractTela):

    def __init__(self):
        pass

    def lista_pessoas(self, pessoas: []):
        print("Listando...")
        for pessoa in pessoas:
            print(pessoa.nome + " - " + str(pessoa.telefone))

    def novo_cadastro(self, tipo: str = "usuario"):
        respostas = {}
        print("Novo Cadastro...")
        respostas["nome"] = input("Nome: ")
        respostas["telefone"] = input("Telefone: ")
        if tipo == "usuario":
            respostas["matricula"] = input("Matrícula: ")
        else:
            respostas["codigo"] = input("Código: ")
            respostas["senha_especial"] = input("Senha Especial: ")
        return respostas

    def mostra_informacao(self, info):
        print(info)
