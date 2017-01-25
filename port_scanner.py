import argparse
import socket

def printBanner(connectionSocket, port):
  try:
    if (port == 80):
      connectionSocket.send("GET HTTP/1.1 \r\n")
    else:
      connectionSocket.send("\r\n")

    response = connectionSocket.recv(4096)
    print "[+] Banner: %s" % str(response)

  except:
    print "[+] Banner not available"

def connectScan(address, port):
  try:
    connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionSocket.connect((address, port))
    print "[+] TCP port %d OPEN" % port
    printBanner(connectionSocket, port)

  except Exception as e:
    print e
    print "[+] TCP port %d CLOSED" % port

  finally:
    connectionSocket.close()

def portScan(address, ports):
  try:
    targetIp = socket.gethostbyname(address)
  except:
      print "[-] Error: unknown host"
      exit(0)

  try:
    targetName = socket.gethostbyaddr(targetIp)
    print "[+] --- Scan results for %s ---" % targetName[0]

  except:
    print "[+] --- Scan results for %s ---" % targetIp

  socket.setdefaulttimeout(10)

  for port in ports:
    connectScan(address, int(port))


def main():
  parser = argparse.ArgumentParser("TCP client scanner")
  parser.add_argument("-a", "--address", type=str, help="The targets ip address")
  parser.add_argument("-p", "--port", type=str, help="A list of ports to scan separated by ','")
  args = parser.parse_args()

  ipAddress = args.address
  ports = args.port.split(",")

  portScan(ipAddress, ports)

if __name__ == "__main__":
  main()
