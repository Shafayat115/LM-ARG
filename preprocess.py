def get_seq(query_prot):
    #print(query_prot)
    flag = 0
    with open('arg_v5.fasta', 'r') as f:
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

def read_id(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        flag = 0
        count = 0
        for line in lines:
            if flag !=1:
                if line[0] == '>':
                    count +=1
                    if (count == 423):
                        break
                    flag = 1
                    continue
            else:
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
                with open('arg_v5_40_seq.fasta','a') as file:
                    file.write('>'+seq_id+'|'+'\n'+get_seq(seq_id))
                #print(seq_id)
                #print(get_seq(seq_id))
                #break
                flag = 0            
    print(count)



print(read_id('arg_v5_40_sorted.clstr'))
#print(get_seq('ACT97463.1'))