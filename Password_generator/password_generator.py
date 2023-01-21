import random
import string

size = int(input("Digite o tamanho desejado para a senha: "))

chars = string.ascii_letters + string.digits + 'çÇ!@#$%&*()-+[]{}^~/?,.'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))
