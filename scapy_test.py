import scapy

sniffed = scapy.sniff(count=30)
print str(sniffed)
