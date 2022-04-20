from ip_scanner import scan_ips
from port_scanner import scan_ports
from time import time


# find ips in lan
print('start scanning LAN...')
start = time()
ips = scan_ips(start='172.18.220.0', end='172.18.223.255')
end = time()


# choose ip to find open ports
for i,ip in enumerate(ips):
    print(f'{i+1}: {ip}')
print(f'found {len(ips)} ips in {int(end-start)}s.')
ip_index = input('select one of them to find open ports: ')


# find ports for selected addr
print('-' * 20)
print('srat scanning ports...')
start = time()
ports = scan_ports(ips[int(ip_index)-1])
end = time()
print(f'found {len(ports)} ports for ip={ip} in {int(end-start)}s:')
print(', '.join([str(p) for p in ports]))