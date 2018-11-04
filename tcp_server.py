#!/usr/bin/env python3

import socket
import threading
import argparse

def serve_client(connection, client_address, port):
  try:
    request = connection.recv(1024)
    print("[!] Received data from client (%s:%d): %s" % (client_address, port, request))

    connection.send("Response from the basic TCP server!")

    connection.close()

  except Exception as e:
    print("[E] Error serving client with address %s on port %s" % (client_address, port))

def start_server(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("0.0.0.0", port))
            server.listen(5)

            print("[!] Localhost listening on port %d" % port)

            while True:
                connection, address = server.accept()
                print("[!] Received connection from %s:%d" % (address[0], int(address[1])))

            # TODO: Update to use asyncio for concurrency instead of threading
            service_thread = threading.Thread(target=serve_client, args=(connection, address[0], address[1]))
            service_thread.start()

    except Exception as e:
        print("[E] Error on server: %s" % e)

def main():
    parser = argparse.ArgumentParser("Basic TCP server")
    parser.add_argument("-p", "--port", type=int, help="Port number to listen to")
    args = parser.parse_args()
    port = args.port

    start_server(int(port))

if __name__ == "__main__":
    main()
