from ip_scanner import scan_ips
from port_scanner import scan_ports
from time import time
import threading
from multiprocessing.pool import ThreadPool



# find ips in lan
print('start scanning LAN...')
start = time()
ips = scan_ips(start='192.168.43.0', end='192.168.43.255')
end = time()


print(f'found {len(ips)} ips in {int(end-start)}s.')
print('--------------------------------------------' )
print('scan ports for found IPs...')


# scan all ips
pool = ThreadPool(processes=len(ips))
start = time()
ip_ports = {ip:pool.apply_async(scan_ports, (ip, )).get() for ip in ips}
end = time()


for i,ip in enumerate(ip_ports):
    ports = ', '.join([str(p) for p in ip_ports[ip]])
    print(f'{i+1}:\t {ip}\t => {ports}')
    
print(f'scanned in {int(end-start)}s')