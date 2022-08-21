from Bio import SeqIO
from Bio.Seq import Seq
def read_fasta(file):

    # dictionary contains seq_id as keys and protein seqs as values
    seq_dict = {}
    for sequence in SeqIO.parse(file, "fasta"):

        prot_description = str(sequence.description)
        this_prot_id = prot_description.split('|')[0]

        prot = str(sequence.seq)
        prot = prot.replace('U','X').replace('Z','X').replace('O','X')

        seq_dict[this_prot_id] = prot
        
    return seq_dict 

file = '/home/shafayat/Desktop/arg_v5_40_seq.fasta'
print(read_fasta(file))
