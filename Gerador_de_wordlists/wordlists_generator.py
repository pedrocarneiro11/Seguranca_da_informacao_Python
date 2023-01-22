import itertools

string = input("String a ser permutada: ")
counter = 0

result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))
    counter = counter + 1

print("Numero de combinacoes geradas: ", counter)
