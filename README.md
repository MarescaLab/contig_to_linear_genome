# contig_to_linear_genome

# OVERVIEW
These scripts are used in the process of converting a complete and circular contig to a genome whose annotation starts with dnaA. 

Scripts are specifically used to:

  trim_fasta.py:               Convert a complete and circular contig with overlap to a linear sequence.
  rearrange_genome_dnaA.py:    Rearrange a linear genome sequence to begin with dnaA as the first CDS annotated
 
 
# NOTE
These scripts do NOT run annotation software. They are for those fiddly steps in between running annotation software.


# STEP-BY-STEP PROCESS SCRIPTS SHOULD BE USED IN
1. Obtain .fasta file containing contig.
2. Determine that contig is circular and at which bp location you want to trim the sequence. Recommend using Gepard for this. 
3. Trim the sequence by running trim_fasta.py.
4. Run your favorite annotation program that generates a .gbk file. 
5. Confirm that dnaA is NOT the first CDS in the annotation.
6. Determine how many bp upstream of dnaA should be the start of the rearranged genome. 
7. Rearrange the genome by running rearrange_genome_dnaA.py.
8. Re-run your favorite annotation program.


# COMMANDS TO RUN SCRIPTS
Both scripts MUST take in two arguments as shown below:  

python trim_fasta.py [.fasta file] [integer]

First argument should be a (.fasta) file containing the complete circular contig. File should have only one fasta sequence in it. 
Second argument should be an integer that is the bp location the sequence should be trimmed at to make the linear representation of the genome.



python rearrange_genome_dnaA.py [.gbk file] [integer]

First argument is a genbank (.gbk) file from your first annotation run that does not start with the dnaA gene as the first CDS. 
Second argument should be an integer that is the number of bp upstream from the dnaA start position that you want in the rearranged representation of the genome. This will be where the rearranged linear representation of the genome starts. 




