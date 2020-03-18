def dobro(x):
    return x*2

lista = [1,2,3,4,5]

print(list(map(dobro,lista)))


print(list(map(lambda i: i*2,lista)))