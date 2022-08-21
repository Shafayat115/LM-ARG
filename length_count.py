
import sys
import Bio.SeqIO as IO


record_dict = IO.to_dict(IO.parse("Data_ARG.fasta", "fasta"))
count =0
ranges_400= []
ranges_800= []
ranges_1200= []
ranges_1600= []
ranges= []

for key in record_dict.items():
    if(len(key[1].seq)<300):
        ranges_400.append(key[0])
print(len(ranges_400))