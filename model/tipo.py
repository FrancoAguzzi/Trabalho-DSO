from enum import Enum


class TipoPessoa(Enum):
    USUARIO = 1
    SEGURANCA = 2


class TipoRegistro(Enum):
    ENTRADA = 1
    SAIDA = 2
    ESPECIAL = 3
