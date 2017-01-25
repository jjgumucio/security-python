import socket
import struct
from ctypes import *

class IPHeader(Structure):
  _fields = [
    ("ihl", c_ubyte, 4),
    ("version", c_ubyte, 4),
    ("tos", c_ubyte),
    ("len", c_ushort),
    ("id", c_ushort),
    ("offset", c_ushort),
    ("ttl", c_ubyte),
    ("protocol_num", c_ubyte),
    ("sum", c_ushort),
    ("src", c_uint32),
    ("dst", c_uint32)
  ]

  def __new__(self, data=None):
    return self.from_buffer_copy(data)

  def __init__(self, data=None):
    # Map source and destination addresses
    self.source_address = socket.inet_ntoa("@I", self.src)
    self.destination_address = socket.inet_ntoa("@I", self.dst)

    # Map for protocols
    self.protocols = {1: "ICMP", 6: "TCP", 17: "UDP"}

    # Get protocol name
    try:
      self.protocol = self.prootocols[self.protocol_num]
    except:
      self.protocol = str(self.protocol_num)

def initSocket():
  tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
  tcp_socket.bind(("127.0.0.1", 0))

  # Include the IP header?
  tcp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

  return tcp_socket

def startSniffer():
  tcp_sniffer = initSocket()
  print "[+] Sniffer listening for incoming connections"

  try:
    while True:
      raw_buffer = tcp_sniffer.recvfrom(65535)[0]
      ip_header = IPHeader(raw_buffer[0:20])

      print ip_header.protocol

      if ip_header.protocol == "TCP":
        print "Protocol: %s %s -> %s" % (ip_header.protocol, ip_header.source_address, ip_header.destination_address)

      elif ip_header_protocol == "ICMP":
        print "Protocol: ICMP"

  except KeyboardInterrupt:
    print "Exiting sniffer..."
    exit(0)

if __name__ == "__main__":
  startSniffer()
