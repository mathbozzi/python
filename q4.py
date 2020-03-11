arquivo = open("seq.fasta")

linhas = arquivo.readlines()

multifasta = {}

for l in linhas:
    if l[0] == ">":
        seq = l[1:4]
        multifasta[seq] = ""
    else:
        multifasta[seq] = multifasta[seq]+l.strip()

print(multifasta)