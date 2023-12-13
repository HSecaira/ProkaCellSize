#!/usr/bin/env python3

import os
from Bio import SeqIO
import pandas as pd
import subprocess
import numpy as np

def get_hegs_to_forty_items(fIn_cds, fIn, file):
    df = pd.read_table(fIn, names=["Subject", "Bit", "SeqID"], skipinitialspace=True)
    df = df.replace('\[.*\]', '', regex=True)
    df["Subject"] = df["Subject"].str.strip()
    df["Subject"] = df["Subject"].apply(lambda x: ' '.join(x.split(' ')[1:]))
    df["Subject"] = df["Subject"].str.lower()
    df = df.replace("elongation factor ef-2", "elongation factor g")
    df2 = df.sort_values(["Subject", "Bit"], ascending=[True,False])
    df2 = df2.loc[df2.groupby('Subject')["Bit"].idxmax()].reset_index(drop=True)
    items = df2.SeqID.unique()

    newSeqs = []
    for seq_record in SeqIO.parse(fIn_cds, "fasta"):
        if (seq_record.id in items):
            newSeqs.append(seq_record)

    if len(newSeqs) < 38:
        print(f"\tWARNING there are less than 38 sequences. Sequences: {len(newSeqs)}")
    
    print(f'\tWritting output to {file.split("/")[-1]}...')
    with open(file, "w") as handle:
        #SeqIO.write(newSeqs, handle, "fasta")
        for s in newSeqs:
            handle.write('>' + s.id + '\n' + str(s.seq) + '\n')

    subprocess.run(["rm", fIn])

    return len(newSeqs)

def get_hegs(fIn, fOut):
    #subprocess.call(["diamond", "blastx", "-d", "testDB", "-q", fIn, "-o", fIn.split('/')[-1] + ".matches", "-f", "6", "stitle", "bitscore", "qseqid", "-k", "1"])
    print(f'\tSearching HEGs...')
    dim = subprocess.run(["diamond", "blastx", "-d", "testDB", "-q", fIn, "-o", fOut, "-f", "6", "stitle", "bitscore", "qseqid", "-k", "1"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)


# Path variables
input = '/mnt/store0/CellSize/analysis/CellSize/codBias/cds/temp'
output = '/mnt/store0/CellSize/analysis/CellSize/codBias/hegs'

# Main
#genomes = ['G000005825', 'G000006175', 'G000006605', 'G000006725', 'G000006745']
wd = '/mnt/store0/CellSize/analysis/CellSize/codBias'
list = os.path.join(wd, 'list.txt')
genomes = np.loadtxt(list, dtype = 'str')

for g in genomes:
	print(f'Genome: {g}')
	fIn = os.path.join(input, g + '.ffn')
	fOut = os.path.join(output, g + '.matches')
	# Execute diamond
	get_hegs(fIn, fOut)
	# Get HEGs
	fOut1 = os.path.join(output, g + '.heg')
	get_hegs_to_forty_items(fIn, fOut, fOut1)



