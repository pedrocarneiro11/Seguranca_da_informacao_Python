import os

print("#" * 60)

ip = input("Digite o ip ou host a ser verificado: ")
print("-" * 60)
os.system(f'ping -n 6 {ip}')
print("-" * 60)