import socket


def server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_address = ('localhost', 12345)
	server_socket.bind(server_address)

	server_socket.listen(5)
	print('waiting for a connection...')

	while True:
		client_socket, client_address = server_socket.accept()
		print(f'received connection from {client_address}')

		data = client_socket.recv(1024).decode()  # ждет получения данных
		print(f'received data: {data}')

		responce = f'server respond: {data}'
		client_socket.send(responce.encode())

		client_socket.close()


if __name__ == '__main__':
	server()
