# Team1-ComparativeGenomics

**Team Members**: Laura Mora, Heather Patrick, Lawrence McKinney, Kenji Gerhardt, Hira Anis, Manasa Vegesna 

# Comparative Genomics Pipeline

This pipeline performs various comparative genomics techniques on E.coli isolates using ANI, MLST and SNP-based approaches to determine the outbreak cluster. 

## Tools Used:

## ANI - Approach
	
#### MUMmer4.0:	
   * A open source bioinformatic tool used align and compare entire genomes at varying evolutionary distances.
   * MUMmer efficiently locates maximal unique matches between two sequences using a suffix tree data structure.
   * MUMmer is a modular design comprising of many various utilities and scripts.
   * There must be exactly one reference file and at least one query file.
     1. Use Case - Aligning two draft sequences
         * Command line syntax: nucmer [options] <ref.fasta> <query.fasta>
     2. Use Case - Report alignment statistics; ANI
         * Command line syntax: dnadiff  [options]  <reference>  <query> or dnadiff  [options]  -d <delta file>
   
## MLST Approach

#### ChewBBACA:	
   * chewBBACA is a comprehensive pipeline including a set of functions for the creation and validation of whole genome and core genome MultiLocus Sequence Typing (wg/cgMLST) schemas, providing an allele calling algorithm based on Blast Score Ratio that can be run in multiprocessor settings.
     * Input: directory with assembled genomes
     * Output: wgMLST and cgMLST schemas
   * Grapetree is used to create a Newick tree for later visualization and must be installed prior to running the pipeline (see [Requirements](#Requirements)).
     * Input: cgMLST schema
     * Output: Newick tree file (cgMLST.tree)	
   
## SNP Approach

#### kSNP:
   * kSNP3 is a program that identifies the pan-genome SNPs in a set of genome sequences, and estimates
phylogenetic trees based upon those SNPs. 
   * Version: 3.0
   * Input: A text file (.txt) containing the location(directory path) of the fasta files and the genome IDs.
   * Output: SNPs identified and phylogenetic tree (newick format) files
   * Parameters: - k : mention k-mer size 
		 - p : builds a phylogenetic tree using the Parsimony method from the identified SNPs
		 - ml : builds a phylogenetic tree using the Maximum-Likelihood method from the identified SNPs
		 - nj : builds a phylogenetic tree usin the Neighbor-Joining method from the identified SNPs

#### FigTree:
   * FigTree is a phylogenetic tree drawing and visualization tool. 
   * Version: 1.4.4
   * Input: Newick Format (.tre) files from kSNP output
   * Output: PDF file of the choosen phylogenetic tree

## Usage:
```
./cg_pipeline.py -i <dir_path> -o <dir_name> [-c <int>] -t <m|c|k|a> [-h]
    -i,--input     full path to directory containing assembled genomes
    -o,--output    path to output directory
    -c,--cpu       number of cpus
    -t,--tool      tool of choice: MUMmer (m), chewBBACA (c), kSNP3 (k), all (a)
    -h             print usage information    
```

## Requirements:
This pipeline assumes all tools (MUMmer, chewBBACA, Grapetree, and kSNP3) and their dependencies have already been installed.
1. [MUMmer](http://mummer.sourceforge.net/)
2. [chewBBACA](https://github.com/B-UMMI/chewBBACA) 
3. [Grapetree](https://github.com/achtman-lab/GrapeTree)
4. [kSNP3](https://sourceforge.net/projects/ksnp/)
5. [FigTree](http://tree.bio.ed.ac.uk/software/figtree/)

## Citations:

1) Kurtz, S., Phillippy, A., Delcher, A. L., Smoot, M., Shumway, M., Antonescu, C., & Salzberg, S. L. (2004). Versatile and open software for comparing large genomes. Genome biology, 5(2), R12.
2) Silva, M., Machado, M. P., Silva, D. N., Rossi, M., Moran-Gilad, J., Santos, S., ... & Carrico, J. A. (2018). chewBBACA: A complete suite for gene-by-gene schema creation and strain identification. Microbial genomics, 4(3).
3) Gardner, S. N., Slezak, T., & Hall, B. G. (2015). kSNP3. 0: SNP detection and phylogenetic analysis of genomes without genome alignment or reference genome. Bioinformatics, 31(17), 2877-2878.
4) Z Zhou, NF Alikhan, MJ Sergeant, N Luhmann, C Vaz, AP Francisco, JA Carrico, M Achtman (2018) "GrapeTree: Visualization of core genomic relationships among 100,000 bacterial pathogens", Genome Res; doi: https://doi.org/10.1101/gr.232397.117
5) Rambaut, A. (2007). FigTree, a graphical viewer of phylogenetic trees.
