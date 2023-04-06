import logging

from database.tabela_comando_pendente import ComandoPendente
from database.tabela_tratamento_string_recebida import TratamentoStringRecebida
from logging import log


class GatewayTratamento:
    def __init__(self):
        self.tratamento_string_recebida = TratamentoStringRecebida()
        self.comando_pendente = ComandoPendente()

    def inserir(self, string):
        self.tratamento_string_recebida.insert_into_string_recebida(string)

    def run(self):
        results = self.comando_pendente.select_all()
        for _id, campos, processado in results:
            self.tratamento_string_recebida.insert_into_string_recebida(campos)
            self.comando_pendente.marcar_como_processado(_id)
            print('último id processado', _id)


gateway_tratamento = GatewayTratamento()
