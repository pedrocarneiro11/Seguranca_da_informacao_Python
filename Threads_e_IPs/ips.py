import ipaddress

ip = '192.168.0.0/24'

rede = ipaddress.ip_network(ip)

print(rede)
