import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        print(addr)


def send_message(client_socket):
    while True:
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "Hello, world\n".encode()
            client_socket.send(response)

    client_socket.close()
    print("Connection cloes")

if __name__ == '__main__':
    accept_connection(server_socket)