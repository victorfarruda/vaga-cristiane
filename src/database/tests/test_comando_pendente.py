from unittest.mock import Mock


def test_pode_criar_objeto_comando_pendente():
    from database import conn
    conn.psycopg2 = Mock()
    from database.tabela_comando_pendente import ComandoPendente
    ComandoPendente.select_last = Mock(return_value=None)

    comando_pendente = ComandoPendente()

    assert isinstance(comando_pendente, ComandoPendente)

