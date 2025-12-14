from ping3 import ping
from urllib.parse import urlparse

def extract_host(data: str) -> str | None:
    try:
        parsed = urlparse(data)
        return parsed.hostname
    except Exception:
        return None

def test_ping(host):
    try:
        response = ping(host, timeout=0.5)
        if response is not None:
            print(f"Ping to {host} successful, round-trip time: {response} ms")
            return True
        else:
            print(f"Ping to {host} failed")
            return False
    except Exception:
        print(f"Ping to {host} failed")

file = open("whitelist.txt", "r")
lines = file.readlines()

out_file = open("working_vpn.txt", "w")

for line in lines:
    line = line.strip()
    ip_address = extract_host(line)
    test = test_ping(ip_address)
    if test == True:
        out_file.write(line + "\n")
