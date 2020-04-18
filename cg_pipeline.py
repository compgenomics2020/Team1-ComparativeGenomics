#!/bin/env python3
import argparse
import subprocess
import os

def chewBBACA(input_genomes,output_dir, cpu):
    '''Creates a wgMLST and cgMLST schema as well as a Newick tree of the cgMLST
       Input: 
            input_genomes = directory where complete or draft genomes are located
            output_dir = directory for output
            cpu = Number of cpus
    '''
    os.chdir(output_dir)
    # Get training file
    if not os.path.isfile(output_dir+"prodigal_training_files/Escherichia_coli.trn"):
        subprocess.run("git clone https://github.com/mickaelsilva/prodigal_training_files", shell = True)

    # wgMLST Schema Creation
    wg = "chewBBACA.py CreateSchema -i " + input_genomes + " --cpu " + str(cpu) + " -o "+ output_dir +"Schema --ptf " + output_dir + "prodigal_training_files/Escherichia_coli.trn"
    #print(wg.split())
    subprocess.run(wg.split())

    # Allele Calling
    allele = "chewBBACA.py AlleleCall -i " + input_genomes + " -g Schema/ -o "+ output_dir +"results_allele --cpu "+str(cpu)+" --ptf prodigal_training_files/Escherichia_coli.trn"
    #print(allele.split())
    subprocess.run(allele.split())

    # Define cgMLST schema
    date = subprocess.check_output("ls -t results_allele/ | head -n1", shell = True)
    date = str(date,'utf-8').rstrip()
    #print(date)
    cg = "chewBBACA.py ExtractCgMLST -i results_allele/"+ date +"/results_alleles.tsv -o " + output_dir +"cgMLST/ -r " + output_dir + "results_allele/" + date + "/RepeatedLoci.txt -p 0.95"
    #print(cg)
    subprocess.run(cg.split())

    # Create Newick Tree
    grapetree = "grapetree --profile " + output_dir + "cgMLST/cgMLST.tsv > cgMLST.tree"
    #print(grapetree)
    subprocess.run(grapetree, shell = True)

    return None

def collect_assembled_genomes():
    pathToInputFiles = "/home/projects/group-a/Team1-GenomeAssembly/assembled_output/"
    input_files = os.listdir(pathToInputFiles)
    base_names = []
    cleaned_files = []
    for file in input_files:
        if file.endswith(".fasta"):
            base_names.append(file)
            cleaned_files.append(pathToInputFiles+file)
    return(base_names, cleaned_files)

def MUMmer(prefix, reference_file, query_file):
    nucmer_command = ["nucmer", "-p", "prefix", reference_file, query_file]
    delta_file = prefix+".delta"	
    dnaff_command = ["dnaff", "-p", "-d", delta_file]
    subprocess.call(nucmer_command)
    subprocess.call(dnaff_command)	
    return(delta_file)

def kSNP():

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
    parser.add_argument("-t", "--tool", help="Tool of choice: MUMmer (m), chewBBACA (c), kSNP (k), or all (a)", choices = ['m', 'c', 'k', 'a'], required = True)
    args = parser.parse_args()

    output = args.output
    if output[-1] != "/":
        output += "/"
   
    #call MUMmer
    names, mummer_inputs = collect_assembled_genomes()
    reference = mummer_inputs[1]
	
    for i in range(0, len(mummer_inputs)):
        prefix = names[i][0:7]
        MUMmer(prefix, reference, mummer_inputs[i])

    #call chewBBACA
    if args.tool == 'c' or args.tool == 'a':
        chewBBACA(args.input, output, args.cpu)

    #call kSNP

    #analysis or visualization -- if we're including it here

if __name__ == "__main__":
    main()
