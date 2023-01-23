import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
region = data['region']
country = data['country']

print("\nDetalhes do IP externo:\n")
print("IP: {4}\nRegiao: {1}\nPais: {2}\nCidade: {3}\nOrganizacao: {0}".format(org,region,country,city,ip))