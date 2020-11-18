# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:23:56 2020

@author: vishu
"""

# Read FASTA sequences in a dictionary
seqdict = {}
sequence = ''

with open('protein.fasta') as protein:
    for line in protein:
        line = line.strip() #removes \n
        if line.startswith('>'):
            if not sequence == '':
                seqdict[seqid] = sequence
                sequence = ''
            seqid = line[1:]
        else:
            sequence = sequence + line
    seqdict[seqid] = sequence

print(seqdict)
