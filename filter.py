lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def pares(i):
    if i % 2 == 0:
        return i


def impares(i):
    if i % 2 == 1:
        return i


lista_impar = filter(impares, lista)
lista_par = filter(pares, lista)

print(list(lista_impar))
print(list(lista_par))
