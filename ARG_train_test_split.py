

from enum import unique
from operator import index
import random



    
def get_seq(query_prot):
    flag = 0
    with open('/home/shafayat/Desktop/ARG_Language/human_mouse.fasta', 'r') as f:
        lines = f.readlines()
        prot = ''
        for line in lines:
            if flag:
                if line[0] != '>':
                    prot = prot + line
                else:
                    break
            if line[0] == '>':
                id = line[4]
                index = 5
                while line[index]!='|':
                    id = id + line[index]
                    index+=1
                #print(id)
                if id==query_prot:
                    flag = 1
                    
    return prot

      
    
def get_arg_seq(query_prot):
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


randomlist = []
with open('/home/shafayat/Desktop/ARG_Language/arg_v5.fasta', 'r') as f:
        lines = f.readlines()        
        for line in lines:
            if line[0] == '>':
                id = line[1]
                index = 2
                while line[index]!='|':
                    id = id + line[index]
                    index+=1
                randomlist.append(id)
#print(randomlist)




randomtrainlist = random.sample(range(0, 17282), round(17282*0.80))
#print("randomlist: ",randomlist)
randomtestlist = []
with open('arg_1_train.fasta','a') as file1:
    with open('arg_1_test.fasta','a') as file2:
        for x in range(17282):
            if x in randomtrainlist:
                file1.write('>'+randomlist[x]+'|'+'ARG'+'\n'+get_arg_seq(randomlist[x]))
            else:
                file2.write('>'+randomlist[x]+'|'+'ARG'+'\n'+get_arg_seq(randomlist[x]))
            print(x)
            
                    
