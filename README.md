# Team1-ComparativeGenomics

**Team Members**: Laura Mora, Heather Patrick, Lawrence McKinney, Kenji Gerhardt, Hira Anis, Manasa Vegesna 

# Comparative Genomics Pipeline

This pipeline performs various comparative genomics techniques on the 50 E.coli isolates using ANI, MLST and SNP-based approaches to determine the outbreak cluster. 

## Tools Used:

## ANI - Approach
	
#### MUMmer:	
   * A bioinformatic tool used align and compare entire genomes at varying evolutionary distances.
   
## MLST Approach

#### ChewBBACA:	
   * chewBBACA is a comprehensive pipeline including a set of functions for the creation and validation of whole genome and core genome MultiLocus Sequence Typing (wg/cgMLST) schemas, providing an allele calling algorithm based on Blast Score Ratio that can be run in multiprocessor settings.
   * Grapetree is used to create a Newick tree and must be installed prior to running pipeline.	
   
## SNP Approach

#### kSNP:
   * kSNP3 is a program that identifies the pan-genome SNPs in a set of genome sequences, and estimates
phylogenetic trees based upon those SNPs. 
   * Version: 3.0

### Usage:
Note: this pipeline assumes all tools (MUMmer, chewBBACA, and kSNP3) have already been installed.
```
./cg_pipeline.py -i <dir_path> -o <dir_name> [-c <int>] -p <file_path> [-h]
    -i,--input    path to directory containing assembled genomes
    -o,--output    path to output directory
    -c,--cpu    number of cpus
    -p,--ptf    path of prodigal training prodigal training file for genome species
    -h    print usage information    
```

### Requirements:

### Citations:

1) Kurtz, S., Phillippy, A., Delcher, A. L., Smoot, M., Shumway, M., Antonescu, C., & Salzberg, S. L. (2004). Versatile and open software for comparing large genomes. Genome biology, 5(2), R12.
2) Silva, M., Machado, M. P., Silva, D. N., Rossi, M., Moran-Gilad, J., Santos, S., ... & Carrico, J. A. (2018). chewBBACA: A complete suite for gene-by-gene schema creation and strain identification. Microbial genomics, 4(3).
3) Gardner, S. N., Slezak, T., & Hall, B. G. (2015). kSNP3. 0: SNP detection and phylogenetic analysis of genomes without genome alignment or reference genome. Bioinformatics, 31(17), 2877-2878.
4) Z Zhou, NF Alikhan, MJ Sergeant, N Luhmann, C Vaz, AP Francisco, JA Carrico, M Achtman (2018) "GrapeTree: Visualization of core genomic relationships among 100,000 bacterial pathogens", Genome Res; doi: https://doi.org/10.1101/gr.232397.117
