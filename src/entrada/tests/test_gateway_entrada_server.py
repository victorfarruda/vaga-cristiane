from unittest.mock import Mock


def test_pode_criar_gateway_entrada():
    import database.conn
    database.conn.psycopg2 = Mock()
    import entrada
    entrada.socket = Mock()
    import entrada.gateway_entrada_server
    entrada.gateway_entrada_server.socket = Mock()
    entrada.gateway_entrada_server.TratamentoComandoRecebido = Mock()
    entrada.gateway_entrada_server.ComandoRecebido = Mock()

    gateway_tratamento = entrada.gateway_entrada_server.GatewayEntrada()

    assert isinstance(gateway_tratamento, entrada.gateway_entrada_server.GatewayEntrada)


def test_chama_metodo_processar():
    import database.conn
    database.conn.psycopg2 = Mock()
    import entrada
    entrada.socket = Mock()
    import entrada.gateway_entrada_server
    entrada.gateway_entrada_server.socket = Mock()
    entrada.gateway_entrada_server.ComandoPendente = Mock()
    entrada.gateway_entrada_server.ComandoRecebido = Mock()

    gateway_tratamento = entrada.gateway_entrada_server.GatewayEntrada()
    gateway_tratamento.comando_pendente.select_last = Mock(return_value=(1, 'mensagem'))
    gateway_tratamento.processar('process;process;process;pp', Mock())

    gateway_tratamento.comando_recebido.insert_into.assert_called_once()
    gateway_tratamento.comando_pendente.select_last.assert_called_once()


def test_chama_metodo_run():
    import database.conn
    database.conn.psycopg2 = Mock()
    import entrada
    entrada.socket = Mock()
    import entrada.gateway_entrada_server
    entrada.gateway_entrada_server.socket = Mock()
    entrada.gateway_entrada_server.ComandoPendente = Mock()
    entrada.gateway_entrada_server.ComandoRecebido = Mock()

    gateway_tratamento = entrada.gateway_entrada_server.GatewayEntrada()
    gateway_tratamento.comando_pendente.select_last = Mock(return_value=(1, 'mensagem'))
    gateway_tratamento.server_socket = Mock()
    gateway_tratamento.server_socket.accept = Mock(return_value=(Mock(), 10))
    gateway_tratamento.processar = Mock()

    gateway_tratamento.run()

    gateway_tratamento.processar.assert_called_once()
    gateway_tratamento.server_socket.accept.assert_called_once()
