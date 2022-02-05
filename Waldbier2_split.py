import Bio
from Bio import SeqIO
import os 
import statistics

path = '/u/home/praktikum/Praktikum012019/Project data/'

def get_files():
    files = []
    dirs = os.listdir(path)
    for filenames in dirs:
        if filenames.endswith(".fq"):
             files.append(filenames)
    return files  

def sorted_files(files):
    sequence_250 = []
    sequence_500 = []
    sequence_1000 = []
    sequence_2000 = []
    sequence_4000 = []
    sequence_6000 = []
    sequence_6150 = []
    sequence_7000 = []
    sequence_13000 = []
    sequence_16000 = []
    sequence_20000 = []
    sequence_20001 = []
    for n in range(len(files)):
        for record in SeqIO.parse(path + files[n], "fastq"):
            if (len(record) < 251):
                sequence_250.append(record)
            elif (len(record) > 501 && ):
                sequence_500.append(record)
            elif (len(record) < 1001):
                sequence_1000.append(record)
            elif (len(record) < 2001):
                sequence_2000.append(record)
            elif (len(record) < 4001):
                sequence_4000.append(record)
            elif (len(record) < 6001):
                sequence_6000.append(record)
            elif (len(record) < 6151):
                sequence_6150.append(record)
            elif (len(record) < 7001):
                sequence_7000.append(record)
            elif (len(record) < 13001):
                sequence_13000.append(record)
            elif (len(record) < 16001):
                sequence_16000.append(record)
            elif (len(record) < 20001):
                sequence_20000.append(record)
            else:
                sequence_20001.append(record)

    for n in range(len(sequence_20001)):
        print(len(sequence_20001[n]))
        SeqIO.write(sequence_8001[n], "Waldbier_MG2_max_"+str(n)+".fasta", "fasta")

    SeqIO.write(sequence_250, "Waldbier2_MG2_250.fasta", "fasta")
    SeqIO.write(sequence_500, "Waldbier2_MG2_500.fasta", "fasta")
    SeqIO.write(sequence_1000, "Waldbier2_MG2_1000.fasta", "fasta")
    SeqIO.write(sequence_2000, "Waldbier2_MG2_2000.fasta", "fasta")
    SeqIO.write(sequence_4000, "Waldbier2_MG2_4000.fasta", "fasta")
    SeqIO.write(sequence_6000, "Waldbier2_MG2_6000.fasta", "fasta")
    SeqIO.write(sequence_6150, "Waldbier2_MG2_6150.fasta", "fasta")
    SeqIO.write(sequence_7000, "Waldbier2_MG2_7000.fasta", "fasta")
    SeqIO.write(sequence_13000, "Waldbier2_MG2_13000.fasta", "fasta")
    SeqIO.write(sequence_16000, "Waldbier2_MG2_16000.fasta", "fasta")
    SeqIO.write(sequence_20000, "Waldbier2_MG2_20000.fasta", "fasta")
    print(len(sequence_250))
    print(len(sequence_500))
    print(len(sequence_1000))
    print(len(sequence_2000))
    print(len(sequence_4000))
    print(len(sequence_6000))
    print(len(sequence_6150))
    print(len(sequence_7000))
    print(len(sequence_13000))
    print(len(sequence_16000))
    print(len(sequence_20000))

sorted_files(get_files())
