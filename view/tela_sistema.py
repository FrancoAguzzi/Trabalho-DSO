from view.abstract_tela import AbstractTela
from model.tipo import TipoPessoa

class TelaSistema(AbstractTela):

    def __init__(self):
        pass

    def lista_relatorio(self, registros):
        print("Timestamp\t-\tIdentificador\t-\tPessoa\t-\tTipo")
        for registro in registros:
            identificador = registro.matricula if registro.matricula is not None else str(registro.codigo)
            tipo_pessoa = TipoPessoa.USUARIO if registro.matricula is not None else TipoPessoa.SEGURANCA
            print(
                registro.timestamp.strftime("%d-%m-%Y %H:%M:%S")
                + "\t-\t"
                + identificador
                + "\t-\t"
                + tipo_pessoa.name
                + "\t-\t"
                + registro.tipo.name
            )

    def mostra_informacao(self, info):
        print(info["mensagem"])
        return input(info["input"])
