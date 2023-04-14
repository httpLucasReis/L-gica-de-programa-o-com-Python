import ipaddress
import socket

hostname= socket.gethostname()
### ip_address = socket.gethostbyname(hostname)
ip_address = '192.168.100.1'

print(ip_address)

def scanner(ip, port):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)
        scanner.connect((ip, port))
        scanner.close()
        return True
    except:
        return False


ports_found = False
for port in range(1, 1025):
    if scanner(ip_address, port):
        print(f"Porta {port} aberta em {ip_address}")
        ports_found = True

if not ports_found:
    print('Nenhuma porta encontrada aberta')
   