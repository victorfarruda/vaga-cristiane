import logging


from database.tabela_tratamento_comando_recebido import TratamentoComandoRecebido

from database.tabela_comando_recebido import ComandoRecebido


class GatewayTratamento:
    def __init__(self):
        self.tratamento_string_recebida = TratamentoComandoRecebido()
        self.comando_pendente = ComandoRecebido()

    def inserir(self, string):
        self.tratamento_string_recebida.insert_into(string)

    def run(self):
        logging.log(logging.INFO, 'RODANDO')
        print('RODANDO print')
        results = self.comando_pendente.select_all()
        for _id, campos, processado in results:
            self.tratamento_string_recebida.insert_into(campos)
            self.comando_pendente.marcar_como_processado(_id)
            print('último id processado', _id)


gateway_tratamento = GatewayTratamento()
