from database.conn import Base
from database.query import (
    SQL_CREATE_TABLE_COMANDO_RECEBIDO,
    SQL_INSERT_COMANDO_RECEBIDO,
    SQL_SELECT_ALL_COMANDO_RECEBIDO,
    SQL_SELECT_BY_ID_COMANDO_RECEBIDO,
    SQL_UPDATE_COMANDO_PROCESSADO,
)


class ComandoRecebido(Base):
    SQL_CREATE = SQL_CREATE_TABLE_COMANDO_RECEBIDO
    SQL_INSERT = SQL_INSERT_COMANDO_RECEBIDO
    SQL_SELECT_ALL = SQL_SELECT_ALL_COMANDO_RECEBIDO
    SQL_SELECT_BY_ID = SQL_SELECT_BY_ID_COMANDO_RECEBIDO
    SQL_UPDATE_COMANDO_PROCESSADO = SQL_UPDATE_COMANDO_PROCESSADO

    def marcar_como_processado(self, _id):
        return self.conn.execute_and_commit(self.SQL_UPDATE_COMANDO_PROCESSADO, (_id,))


if __name__ == '__main__':
    s = ComandoRecebido()
    s.insert_into('nome;endereco;telefone;teste')
    s.select_all()
