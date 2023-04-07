from unittest.mock import Mock


def test_pode_criar_gateway_tratamento():
    import database.conn
    database.conn.psycopg2 = Mock()
    import tratamento.gateway_tratamento
    tratamento.gateway_tratamento.TratamentoComandoRecebido = Mock()
    tratamento.gateway_tratamento.ComandoRecebido = Mock()

    gateway_tratamento = tratamento.gateway_tratamento.GatewayTratamento()

    assert isinstance(gateway_tratamento, tratamento.gateway_tratamento.GatewayTratamento)


def test_chama_metodo_inserir():
    import database.conn
    database.conn.psycopg2 = Mock()
    import tratamento.gateway_tratamento
    tratamento.gateway_tratamento.TratamentoComandoRecebido = Mock()
    tratamento.gateway_tratamento.ComandoRecebido = Mock()

    gateway_tratamento = tratamento.gateway_tratamento.GatewayTratamento()

    gateway_tratamento.tratamento_string_recebida = Mock()
    gateway_tratamento.comando_pendente = Mock()

    gateway_tratamento.inserir('inserir;inserir', 10)

    gateway_tratamento.tratamento_string_recebida.insert_into.assert_called_once()
    gateway_tratamento.comando_pendente.marcar_como_processado.assert_called_once()


def test_chama_metodo_run():
    import database.conn
    database.conn.psycopg2 = Mock()
    import tratamento.gateway_tratamento
    tratamento.gateway_tratamento.TratamentoComandoRecebido = Mock()
    tratamento.gateway_tratamento.ComandoRecebido = Mock()

    gateway_tratamento = tratamento.gateway_tratamento.GatewayTratamento()

    gateway_tratamento.tratamento_string_recebida = Mock()
    gateway_tratamento.comando_pendente = Mock()
    gateway_tratamento.comando_pendente.select_all = Mock(return_value=[(1, 'campos', False)])

    gateway_tratamento.run()

    gateway_tratamento.tratamento_string_recebida.insert_into.assert_called_once()
    gateway_tratamento.comando_pendente.select_all.assert_called_once()
    gateway_tratamento.comando_pendente.marcar_como_processado.assert_called_once()
