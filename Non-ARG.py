import pandas as pd

#read_file = pd.read_csv (r'unprot_blast.txt')
#read_file.to_csv (r'uniprot_blast.csv', index=None)

#print(df.head())
#print(df.shape)

#print(df.loc[df['evalue'] < 0.001e-12])
#print(df.loc[:,['sseqid','evalue']])
#print((df.loc[df['evalue'] < 0.001e-12]).loc[:,['sseqid','evalue']])

df = pd.read_csv("human_mouse_blast_result.csv", names=['qseqid' ,'sseqid' , 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'], sep='\t')


with open("Selected_Non-ARG_Human_Mouse.txt", 'a') as f:
    dfAsString = ((df.loc[df['evalue'] < 1]).loc[:,['sseqid','evalue']]).to_string(header=False, index=False)
    f.write(dfAsString)