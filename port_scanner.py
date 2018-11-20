#!/usr/bin/env python3

import argparse
import socket

def printBanner(connectionSocket, port):
  try:
    if (port == 80):
        connectionSocket.send(b"GET /HTTP/1.1\r\n")
    elif (port == 21):
        connectionSocket.recv(4096)
        connectionSocket.send(b"HELP\r\n")
    else:
      connectionSocket.sendall("\r\n")

    response = connectionSocket.recv(4096)
    print("[+] Banner: %s" % str(response))

  except Exception as e:
      print("[E] Banner not available. Error details: %s" % e)

def connectScan(address, port):
  try:
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionSocket.connect((address, port))
    print("[+] TCP port %d OPEN" % port)
    printBanner(connectionSocket, port)

  except:
    print("[+] TCP port %d CLOSED" % port)

  finally:
    connectionSocket.close()

def portScan(address, ports):
  try:
    targetIp = socket.gethostbyname(address)
  except Exception as e:
    print("[E] Error: unknown host. Error details: %s" % e)
    exit(0)

  try:
    targetName = socket.gethostbyaddr(targetIp)
    print("[+] --- Scan results for %s ---" % targetName[0])

  except Exception as e:
    print("[E] --- Error on scan for %s. Error details: %s. ---" % (targetIp, e))

  socket.setdefaulttimeout(10)

  for port in ports:
    connectScan(address, int(port))

def main():
  parser = argparse.ArgumentParser("TCP client scanner")
  parser.add_argument("-a", "--address", type=str, help="The targets ip address")
  parser.add_argument("-p", "--port", type=str,
                      help="A list of ports to scan separated by ','", required=True)
  args = parser.parse_args()

  ipAddress = args.address
  ports = args.port.split(",")

  portScan(ipAddress, ports)

if __name__ == "__main__":
  main()
