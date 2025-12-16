from singbox2proxy import SingBoxProxy

def test_ping(host):
    try:
        response = host.request("GET", "https://api.ipify.org?format=json", timeout=1, retries=1)
        if response.status_code == 200:
            print(f"Ping to {response.text} successful, round-trip time: {response} ms")
            return True
        else:
            print(f"Ping to {response.text} failed")
            return False
    except Exception:
        print(f"Ping failed")
        return False

file = open("whitelist.txt", "r")
lines = file.readlines()
file.close()

out_file = open("working_vpn.txt", "w")

c = 0
for line in lines:
    c += 1
    line = line.strip()
    try:
        with SingBoxProxy(line) as vless_address:
            test = test_ping(vless_address)
            print(f"\nProgress: {c}/{len(lines)}")
            if test == True:
                out_file.write(line + "\n")
                out_file.flush()
    except Exception as e:
        print(f"Error creating proxy object for line {c}: {e}")
        continue

out_file.close()
