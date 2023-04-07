from . import socket
from database.tabela_comando_pendente import ComandoPendente
from database.tabela_comando_recebido import ComandoRecebido


class GatewayEntrada:
    def __init__(self):
        addr = ('entrada', 7000)
        self.server_socket = socket.socket()
        self.server_socket.bind(addr)
        self.server_socket.listen(1)

        self.comando_recebido = ComandoRecebido()
        self.comando_pendente = ComandoPendente()

    def processar(self, data, conn):
        self.comando_recebido.insert_into(data)
        _id, campos = self.comando_pendente.select_last()
        conn.send(campos.encode())

    def run(self):
        conn, address = self.server_socket.accept()
        data = conn.recv(1024).decode()
        if data:
            self.processar(data, conn)
        conn.close()


gateway_entrada = GatewayEntrada()
