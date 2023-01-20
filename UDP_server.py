import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Socket criado com sucesso!")

    host = 'localhost'
    port = '5432'

    s.bind((host, int(port)))
    mensagem = 'Server says: Hello World'

    while 1:
        dados, end = s.recvfrom(4096)

        if dados:
            print('Servidor enviando mensagem...')
            s.sendto((dados + mensagem.encode()), end)

except socket.error as e:
    print(" Error: {}".format(e))
