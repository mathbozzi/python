#-*-coding: utf-8 -*-

seq = input("digite uma sequancia fasta:")

arquivoFasta = open("seq.fasta","w")
arquivoFasta.write("seq>\n")
arquivoFasta.write(seq)
arquivoFasta.close()
