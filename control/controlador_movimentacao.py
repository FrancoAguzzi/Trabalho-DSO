from model.movimentacao import Movimentacao
from view.tela_movimentacao import TelaMovimentacao
from model.cadastro import Cadastro
from model.registro import Registro
from datetime import *


class ControladorMovimentacao:

    def __init__(self, entrada = Registro(), saida = Registro()):
        self.__entrada = entrada
        self.__saida = saida

    def acesso(self, matricula, codigo, senha_especial):
        switcher = {
            0: Cadastro.usuarios,
            1: Cadastro.segurancas,
        }
        try:
            opcao = TelaMovimentacao.mostra_informacao({
                "input": "Selecione a opção: ",
                "mensagem": "Acesso de:"
                            "\n0 -> Usuário"
                            "\n1 -> Segurança"
            })
            opcao_escolhida = switcher[int(opcao)]
        except:
            raise #Opção Inválida Exception
        if opcao == 0:
            for usuario in opcao_escolhida:
                if usuario.matricula == matricula:
                    if Movimentacao.vagas > 0:
                        print("Acesso Liberado " + matricula)
                    else:
                        raise #Bicicletário Lotado Exception
                else:
                    raise #Matricula Invalida Exception
        elif opcao == 1:
            for seguranca in opcao_escolhida:
                if seguranca.codigo == codigo and seguranca.senha_especial == senha_especial:
                    print("Acesso Liberado " + codigo)
                else:
                    raise #Código e Senha Invalido Exception

    def inclui_entrada(self, matricula = None, codigo = None):
        if matricula == None and codigo == None:
            raise #Falta Parâmetros Exception
        elif matricula != None and codigo != None:
            raise #Informação Duplicada Exception
        elif matricula != None:
            for usuario in Cadastro.usuarios:
                if usuario.matricula == matricula:
                    entrada_usuario = Registro(datetime.datetime.now(), matricula)
                    Movimentacao.registro_entrada.append(entrada_usuario)
            return entrada_usuario
        elif codigo != None:
            for seguranca in Cadastro.segurancas:
                if seguranca.codigo == codigo:
                    entrada_seguranca = Registro(datetime.datetime.now(), codigo)
                    Movimentacao.registro_entrada.append(entrada_seguranca)
            return entrada_seguranca

    def exclui_entrada(self, registro):
        pass

    def atualiza_entrada(self, registro):
        pass

    def inclui_saida(self, registro):
        pass

    def exclui_saida(self, registro):
        pass

    def atualiza_saida(self, registro):
        pass