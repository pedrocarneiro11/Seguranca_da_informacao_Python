import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    print('\nCliente Socket Criado Com Sucesso')

    host = 'localhost'
    port = 5433
    message = "Hello World 123"

    print('\nCliente: ' + message)
    s.sendto(message.encode(), (host, 5433))

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
