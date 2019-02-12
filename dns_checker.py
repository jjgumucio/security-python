import argparse
import requests
from datetime import time

def check_dns(record_type, domain_name):
    url = f'''https://dns-api.org/{record_type}/{domain_name}'''
    print(url)
    response = requests.get(url)
    dns = response.json()
    if not len(dns):
        print("No DNS information")
    else:
        print(dns)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--record_type", required=True, type=str,
                        help="type: CNAME/A/MX")
    parser.add_argument("-d", "--domain", required=True, type=str,
                        help="Domain name")
    args = parser.parse_args()
    check_dns(args.record_type, args.domain)

if __name__ == "__main__":
    main()
