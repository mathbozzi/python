# -*-coding: utf-8 -*-

nome = input("arquivo que deseja abrir:")

arquivo = open(nome)

linhas = arquivo.readlines()

for l in linhas:
    print(l.strip())
