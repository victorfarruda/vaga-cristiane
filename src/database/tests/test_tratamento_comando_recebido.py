from unittest.mock import Mock

import pytest


def test_pode_criar_objeto_tratamento_comando_recebido():
    from database import conn
    conn.psycopg2 = Mock()
    from database.tabela_tratamento_comando_recebido import TratamentoComandoRecebido

    tratamento_comando_recebido = TratamentoComandoRecebido()

    assert isinstance(tratamento_comando_recebido, TratamentoComandoRecebido)


def test_insert_into():
    from database import conn
    conn.psycopg2 = Mock()
    from database.tabela_tratamento_comando_recebido import TratamentoComandoRecebido

    comando_pendente = TratamentoComandoRecebido()
    comando_pendente.conn = Mock()

    comando_pendente.insert_into('v1;2;v4;v5')

    comando_pendente.conn.execute_and_commit.assert_called_once()


def test_insert_into_error():
    from database import conn
    conn.psycopg2 = Mock()
    from database.tabela_tratamento_comando_recebido import TratamentoComandoRecebido

    comando_pendente = TratamentoComandoRecebido()
    comando_pendente.conn = Mock()
    with pytest.raises(Exception):
        comando_pendente.insert_into('v1;2;v4')
