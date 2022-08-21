from enum import unique
from operator import index
import random



    
def get_seq(query_prot):
    flag = 0
    with open('/home/shafayat/Desktop/ARG_Language/Human_Mouse_final.fasta', 'r') as f:
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

      

randomlist = []
with open('/home/shafayat/Desktop/ARG_Language/Selected_Non-ARG_Human_Mouse.txt', 'r') as f:
        lines = f.readlines()        
        for line in lines:
            id = line.split(' ')[0]
            randomlist.append(id)

print(len(randomlist))
num_values = set(randomlist)
unique_val = list(num_values)

print(len(num_values))


randomtrainlist = random.sample(range(0, 1730), round(1730*0.80))
#print("randomlist: ",randomlist)
randomtestlist = []
with open('human_mouse_train.fasta','a') as file1:
    with open('human_mouse_1_test.fasta','a') as file2:
        for x in range(1730):
            if x in randomtrainlist:
                file1.write('>'+unique_val[x]+'|'+'NON-ARG'+'\n'+get_seq(unique_val[x]))
            else:
                file2.write('>'+unique_val[x]+'|'+'NON-ARG'+'\n'+get_seq(unique_val[x]))
            #print(x)  """