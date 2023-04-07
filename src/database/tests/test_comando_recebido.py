from unittest.mock import Mock


def test_pode_criar_objeto_comando_recebido():
    from database import conn
    conn.psycopg2 = Mock()
    from database.tabela_comando_recebido import ComandoRecebido

    comando_pendente = ComandoRecebido()

    assert isinstance(comando_pendente, ComandoRecebido)


def test_marcar_como_processado():
    from database import conn
    conn.psycopg2 = Mock()
    from database.tabela_comando_recebido import ComandoRecebido

    comando_pendente = ComandoRecebido()
    comando_pendente.conn = Mock()

    comando_pendente.marcar_como_processado(1)

    comando_pendente.conn.execute_and_commit.assert_called_once()
