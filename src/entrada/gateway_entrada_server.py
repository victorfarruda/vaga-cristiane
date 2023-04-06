import socket

from database.tabela_comando_pendente import ComandoPendente
from database.tabela_comando_recebido import ComandoRecebido


class GatewayEntrada:
    def __init__(self):
        addr = ('10.5.0.5', 7000)
        self.server_socket = socket.socket()
        self.server_socket.bind(addr)
        self.server_socket.listen(1)

        self.comando_recebido = ComandoRecebido()
        self.comando_pendente = ComandoPendente()

    def run(self):
        print('aguardando conexao')
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if data:
            _id = self.comando_recebido.insert_into(data)
            id, campos = self.comando_pendente.select_last()
        print("from connected user: " + str(data))
        conn.send(campos.encode())  # send data to the client
        conn.close()  # close the connection


gateway_entrada = GatewayEntrada()


if __name__ == '__main__':
    gateway_entrada.run()
