from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa


class TelaSistema(AbstractTela):

    def __init__(self):
        super().__init__()

    def lista_relatorio(self, registros, cadastros):
        print("Timestamp\t\t-\tIdent.\t-\tNome\t-\tTipo Pessoa\t-\tTipo")
        for registro in registros:
            tipo_pessoa = TipoPessoa.USUARIO if registro.matricula is not None else TipoPessoa.SEGURANCA
            if tipo_pessoa == tipo_pessoa.USUARIO:
                identificador = registro.matricula
                nome = next(filter(lambda c:
                                   c.matricula == registro.matricula, cadastros.usuarios
                                   ), "Não encontrado").nome
            else:
                identificador = str(registro.codigo)
                nome = next(filter(lambda c:
                                   c.codigo == registro.codigo, cadastros.segurancas
                                   ), "Não encontrado").nome

            print(
                registro.timestamp.strftime("%d-%m-%Y %H:%M:%S")
                + "\t-\t"
                + identificador
                + "\t-\t"
                + nome
                + "\t-\t"
                + tipo_pessoa.name
                + " \t-\t"
                + registro.tipo.name
            )

    def mostra_informacao(self, info):
        print(info["mensagem"])
        return input(info["input"])

    def tela_inicia(self):
        print("Iniciando...")
        print("Criando usuários e seguranças padrão...")
        if len(ControladorCadastro.cadastro.usuarios) >= 1:
            if len(ControladorCadastro.cadastro.segurancas) >= 1:
                print("Usuários e Seguranças criados!")
                print("Criando registros padrão...")
            else:
                break
        else:
            break
        #adicionar validação da existencia dos registros

    def retorna(self):
        print("Retornando...")