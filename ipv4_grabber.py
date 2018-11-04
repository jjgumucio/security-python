#!/usr/bin/python3
import subprocess
import argparse
import re

def get_ipv4_addresses(domain):
    """Returns a list of IPv4 addresses for the given domain name."""
    ipv4_regex = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    try:
        output = subprocess.run(["whois", domain], stdout=subprocess.PIPE,
                                text=True)
        ip_addresses = re.findall(ipv4_regex, output.stdout)
        print("[i] Found %d IP addresses" % len(ip_addresses))
        return ip_addresses
    except Exception as e:
        print("[E] Error running 'whois' for domain %s: %s" % (domain, e))

def write_file(addresses, filename):
    """Writes each IP address of <addresses> array at a new line on <filename> file"""
    try:
        with open(filename, mode="w") as file:
            for address in addresses:
                file.write(f"""{address}\n""")
        print("[i] Wrote %d IP addresses on file %s" % (len(addresses), filename))
    except Exception as e:
        print("[E] Error writing ip addresses to file %s: %s" % (filename, e))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", type=str, help="Domain name to get ip address of",
                        required=True)
    parser.add_argument("-s", "--save", type=str, help="Save addresses to file [FILENAME]")
    args = parser.parse_args()
    domain = args.domain
    filename = args.save

    ip_addresses = get_ipv4_addresses(domain)
    if (filename):
        write_file(ip_addresses, filename)

if __name__ == "__main__":
    main()


