# Dataset

This directory contains information on **cell size**, **taxonomy**, and **genome properties** for 5,380 bacterial and archaeal species.

## Columns description
* `taxid`	[NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi) identifier.
* `lenght`	Values for cell length in $\mu m$
* `width`	Values for cell width in $\mu m$
* `volume`	Values for cell volume in $\mu m$ calculated using the formula for a [capsule](https://en.wikipedia.org/wiki/Capsule_(geometry)). See also `preprocess` for further details.
* `surface`	Values for cell surface in $\mu m$ calculated using the formula for a [capsule](https://en.wikipedia.org/wiki/Capsule_(geometry)). See also `preprocess for further details.
* `svratio`	Values for cell surface-to-volume ratio in $\mu m$.
* `vsratio`	Values for cell volume-to-surface ratio in $\mu m$.
* `log_vsratio`	Values for cell volume-to-surface ratio log-transformed using $\text{log}_{10}$.
* `species`	Species name according to NCBI taxonomy.
* `genus`	Genus name according to NCBI taxonomy.
* `family`	Family name according to NCBI taxonomy.
* `order`	Order name according to NCBI taxonomy.
* `class`	Class name according to NCBI taxonomy.
* `phylum`	Phylum name according to NCBI taxonomy.
* `kingdom`	Kingdom name according to NCBI taxonomy.
* `genome`	Web of Life [(WoL)](https://biocore.github.io/wol/data/genomes/) genome identifier. If empty, species cannot be linked to a genome present in WoL.
* `genome_size`	Genome size (base pairs) according to metadata from WoL.
* `gc`	Proportion of G and C in genome according to metadata from WoL.
* `proteins`	Number of proteins in genome according to metadata from WoL.
* `coding`	Proportion of coding sequences in genome according to metadata from WoL.
* `rrnas`	Number of 16S rRNA genes in genomes according to metadata from WoL.
* `ENCprime`	Codon usage bias calculated using the ENC\' metric as shown in [Vieira-Silva, et al. 2010.](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1000808).
