import ctypes

atributos_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('arquivo_a_ocultar.txt', atributos_ocultar)

if retorno:
    print("O arquivo foi ocultado")
else:
    print("O arquivo nao foi ocultado")