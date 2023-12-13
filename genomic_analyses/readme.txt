Directory containing the notebooks and files for genomic analyses and to generate Figure S8, Figure S9 and Table S10

Files and directories:

cell_size_genomic.ipynb Notebook with code to test for correlation between cell size and photosynthesis, rubisco, chemotaxis, and flagellar movement
cell_size_genomic_no_cyanos.ipynb	Notebook with code to test for correlation between cell size and photosynthesis, rubisco, chemotaxis, and flagellar movement excluding cyanobacteria
cell_size_genomic_pathways.ipynb	Notebook with code to test for correlation between cell size and KEGG pathways
function/	Directory containing KEGG annotations of the genomes from the Web of Life (http://ftp.microbio.me/pub/wol2/).
		To generate input file for `cell_size_genomic_pathways.ipynb`. Download all the protein sequences (all.faa.xz; http://ftp.microbio.me/pub/wol2/proteins/)
		and use grep (grep -f orf-to-ko_genome_genomic_information -A 1 all.faa > all_genomes_genomic_information.faa).
			
kegg_lregress/	Directory containing output from cell_size_genomic_pathways.ipynb


