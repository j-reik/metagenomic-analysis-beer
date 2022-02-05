import Bio
from Bio import SeqIO
from Bio.Blast import NCBIWWW
import matplotlib.pyplot as plt
import numpy as np
import statistics
import os 
import random

#Datei beschriftung png anpassen x/y nicht fail/pass sondern dateiname?

length = []
quality = []
pass_path = '/u/home/praktikum/Praktikum012019/fastq_pass/'
fail_path = '/u/home/praktikum/Praktikum012019/fastq_fail/'
beer_type = 'Waldbier2/'

def get_files(path):
    files = []
    dirs = os.listdir(path + beer_type)
    for filenames in dirs:
         files.append(filenames)
    return files  

def quality_files(good_quality):
    #for n in range(len(data)):
    #    if len(data[n]) > 100 and statistics.mean(data[n].letter_annotations["phred_quality"]) > 14:
    #        good_quality.append(data[n])
    print(len(good_quality))
    subset = random.sample(good_quality, 10)
    SeqIO.write(subset, "pass_Waldbier2_test.fasta", "fasta")
    print("Quality check")

def read_sequences(filenames, path):
    sequence = []
    print(filenames)
    for n in range(len(filenames)):
        print(filenames[n])
        for record in SeqIO.parse(path + beer_type + filenames[n], "fastq"):
            length.append(len(record))
            quality.append(record.letter_annotations["phred_quality"])
            if len(record) > 100 and statistics.mean(record.letter_annotations["phred_quality"]) > 14:
               sequence.append(record)
    quality_files(sequence)
    print("List is done!")

read_sequences(get_files(pass_path), pass_path)

def blast():
    for samples in SeqIO.parse("fail_map.fasta", "fasta"):
        print(samples.id)
        print(len(samples))
        result_handle = NCBIWWW.qblast("blastn", "nt", samples.seq)
    with open("fail_map.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()
#blast()




