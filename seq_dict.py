from Bio import SeqIO

index_of_args = {
    'aminoglycoside': 0,
    'bacitracin': 1,
    'beta_lactam': 2,
    'chloramphenicol': 3,
    'fosfomycin': 4,
    'glycopeptide': 5,
    'multidrug': 6,
    'polymyxin': 7,
    'quinolone': 8,
    'rifampin': 9,
    'sulfonamide': 10,
    'tetracycline': 11,
    'trimethoprim': 12,
    'macrolide-lincosamide-streptogramin': 13,
    'others': 14
}

AMINO_ACID_VOCABULARY_with_index = {
    'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14,'S':15, 'T':16, 'V':17, 'W':18, 'Y':19
}
def create_lablels_of_protein_seq(args):
    '''
    argument metals can be like Zinc (Zn), Copper (Cu) i.e., csv
    '''
    label = [0] * 15 # there are 23 types of metals in BacMet DB
    arg_list = args.split(',')
    for i in arg_list:
        label[index_of_args[i.strip()]] = 1
    
    return label

def read_fasta(file):
    
    # dictionary contains seq_id as keys and protein seqs as values
    seq_dict = {}
    for sequence in SeqIO.parse(file, "fasta"):

        prot_description = str(sequence.description)
        this_prot_id = prot_description.split('|')[0]

        this_prot_label = prot_description.split('|')[-1]
        
        seq_dict[this_prot_id] = create_lablels_of_protein_seq(this_prot_label)
        
    return seq_dict

seq_path ='/home/shafayat/Desktop/arg_v5_40_seq_with_label_others.fasta'
gene_id_label_dict = read_fasta(seq_path)

print(gene_id_label_dict)
