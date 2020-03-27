from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC 
import sys

####Import fasta file containing circular genome####
input_fasta = sys.argv[1]
genome = SeqIO.parse(open(input_fasta), 'fasta')

####Import position where sequence should be trimmed####
input_position = int(sys.argv[2])

##Make output fasta file for linear sequence##
output = open("linear_genome.fasta", "w")

##Trim the sequence##
for record in genome:
	record.seq = record.seq[0:input_position]

##Write new seqeunce to outputfile##
SeqIO.write(record, output, 'fasta')




