Directory contains all the scripts and data necessary to identify the set of Highly Expressed Genes and concatenated CoDing Sequences
and HEGs into a single fasta file.

For this, it is necessary to create a conda environment
#conda create -y -n codBias
#conda activate codBias

Packages in environmnet:
biopython	1.79
pandas	1.4.1
diamond	2.0.14

Files and directories:
list.txt	list containing the id of all the genomes from the WoL database
extract_hegs.py	script to extract the set of highly expressed genes (heg) for each genome. Modified from Dehlinger et al (2021) (https://doi.org/10.1099/mgen.0.000663)
testDB.dmnd	diamond database with representatives of 40 HEGs described by Sharp et al (2005) (https://doi.org/10.1093/nar/gki242)
hegs/	directory containing the hegs for each genome. Reproducible using the script "extract_hegs.py" and cds directory.
cds/	directory containing the cds of each genome. Available from the Web of Life project (https://biocore.github.io/wol/)

