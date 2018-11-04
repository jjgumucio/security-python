from ftplib import FTP
import argparse

def connect_ftp(host):
    try:
        with FTP(host, timeout=10) as ftp:
            print(ftp.dir())
    except Exception as e:
        print("[E] Error connecting to FTP service: %s" % e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", required=True, type=str,
                        help="FTP host to connect to")
    args = parser.parse_args()
    host = args.address

    connect_ftp(host)

if __name__ == "__main__":
    main()
