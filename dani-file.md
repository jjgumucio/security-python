# danidaniels.com Pentest

## Recon:
**Domain:** danidaniels.com
**IP:** 31.192.113.173 Obtained making a ping request to the domain
**MAILSERVER:** 20 mail.danidaniels.com

**NOTES:** It seems that the ip obtained belongs to domain modelcentro.com

### Services / Ports (nmap report):
Nmap scan report for 31.192.113.173
Host is up (0.32s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE    VERSION
21/tcp   open  tcpwrapped
80/tcp   open  http       nginx
|_http-server-header: nginx
|_http-title: Did not follow redirect to https://modelcentro.com
443/tcp  open  ssl/http   nginx
|_http-server-header: nginx
|_http-title: Did not follow redirect to https://modelcentro.com
| ssl-cert: Subject: commonName=mcprofits.com
| Subject Alternative Name: DNS:mcprofits.com
| Not valid before: 2018-02-03T07:08:16
|_Not valid after:  2019-02-14T11:12:23
|_ssl-date: TLS randomness does not represent time
8086/tcp open  websocket  Ogar agar.io server
Device type: general purpose
Running (JUST GUESSING): Linux 3.X (85%)
OS CPE: cpe:/o:linux:linux_kernel:3.0
Aggressive OS guesses: Linux 3.0 (85%)
No exact OS matches for host (test conditions non-ideal).

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   3.82 ms   172.20.10.1
2   ...
3   150.17 ms 172.16.64.177
4   ... 5
6   150.19 ms 172.16.66.17
7   134.63 ms 172.18.86.82
8   ... 30

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 501.48 seconds


