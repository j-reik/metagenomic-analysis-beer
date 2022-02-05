import Bio
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np
import os 

length_fail = []
quality_fail = []
length_pass = []
quality_pass = []
pass_path = '/u/home/praktikum/Praktikum012019/fastq_pass/'
fail_path = '/u/home/praktikum/Praktikum012019/fastq_fail/'
beer_type = 'Waldbier2'

def get_files(path):
    files = []
    dirs = os.listdir(path + beer_type + "/")
    for filenames in dirs:
        if filenames.endswith(".fastq"):
             files.append(filenames)
    return files  

def read_sequences(filenames_fail, filenames_pass, path_fail, path_pass):
    for n in range(len(filenames_fail)):
        for record in SeqIO.parse(path_fail + beer_type + "/" + filenames_fail[n], "fastq"):
            length_fail.append(len(record))
            quality_fail.append(record.letter_annotations["phred_quality"])
    for n in range(len(filenames_pass)):
        for record in SeqIO.parse(path_pass + beer_type + "/" + filenames_pass[n], "fastq"):
            length_pass.append(len(record))
            quality_pass.append(record.letter_annotations["phred_quality"])
    print("List is done!")

def quality_histogram(quality_list1, quality_list2, n_bins = 0, data1_name="Fail Sequences", data1_color="#539caf", data2_name="Pass Sequences", data2_color="#7663b0", x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    mean_data1 = []
    mean_data2 = []
    for n in range(len(quality_list1)):
        mean_data1.append(np.mean(quality_list1[n]))
    for m in range(len(quality_list2)):
        mean_data2.append(np.mean(quality_list2[m]))
    
    max_nbins = 50
    data_range = [min(min(mean_data1), min(mean_data2)), max(max(mean_data1), max(mean_data2))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins


    if n_bins == 0:
    	bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    else: 
    	bins = n_bins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(mean_data1, bins = bins, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(mean_data2, bins = bins, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')
    plt.savefig("Quality_" + beer_type + ".png")
    plt.show()

def length_histogram(x, y, n_bins = 0, data1_name="Fail Sequences", data1_color="#539caf", data2_name="Pass Sequences", data2_color="#7663b0", x_label="", y_label="", title=""):
    # Set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 50
    data_range = [min(min(x), min(y)), max(max(x), max(y))]
    binwidth = (data_range[1] - data_range[0]) / max_nbins


    if n_bins == 0:
    	bins = np.arange(data_range[0], data_range[1] + binwidth, binwidth)
    else: 
    	bins = n_bins

    # Create the plot
    _, ax = plt.subplots()
    ax.hist(x, bins = bins, color = data1_color, alpha = 1, label = data1_name)
    ax.hist(y, bins = bins, color = data2_color, alpha = 0.75, label = data2_name)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.legend(loc = 'best')
    plt.savefig("Length_" + beer_type + ".png")
    plt.show()

def length_quality(quality_list1, length_list1, quality_list2, length_list2, x_label="", y_label="", title="", color = "r", yscale_log=False):
    _, ax = plt.subplots()

    mean_data1 = []
    for n in range(len(quality_list1)):
        mean_data1.append(np.mean(quality_list1[n]))
    mean_data2 = []
    for n in range(len(quality_list2)):
        mean_data2.append(np.mean(quality_list2[n]))

    ax.scatter(mean_data1, length_list1, s = 10, color = "#539caf", alpha = 1)
    ax.scatter(mean_data2, length_list2, s = 10, color = "#7663b0", alpha = 0.50)

    if yscale_log == True:
        ax.set_yscale('log')
    
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.savefig("Length_Mix_" + beer_type + ".png")
    plt.show()

read_sequences(get_files(fail_path), get_files(pass_path), fail_path, pass_path)
#Fail/Pass overlaid histogram (Read length)
length_histogram(length_fail, length_pass)
quality_histogram(quality_fail, quality_pass)
length_quality(quality_fail, length_fail, quality_pass, length_pass)

