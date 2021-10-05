#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:55:17 2021

@author: tsanga
"""


def translate(dna):
    
    # borrowed from:
        # https://towardsdatascience.com/starting-off-in-bioinformatics-turning-dna-sequences-into-protein-sequences-c771dc20b89f
        # DNA codon dictionary
    protein = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
           "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
           "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
           "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
           "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
           "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
           "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
           "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
           "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
           "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
           "TAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
           "TAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
           "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
           "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
           "TGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G",
           "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G",
           }
    
    
    #from reference_sequences import protein
    dna = dna.upper()
    prot_seq = ''
    
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon.find('N') > -1: # can occur where nucelotide sequence is missing bases, 'n' gets filled in. 
            prot_seq += 'x'
        else:
            prot_seq += protein[dna[i:i+3]]
            
            if protein[codon] == "*" or i > len(dna)-3:
                break
            
        
            
    return prot_seq
