import socket
addr = socket.gethostname(), 7000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = 'NOVOdsd;CAMPO2;000000;CAMPO4'
client_socket.send(mensagem.encode('utf-8'))
print('mensagem enviada')
response = client_socket.recv(1024)
print(response)
client_socket.close()
