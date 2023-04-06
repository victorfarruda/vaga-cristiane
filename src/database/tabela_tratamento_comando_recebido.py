from database.conn import Base
from database.query import (
    SQL_CREATE_TABLE_TRATAMENTO_COMANDO_RECEBIDO,
    SQL_INSERT_TRATAMENTO_COMANDO_RECEBIDO,
    SQL_SELECT_ALL_TRATAMENTO_COMANDO_RECEBIDO,
)


class TratamentoComandoRecebido(Base):
    SQL_CREATE = SQL_CREATE_TABLE_TRATAMENTO_COMANDO_RECEBIDO
    SQL_INSERT = SQL_INSERT_TRATAMENTO_COMANDO_RECEBIDO
    SQL_SELECT_ALL = SQL_SELECT_ALL_TRATAMENTO_COMANDO_RECEBIDO

    def insert_into(self, values):
        campo1, campo2, campo3, campo4 = values.split(';')
        return self.conn.execute_and_commit(SQL_INSERT_TRATAMENTO_COMANDO_RECEBIDO, (campo1, campo2, campo3, campo4))


if __name__ == '__main__':
    s = TratamentoComandoRecebido()
    _id = s.insert_into('nome;endereco;telefone;teste')
    print(_id)
    s.select_all()
