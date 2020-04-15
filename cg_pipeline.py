#!/bin/env python3
import argparse
import subprocess

def MUMmer:

    return None

def chewBBACA(input_genomes,output_dir, cpu, prodigal = "prodigal_training_files/Escherichia_coli.trn"):
    '''Creates a wgMLST and cgMLST schema as well as a Newcik tree of the cgMLST
       Input: 
            input_genomes = directory where complete or draft genomes are located
            output_dir = directory for output
            cpu = Number of cpus
            prodigal = prodigal training file for genome species
    '''
    # wgMLST Schema Creation
    subprocess.run("chewBBACA.py CreateSchema -i " + input_genomest + " --cpu" + cpu + " -o "+output_dir+"Schema --ptf " + prodigal, shell = True)
    # Allele Calling
    subprocess.run("chewBBACA.py AlleleCall -i " + input_genomest + " -g schema/ -o "+output_dir+"results_allele --cpu "+cpu+" --ptf "+ prodigal, shell = True)
    # Define cgMLST schema
    date = subprocess.run("ls -t results_allele/ | head -n1", shell = True)
    subprocess.run("chewBBACA.py ExtractCgMLST -i results_allele/"+date+"/results_alleles.tsv -o "+output_dir+"cgMLST/ -r "+outputdir+"results_allele/"+date+"/RepeatedLoci.txt -p 0.95", shell = True)
    # Create Newick Tree
    subprocess.run("grapetree "+output_dir+"cgMLST/cgMLST.tsv > cgMLST.tree", shell = True)
    return None

def kSNP:

    ### kSNP should be on your path
    ### Input: assembled Reads

    ### options

    ## if parsimony

    ## if maximum likelihood

    ## if neighbour-joining

    ## getting the required input files

    pathToInputFiles = "/home/projects/group-a/Team1-GenomeAssembly/assembled_output/"
    input_files_command = 'ls '+ path_to_gpresults + '*.fasta'
    input_files = subprocess.check_output(input_files_command,shell=True)
    input_files = input_files.split('\n')

    #### creating an input fasta file for kSNP:

    ## running Kchooser

    #### running kSNP

    return None

def main():

    #get options using os or argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="directory for input genomes", required = True)
    parser.add_argument("-o", "--output", help="name of output directory", required = True)
    parser.add_argument("-c", "--cpu", help="Number of cpus to use", default = 6)
    parser.add_argument("-p", "--ptf", help = "Prodigal training file for chewBBACA; has extension *.ptf")
    args = parser.parse_args()

    output = args.output
    if output[-1] != "/":
        output += "/"
   
     #call MUMmer

    #call chewBBACA
    if args.ptf:
        chewBBACA(args.input,output, args.cpu, args.ptf)
    else:
        chewBBACA(args.input,output, args.cpu))

    #call kSNP

    #analysis or visualization -- if we're inclusing it here

if __name__ == "__main__":
    main()
