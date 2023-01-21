from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Carro: {} Km {} \n'.format(piloto, trajeto))


t_carro1 = Thread(target=carro, args=[5, 'Piloto1'])
t_carro2 = Thread(target=carro, args=[10, 'Piloto2'])

t_carro1.start()
t_carro2.start()
