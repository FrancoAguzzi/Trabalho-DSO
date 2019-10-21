from model.movimentacao import Movimentacao
from view.tela_movimentacao import TelaMovimentacao
from model.registro import Registro
from datetime import *
from model.tipo import TipoRegistro
from exception.exception_movimentacao import *
from exception.exception_cadastro import *
from exception.exception_sistema import *


class ControladorMovimentacao:

    def __init__(self, controlador_cadastro):
        self.__movimentacao = Movimentacao(vagas=10)
        self.__controladorCadastro = controlador_cadastro
        self.__telaMovimentacao = TelaMovimentacao()

    @property
    def movimentacao(self):
        return self.__movimentacao

    @property
    def registros(self):
        return self.__movimentacao.registros

    def acesso(self):
        opcao = self.__telaMovimentacao.mostra_informacao({
            "input": "Selecione a opção: ",
            "mensagem": "Acesso de:"
                        "\n1 -> Usuário"
                        "\n2 -> Segurança"
        })

        if opcao == "1":
            usuarios = self.__controladorCadastro.cadastro.usuarios
            respostas = self.__telaMovimentacao.acesso_pessoa()
            for usuario in usuarios:
                if usuario.matricula == respostas["matricula"]:
                    for registro in reversed(self.__movimentacao.registros):
                        if registro.matricula == respostas["matricula"]:
                            if registro.tipo == TipoRegistro.ENTRADA:
                                self.__movimentacao.vagas += 1
                                self.__movimentacao.registros.append(
                                    Registro(timestamp=datetime.now(),
                                             tipo=TipoRegistro.SAIDA,
                                             matricula=respostas["matricula"]
                                             ))
                                print("Retire sua bicicleta")
                            else:
                                if self.__movimentacao.vagas > 0:
                                    self.__movimentacao.vagas -= 1
                                    self.__movimentacao.registros.append(
                                        Registro(timestamp=datetime.now(),
                                                 tipo=TipoRegistro.ENTRADA,
                                                 matricula=respostas["matricula"]
                                                 ))
                                    print("Coloque sua bicicleta em um local disponível")
                                else:
                                    raise BicicletarioLotadoException
                            print("Acesso Liberado " + usuario.nome)
                            return
                    if self.__movimentacao.vagas > 0:
                        self.__movimentacao.vagas -= 1
                        self.__movimentacao.registros.append(
                            Registro(timestamp=datetime.now(),
                                     tipo=TipoRegistro.ENTRADA,
                                     matricula=respostas["matricula"]
                                     ))
                        print("Coloque sua bicicleta em um local disponível")
                        print("Acesso Liberado " + usuario.nome)
                        return
                    else:
                        raise BicicletarioLotadoException
            raise MatriculaInvalidaException
        elif opcao == "2":
            segurancas = self.__controladorCadastro.cadastro.segurancas
            respostas = self.__telaMovimentacao.acesso_pessoa(tipo="segurança")
            for seguranca in segurancas:
                if seguranca.codigo == int(respostas["codigo"]) and seguranca.senha_especial == respostas["senha_especial"]:
                    self.__movimentacao.registros.append(
                        Registro(timestamp=datetime.now(),
                                 tipo=TipoRegistro.ESPECIAL,
                                 codigo=respostas["codigo"]
                                 ))
                    print("Acesso Liberado " + seguranca.nome)
                else:
                    raise CodigoSenhaInvalidoException
        else:
            raise OpcaoInvalidaException

    def atualiza_acesso(self):
        opcao = self.__telaMovimentacao.mostra_informacao({
            "input": "Selecione a opção: ",
            "mensagem": "Tipo de acesso:"
                        "\n1 -> Entrada"
                        "\n2 -> Saída"
        })
        if int(opcao) > 2 or int(opcao) < 1:
            raise OpcaoInvalidaException

        id_pessoa = self.__telaMovimentacao.mostra_informacao({
            "input": "Digite a matricula: ",
            "mensagem": "Alterar o acesso de:"
        })

        for registro in self.__movimentacao.registros:
            if registro.tipo == TipoRegistro(int(opcao)):
                if registro.matricula == id_pessoa:
                    if registro.tipo == TipoRegistro.ENTRADA:
                        registro.tipo = TipoRegistro.SAIDA
                        self.__movimentacao.vagas += 1
                    elif registro.tipo == TipoRegistro.SAIDA:
                        if self.movimentacao.vagas > 0:
                            registro.tipo = TipoRegistro.ENTRADA
                            self.__movimentacao.vagas -= 1
                        else:
                            raise BicicletarioLotadoException
                    print("Registro alterado com sucesso!")
                    return
        raise MatriculaInvalidaException


    def exclui_acesso(self):
        opcao = self.__telaMovimentacao.mostra_informacao({
            "input": "Selecione a opção: ",
            "mensagem": "Tipo de acesso:"
                        "\n1 -> Entrada"
                        "\n2 -> Saída"
                        "\n3 -> Especial"
        })
        if int(opcao) > 3 or int(opcao) < 1:
            raise OpcaoInvalidaException

        id_pessoa = self.__telaMovimentacao.mostra_informacao({
            "input": "Digite o identificador: ",
            "mensagem": "Remover o acesso de:"
        })

        for registro in self.__movimentacao.registros:
            if registro.tipo == TipoRegistro(int(opcao)):
                if registro.matricula == id_pessoa or registro.codigo == int(id_pessoa):
                    self.__movimentacao.registros.remove(registro)
                    if registro.tipo == TipoRegistro.ENTRADA:
                        self.__movimentacao.vagas += 1
                    if registro.tipo == TipoRegistro.SAIDA:
                        if self.movimentacao.vagas > 0:
                            self.__movimentacao.vagas -= 1
                        else:
                            raise BicicletarioLotadoException
                    print("Registro removido com sucesso!")
                    return
        if opcao == "3":
            raise CodigoInvalidoException
        else:
            raise MatriculaInvalidaException
