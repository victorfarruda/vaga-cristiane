import socket

from decouple import config

addr = 'entrada', 7000

client_socket = socket.socket()
client_socket.connect(addr)

mensagem = config('MENSAGEM_CLIENTE', 'TESTE1;TESTE2;TESTE3;TESTE4')

client_socket.send(mensagem.encode('utf-8'))
print('mensagem enviada')

response = client_socket.recv(1024)
print(response)

client_socket.close()
