import socket

addr = 'entrada', 7000

client_socket = socket.socket()
client_socket.connect(addr)

mensagem = 'UAITREM;CAMPO2;000000;CAMPO4'

client_socket.send(mensagem.encode('utf-8'))
print('mensagem enviada')

response = client_socket.recv(1024)
print(response)

client_socket.close()
