from database.conn import BaseString
from database.query import (
    SQL_CREATE_TABLE_TRATAMENTO_STRING_RECEBIDA,
    SQL_INSERT_TRATAMENTO_STRING_RECEBIDA,
    SQL_SELECT_ALL_TRATAMENTO_STRING_RECEBIDA,
)


class TratamentoStringRecebida(BaseString):
    SQL_CREATE = SQL_CREATE_TABLE_TRATAMENTO_STRING_RECEBIDA
    SQL_INSERT = SQL_INSERT_TRATAMENTO_STRING_RECEBIDA
    SQL_SELECT_ALL = SQL_SELECT_ALL_TRATAMENTO_STRING_RECEBIDA

    def insert_into_string_recebida(self, values):
        campo1, campo2, campo3, campo4 = values.split(';')
        return self.conn.execute_and_commit(SQL_INSERT_TRATAMENTO_STRING_RECEBIDA, (campo1, campo2, campo3, campo4))


if __name__ == '__main__':
    s = TratamentoStringRecebida()
    _id = s.insert_into_string_recebida('nome;endereco;telefone;teste')
    print(_id)
    s.select_all()
