import hashlib

menu = 0
string = input("Digite algo: ")
while 0 >= int(menu) or int(menu) >= 5:
    menu = input(''' ### MENU - ESCOLHA O TIPO DE HASH ###
                1 - MD5
                2 - SHA1
                3 - SHA256
                4 - SHA512
                Digite o numero do hash a ser gerado: ''')

if int(menu) == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print("O hash MD5 da string é: ", result.hexdigest())

elif int(menu) == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print("O hash SHA1 da string é: ", result.hexdigest())

elif int(menu) == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print("O hash SHA256 da string é: ", result.hexdigest())

elif int(menu) == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print("O hash SHA512 da string é: ", result.hexdigest())
