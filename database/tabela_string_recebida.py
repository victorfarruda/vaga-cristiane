from database.conn import BaseString
from database.query import (
    SQL_CREATE_TABLE_STRING_RECEBIDA,
    SQL_INSERT_STRING_RECEBIDA,
    SQL_SELECT_ALL_STRING_RECEBIDA,
)


class StringRecebida(BaseString):
    SQL_CREATE = SQL_CREATE_TABLE_STRING_RECEBIDA
    SQL_INSERT = SQL_INSERT_STRING_RECEBIDA
    SQL_SELECT_ALL = SQL_SELECT_ALL_STRING_RECEBIDA


if __name__ == '__main__':
    s = StringRecebida()
    s.insert_into_string_recebida('nome;endereco;telefone;teste')
    s.select_all()
