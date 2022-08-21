
from enum import unique


index_of_args = {
    'aminoglycoside','bacitracin','beta_lactam','chloramphenicol',
    'fosfomycin',
    'glycopeptide',
    'multidrug',
    'polymyxin',
    'quinolone',
    'rifampin',
    'sulfonamide',
    'tetracycline',
    'trimethoprim',
    'macrolide-lincosamide-streptogramin'}
AMINO_ACID_VOCABULARY_with_index = {
    'A':0, 'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'H':6, 'I':7, 'K':8, 'L':9, 'M':10, 'N':11, 'P':12, 'Q':13, 'R':14,'S':15, 'T':16, 'V':17, 'W':18, 'Y':19
}


def unique(list1):
      
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    new_labels =[]
    for x in unique_list:
        new_labels.append(x)
    return new_labels
      
def number_of_labels(file):
    
        with open(file, 'r') as f:
            lines = f.readlines()
            number_of_samples = [0]*33
            for line in lines:
                if line[0] == '>':
                    #print("here one")
                    index =1
                    count = 0              
                    while count !=3:
                        index+=1
                        #print("here two : ",index)
                        #print(line[index])
                        if(line[index]=='|'):
                            count+=1
                    index+=1
                    label = ''
                    while line[index]!='|':
                        label= label+line[index]
                        index+=1
                    #print("here three : ",label)
                    if (label in new_list):
                        #print("here four : ",new_list.index(label))
                        number_of_samples[new_list.index(label)]+=1
            print(new_list)
            return number_of_samples


#219 elements across 19 class

#print(read_id('/home/shafayat/Desktop/ARG_Language/CD-HIT_40/arg_v5_40_sorted.clstr'))

list_of_new_labels =['qa_compound', 'qa_compound', 'qa_compound', 'qa_compound', 'qa_compound', 'qa_compound', 'qa_compound', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'kasugamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'elfamycin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'nitroimidazole', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'aminocoumarin', 'fosmidomycin', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'fosmidomycin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'tetracenomycin', 'bleomycin', 'bleomycin', 'bleomycin', 'bleomycin', 'bleomycin', 'bleomycin', 'thiostrepton', 'thiostrepton', 'thiostrepton', 'thiostrepton', 'thiostrepton', 'qa_compound', 'qa_compound', 'qa_compound', 'qa_compound', 'qa_compound', 'ethambutol', 'ethambutol', 'streptothricin', 'peptide', 'peptide', 'bleomycin', 'peptide', 'peptide', 'peptide', 'peptide', 'streptothricin', 'streptothricin', 'streptothricin', 'fusidic_acid', 'fusidic_acid', 'fusidic_acid', 'tunicamycin', 'tunicamycin', 'tunicamycin', 'fosmidomycin', 'pleuromutilin', 'pleuromutilin', 'elfamycin', 'elfamycin', 'qa_compound', 'qa_compound', 'peptide', 'peptide', 'mupirocin', 'mupirocin', 'mupirocin', 'mupirocin', 'peptide', 'peptide', 'triclosan', 'triclosan', 'isoniazid', 'aminocoumarin', 'kasugamycin', 'kasugamycin', 'peptide', 'peptide', 'streptothricin', 'mupirocin', 'triclosan', 'peptide', 'peptide', 'fusidic_acid', 'peptide', 'peptide', 'puromycin', 'peptide', 'triclosan', 'isoniazid', 'triclosan', 'pleuromutilin', 'isoniazid', 'triclosan', 'aminocoumarin', 'ethambutol', 'aminocoumarin', 'isoniazid', 'puromycin', 'ethambutol', 'peptide', 'isoniazid', 'peptide', 'peptide']
new_list = unique(list_of_new_labels)
#final_labels = list(new_list)+index_of_args

for x in index_of_args:
        new_list.append(x)
#print(new_list)
print(number_of_labels('/home/shafayat/Desktop/ARG_Language/arg_v5.fasta'))




                