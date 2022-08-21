from calendar import c


def get_seq(query_prot):
    #print(query_prot)
    flag = 0
    with open('/home/shafayat/Desktop/ARG_Language/arg_v5_test.fasta', 'r') as f:
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
                #print(query_prot.strip())
                #print(id)
                if id==query_prot.strip():
                    flag = 1
                    
    return prot

def get_label(query_prot):
    #print(query_prot)
    with open('/home/shafayat/Desktop/ARG_Language/arg_v5_test.fasta', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == '>':
                id = line[1]
                index = 2
                while line[index]!='|' :
                    id = id + line[index]
                    index+=1
                #print(query_prot.strip())
                #print(id)
                if id==query_prot.strip():
                    #print("id found"+ line[index+1])
                    index+=1
                    count = 1
                    label = ''
                    while line[index]!='|':
                        index+=1
                        #print(line[index])
                        if(line[index]=='|'):
                            if(count!=2):
                                count+=1
                                index+=1
                            else:
                                break
                    #print(line[index], count)
                    index+=1
                    while line[index]!='|':
                        label = label+line[index]
                        index+=1
                    return label


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


def read_id(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        flag = 0
        count = 0
        seq_count = 0
        for line in lines:
            if line[0] == '>':
                count +=1
                print("cluster count: " ,count)
                continue                                
            else:
                seq_count+=1
                print("sequence count: ", seq_count)
                index = 0
                #print(line)
                while line[index] != '>':
                    index+=1
                #print(index)
                seq_id = ''
                index+=1
                while line[index]!='|':
                    seq_id = seq_id + line[index]
                    index+=1
                with open('arg_v5_90_seq_with_label_others_test_3456_fasta','a') as file:
                    #if(count>650):    #uncomment for test set
                    if get_label(seq_id) in index_of_args:
                        file.write('>'+seq_id+'|'+get_label(seq_id)+'\n'+get_seq(seq_id))
                    else:
                        file.write('>'+seq_id+'|'+'others'+'\n'+get_seq(seq_id))
                #print(seq_id)
                #print(get_seq(seq_id))
                #break          
    #print(count)


print(read_id('/home/shafayat/Desktop/ARG_Language/arg_v5_90_test_sorted.clstr'))
##print(get_label('ACT97463.1'))