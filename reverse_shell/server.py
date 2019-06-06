import socket
import argparse

def connect(address_family=('localhost', 8080)):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Starting server...')
    s.bind(address_family)
    s.listen(1)
    print('Waiting for connections...')
    connection, address = s.accept()

    while 1:
        command = input('Shell> ')
        if 'terminate' in command:
            connection.send(command.encode('utf-8'))
            print("Last reception:", connection.recv(1024).decode())
            s.close()
            break
        else:
            connection.send(command.encode('utf-8'))
            print(connection.recv(1024).decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", type=str,
                        help="Ip address to bind to")
    parser.add_argument("-p", "--port", type=int,
                        help="Port to bind to")
    args = parser.parse_args()

    if args.address and args.port:
        connect((args.address, args.port))
    else:
        connect()
