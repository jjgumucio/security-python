import socket
import threading
import argparse

def serveClient(connection, clientAddress, port):
  try:
    request = connection.recv(4096)
    print "[!] Received data from client (%s:%d): %s" % (clientAddress, port, request)

    connection.send("Response from the basic TCP server!")

    connection.close()

  except Exception as e:
    print e

def startServer(port):
  try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)

    print "[!] Localhost listening on port %d" % port

    while True:
      connection, address = server.accept()
      print "[!] Received connection from %s:%d" % (address[0], int(address[1]))

      serviceThread = threading.Thread(target=serveClient, args=(connection, address[0], address[1]))
      serviceThread.start()

  except Exception as e:
      print "[E] Error on server: %s" % e

def main():
  parser = argparse.ArgumentParser("Basic TCP server")
  parser.add_argument("-p", "--port", type=int, help="Port number to listen on")
  args = parser.parse_args()
  port = args.port

  startServer(int(port))

if __name__ == "__main__":
  main()
