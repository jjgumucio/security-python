#!/usr/bin/env python3

import socket
import argparse

def connect(address, port):
    print("[!] Connecting to host at: %s on port %s" % (address, port))
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((address, port))
            client.sendall(b"Hello server from the client")
            response = client.recv(1024)
            print("Response from server: %s" % response)
    except Exception as e:
        print("[E] Error connecting to host: %s on port: %s. %s" % (address, port, r))

def main():
    parser = argparse.ArgumentParser("Very simple TCP client")
    parser.add_argument("-a", "--address", type=str, default="127.0.0.1", nargs="?",
                        help="IP address to connect to. Defaults to localhost")
    parser.add_argument("-p", "--port", type=int, required=True,
                        help="Port number to connect to")
    args = parser.parse_args()
    address = args.address
    port = args.port

    connect(address, int(port))

if __name__ == "__main__":
    main()

