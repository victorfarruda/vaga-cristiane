from database.conn import BaseString
from database.query import (
    SQL_CREATE_TABLE_COMANDO_PENDENTE,
    SQL_INSERT_COMANDO_PENDENTE,
    SQL_SELECT_ALL_COMANDO_PENDENTE,
)


class ComandoPendente(BaseString):
    SQL_CREATE = SQL_CREATE_TABLE_COMANDO_PENDENTE
    SQL_INSERT = SQL_INSERT_COMANDO_PENDENTE
    SQL_SELECT_ALL = SQL_SELECT_ALL_COMANDO_PENDENTE


if __name__ == '__main__':
    s = ComandoPendente()
    s.insert_into('teste1;teste2;teste3;teste4')
    s.select_all()
