# -*-coding: utf-8 -*-
import re

seq1 = input("digite uma sequencia:")
seq2 = input("digite outra sequencia:")

if (seq1)==(seq2):
    print("igual")
else:
    print("diferente")

busca = re.match(seq1,seq2)

if busca:
    print("igual")
    print(busca.group())
else:
    print("diferente")