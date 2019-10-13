from model.movimentacao import Movimentacao
from view.tela_movimentacao import TelaMovimentacao
from model.cadastro import Cadastro
from model.registro import Registro
from datetime import *
from model.tipo import TipoRegistro

class ControladorMovimentacao:

    def __init__(self, controlador_cadastro):
        self.__movimentacao = Movimentacao(vagas=1)
        self.__controladorCadastro = controlador_cadastro
        self.__telaMovimentacao = TelaMovimentacao()

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
                                    raise  # Bicicletário Lotado Exception
                            print("Acesso Liberado " + usuario.nome)
                            return
                    if self.__movimentacao.vagas > 0:
                        self.__movimentacao.vagas -= 1
                        self.__movimentacao.registros.append(
                            Registro(timestamp=datetime.now(),
                                     tipo=TipoRegistro.ENTRADA,
                                     matricula=respostas["matricula"]
                                     ))
                        print("Coloque sua bicicleta em um local disponóivel")
                        print("Acesso Liberado " + usuario.nome)
                        return
                    else:
                        raise # Bicicletario Lotado Exception
            raise # Matricula Invalida Exception
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
                    raise #Código e Senha Invalido Exception
        else:
            print("Opção inválida, retornando")

    def exclui_entrada(self, registro):
        pass

    def atualiza_entrada(self, registro):
        pass

    def exclui_saida(self, matricula = None, codigo = None):
        pass

    def atualiza_saida(self, registro):
        pass