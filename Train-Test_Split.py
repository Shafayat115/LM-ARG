
from enum import unique
from operator import index
import random




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
      
    
def get_seq(query_prot):
    flag = 0
    with open('/home/shafayat/Desktop/ARG_Language/arg_v5.fasta', 'r') as f:
        lines = f.readlines()
        prot = ''
        for line in lines:
            if flag:
                if line[0] != '>':
                    prot = prot + line
                else:
                    break
            if line[0] == '>':
                id = line[1]
                index = 2
                while line[index]!='|':
                    id = id + line[index]
                    index+=1
                if id==query_prot.strip():
                    flag = 1
                    
    return prot





                
args = {
    'aminoglycoside',
    'bacitracin',
    'beta_lactam',
    'chloramphenicol',
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

class Labels:
    name =''
    count = 0
    id = []
    def __init__(self, name,id):
        self.name = name
        self.id = id

All_Labels = []

for i in args:
    new_label = Labels(i,[])
    All_Labels.append(new_label)

with open('/home/shafayat/Desktop/ARG_Language/arg_v5.fasta', 'r') as f:
    lines = f.readlines()
    number_of_samples = [0]*14
    for line in lines:
        if line[0] == '>':
            index =1
            count = 0              
            while count !=3:
                index+=1
                if(line[index]=='|'):
                    count+=1
            index+=1
            label = ''
            while line[index]!='|':
                label= label+line[index]
                index+=1
            if (label in args):
                index =1
                label_id = ''
                while(line[index]!='|'):
                    label_id = label_id+line[index]
                    index+=1
                for y in All_Labels:                    
                    if(label==y.name):
                        #print(label, label_id)
                        (y.id).append(label_id)
                        y.count+=1
                        #print("y.name: ",y.name," y.id: ",len(y.id)," y.count: ",y.count)

for i in All_Labels:
    print("label name : ",i.name )
    # for j in (i.id):
    #     print("members : ",j)
    print("label count :",i.count)


for y in All_Labels:
    randomlist = random.sample(range(0, y.count), round(y.count*0.80))
    print("randomlist: ",randomlist)
    #randomtestlist = []
    with open('cross_validation_3_train.fasta','a') as file1:
        with open('cross_validation_3_test.fasta','a') as file2:
            for x in range(y.count):
                if x in randomlist:
                    file1.write('>'+y.id[x]+'|'+y.name+'\n'+get_seq(y.id[x]))
                else:
                    file2.write('>'+y.id[x]+'|'+y.name+'\n'+get_seq(y.id[x]))
                    #randomtestlist.append(x)
    #print("randomtestlist : ",randomtestlist)

                