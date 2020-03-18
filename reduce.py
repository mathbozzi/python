
# soma = 0
# lista = [1,2,3,4,5,6,7]

# for i in lista:
#     soma = soma + i

# print(soma)

from functools import reduce

lista = [1,2,3,4,5,6,7]

def soma(x,y):
    return x+y

soma = reduce(soma,lista)

print(soma)
