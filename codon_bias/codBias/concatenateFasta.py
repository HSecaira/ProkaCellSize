#!/usr/bin/env python3

'''
Script that finds the number of modules per replicate and performs
hierarchical clustering over similarity matrices
'''

# Some imports
import os, sys
import timeit
import timeit

#################################################################################################

# Functions 

def executionTime(start, stop):
	'''
	Function that calculates the execution time.
	Inputs:
		start: float indicating the starting time in seconds
		stop: float indicating the stop time in seconds
	Outputs:
		None
	'''

	# Calculate execution time
	total_time = stop - start
	# Output in a nice format
	mins, secs = divmod(total_time, 60)
	hours, mins = divmod(mins, 60)
	print(f'Running time: {hours} h, {mins} mins, {secs} seconds')

def concatenateFasta(fIn):
	'''
	Function that concatenates a fasta file with multiple sequence into one
	Inputs:
		fIn: fasta file containing multiple sequences with headers
	Outputs:
		seq: str containing the concatenated sequence
	'''

	# Declare structures
	seq = ''
	
	# Iterate over file
	with open(fIn, 'r') as f:
		for line in f:
			if line[0] != '>':
				seq += line.strip()

	return seq

def writeFasta(seqs, fOut):
	'''
	Function that writes a Fasta file for a set of sequences
	Inputs:
		seqs: dictionary containing the headers (keys) and sequences (values)
		fOut: str containing the name of the output file
	Outputs:
		None
	'''

	with open(fOut, 'w') as f:
		for head, seq in seqs.items():
			f.write(f'>{head}\n{seq}\n')

def loadList(fIn):
	'''
	Function that loads a list of str into
	Inputs:
		fIn: str containing the file name
	Outputs:
		genomes: list of str cotaining the genomes
	'''

	# Declare structure
	genomes = []

	with open(fIn, 'r') as f:
		for line in f:
			genomes.append(line.strip())

	return genomes

#################################################################################################

# Define paths
dataPathIn = '/mnt/store0/CellSize/analysis/CellSize/codBias/'

#################################################################################################

# Start execution time
start = timeit.default_timer()

# Load genomes
fIn_genomes = os.path.join(dataPathIn, 'list.txt')
genomes = loadList(fIn_genomes)

# Concatenate and save fasta
for genome in genomes:
	print(f'Genome: {genome}')

	fIn_cds = os.path.join(dataPathIn, f'cds/temp/{genome}.ffn')
	fIn_hegs = os.path.join(dataPathIn, f'hegs/{genome}.heg')
	fOut = os.path.join(dataPathIn, f'concatenated/{genome}.fa')

	# Concatenate fasta
	seq_cds = concatenateFasta(fIn_cds)
	seq_hegs = concatenateFasta(fIn_hegs)
	seqs = {genome: seq_cds, 'hegs': seq_hegs}
	# Save fasta
	writeFasta(seqs, fOut)

# Get execution time
stop = timeit.default_timer()
executionTime(start, stop)














