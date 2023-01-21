import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())
conteudo_hash1 = hash1.digest()

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())
conteudo_hash2 = hash2.digest()

if conteudo_hash1 == conteudo_hash2:
    print("Hashes iguais")
else:
    print("Hashes diferentes")