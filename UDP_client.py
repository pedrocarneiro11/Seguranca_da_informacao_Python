import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print('\nCliente Socket Criado Com Sucesso')

    host = 'localhost'
    port = 5432
    message = " "

    print('\nCliente: ' + message)
    s.sendto(message.encode(), (host, port))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print("Client: " + data)

except socket.error as e:
    pass
    # 2o bloco com erro
    # print("2o bloco try")
    # print("Nao foi possivel criar o Cliente Socket, erro: {}".format(e))

finally:
    print("Cliente: Fechando a conexao...")
    s.close()
