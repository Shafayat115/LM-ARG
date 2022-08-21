 
with open('/home/shafayat/Desktop/ARG_Language/Human_Mouse_final.fasta', 'r') as f:
    lines = f.readlines()
    count = 0
    for y in lines:
        if(y[0]=='>'):
            count+=1
print(count) 
