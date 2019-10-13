from enum import Enum


class TipoPessoa(Enum):
    SEGURANCA = 1
    USUARIO = 2


class TipoRegistro(Enum):
    ENTRADA = 1
    SAIDA = 2
    ESPECIAL = 3
