from Bio import SeqIO 
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC, generic_dna
from Bio import SeqFeature
from Bio.SeqFeature import FeatureLocation
import sys

###Import Genbank file###
input_gbk = sys.argv[1]
gbk = SeqIO.parse(open(input_gbk), 'genbank')

###Import trimming location###
upstream_bp = int(sys.argv[2])

for record in gbk:
###Get the fasta sequence###
	genome_seq = record.seq
	for item in record.features:
		if item.type == "CDS" and "gene" in item.qualifiers: 
			if item.qualifiers["gene"][0] == "dnaA" or item.qualifiers["gene"][0] == "dnaA_1": ## Find dnaA
				if item.strand == -1: ## dnaA is on the reverse strand reverse/complement 
					
					rev_comp_genome_seq=genome_seq.reverse_complement() ## Take the complement and reverse
					###renumber
					
					#get dnaA start and stop positions
					dnaA_start = int(item.location.start)
					dnaA_end = int(item.location.end)
					
					#calculate trimming location on reverse complement
					end_pos = len(genome_seq)-1
					new_dnaA_start=end_pos-dnaA_end
					trim_location=new_dnaA_start-upstream_bp ##35bp upstream 
					
					#rearrange the reverse complement sequence so dnaA will be first in annotation re-run
					front_seq=rev_comp_genome_seq[0:trim_location]
					back_seq = rev_comp_genome_seq[trim_location+1:]
					rearranged_seq=back_seq+front_seq
					
					##Make output fasta file for linear sequence##
					output = open("%s_linear_genome_rvrs_cmplmnt_renum.fasta" % (input_gbk[0:len(input_gbk)-4]), "w")
					
					###Write new seqeunce to outputfile##
					new_record = SeqRecord(rearranged_seq, "Linear reverse complement of genome rearranged such that dnaA is the first gene annotated.")
					SeqIO.write(new_record, output, 'fasta')
					
					
				elif item.strand == 1: ## dnaA in on the forward strand
					##renumber
					
					#get dnaA start and stop positions
					dnaA_start = int(item.location.start)
					dnaA_end = int(item.location.end)

					#calculate trimming location
					trim_location = dnaA_start-upstream_bp
					
					#rearrange the reverse complement sequence so dnaA will be first in annotation re-run
					front_seq=genome_seq[0:trim_location]
					back_seq =genome_seq[trim_location+1:]
					rearranged_seq=back_seq+front_seq
					
					##Make output fasta file for linear sequence##
					output = open("%s_linear_genome_renum.fasta" % (input_gbk[0:len(input_gbk)-4]), "w")
										
					###Write new seqeunce to outputfile##
					new_record = SeqRecord(rearranged_seq, "Linear represenation of genome rearranged such that dnaA is the first gene annotated.")
					SeqIO.write(new_record, output, 'fasta')