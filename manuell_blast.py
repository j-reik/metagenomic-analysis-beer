import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
import statistics
import os 
import random

sequence = []
length = []
quality = []
pass_path = '/u/home/praktikum/Praktikum012019/fastq_pass/'
fail_path = '/u/home/praktikum/Praktikum012019/fastq_fail/'
beer_type = 'Mix/'

def get_files(path):
    files = []
    dirs = os.listdir(path + beer_type)
    for filenames in dirs:
        if filenames.endswith(".fastq"):
             files.append(filenames)
    return files  

def read_sequences(filenames, path):
    print(filenames)
    for n in range(len(filenames)):
        print(filenames[n])
        for record in SeqIO.parse(path + beer_type + filenames[n], "fastq"):
            sequence.append(record)
            length.append(len(record))
            quality.append(record.letter_annotations["phred_quality"])
    print("List is done!")

def quality_files():
    good_quality = []
    for n in range(len(sequence)):
        if len(sequence[n]) > 100 and statistics.mean(sequence[n].letter_annotations["phred_quality"]) > 16:
            good_quality.append(sequence[n])
    subset = random.sample(good_quality, 10)
    SeqIO.write(subset, "Mix_subset.fasta", "fasta")
    print("Quality check")
    #return good_quality
    

read_sequences(get_files(pass_path), pass_path)
quality_files()

