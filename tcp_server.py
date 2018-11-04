#!/usr/bin/env python3

import socket
import threading
import argparse

def serve_client(connection, client_address, port):
  try:
    request = connection.recv(1024)
    print("[!] Received data from client (%s:%d): %s" % (client_address, port, request))

    connection.send(b"Response from the basic TCP server!")

    connection.close()

  except Exception as e:
    print("[E] Error serving client with address %s on port %s. %s" % (client_address, port, e))

def start_server(address, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((address, port))
            server.listen(5)

            print("[!] Localhost listening on port %d" % port)

            while True:
                client_socket, client_address = server.accept()
                host, port = client_address
                print("HOST: %s; PORT: %s" % (host, port))
                print("[!] Received connection from %s:%d" % (host, int(port)))
                serve_client(client_socket, host, port)

            # TODO: Update to use asyncio for concurrency instead of threading
            # service_thread = threading.Thread(target=serve_client, args=(connection, address[0], address[1]))
            # service_thread.start()

    except Exception as e:
        print("[E] Error on server: %s" % e)

def main():
    parser = argparse.ArgumentParser("Basic TCP server")
    parser.add_argument("-a", "--address", type=str, nargs="?", default="127.0.0.1",
                        help="IP address to listen to. Defaults to localhost")
    parser.add_argument("-p", "--port", required=True,
                        help="Port number to listen to")
    args = parser.parse_args()
    address = args.address
    port = args.port

    start_server(address, int(port))

if __name__ == "__main__":
    main()
