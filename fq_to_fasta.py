import Bio
from Bio import SeqIO
import os 

path = '/u/home/praktikum/Praktikum012019/Project data/'

def get_files():
    files = []
    dirs = os.listdir(path)
    for filenames in dirs:
        if filenames.endswith(".fq"):
             files.append(filenames)
    return files  

def turn_into_fasta(files):
    sequence = []
    for n in range(len(files)):
        print(files[n])
        for record in SeqIO.parse(path + files[n], "fastq"):
            sequence.append(record)
    SeqIO.write(sequence, "Waldbier2_MG2.fasta", "fasta")

turn_into_fasta(get_files())
