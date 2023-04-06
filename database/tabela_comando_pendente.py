from database.conn import BaseString
from database.query import (
    SQL_CREATE_TABLE_COMANDO_PENDENTE,
    SQL_INSERT_COMANDO_PENDENTE,
    SQL_SELECT_ALL_COMANDO_PENDENTE,
    SQL_SELECT_BY_ID_COMANDO_PENDENTE,
    SQL_UPDATE_COMANDO_PROCESSADO
)


class ComandoPendente(BaseString):
    SQL_CREATE = SQL_CREATE_TABLE_COMANDO_PENDENTE
    SQL_INSERT = SQL_INSERT_COMANDO_PENDENTE
    SQL_SELECT_ALL = SQL_SELECT_ALL_COMANDO_PENDENTE
    SQL_SELECT_BY_ID = SQL_SELECT_BY_ID_COMANDO_PENDENTE
    SQL_UPDATE_COMANDO_PROCESSADO = SQL_UPDATE_COMANDO_PROCESSADO

    def marcar_como_processado(self, _id):
        return self.conn.execute_and_commit(self.SQL_UPDATE_COMANDO_PROCESSADO, (_id,))


if __name__ == '__main__':
    s = ComandoPendente()
    s.insert_into_string_recebida('nome;endereco;telefone;teste')
    s.select_all()
