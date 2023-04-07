from decouple import config

from database.conn import Base
from database.query import (
    SQL_CREATE_TABLE_COMANDO_PENDENTE,
    SQL_INSERT_COMANDO_PENDENTE,
    SQL_SELECT_ALL_COMANDO_PENDENTE,
    SQL_SELECT_LAST_COMANDO_PENDENTE,
)


class ComandoPendente(Base):
    SQL_CREATE = SQL_CREATE_TABLE_COMANDO_PENDENTE
    SQL_INSERT = SQL_INSERT_COMANDO_PENDENTE
    SQL_SELECT_ALL = SQL_SELECT_ALL_COMANDO_PENDENTE
    SQL_SELECT_LAST = SQL_SELECT_LAST_COMANDO_PENDENTE

    def __init__(self):
        super().__init__()
        last = self.select_last()
        if last is None:
            self.insert_into(config('INSERSAO_MANUAL', 'teste4;teste5;teste6;teste7'))
