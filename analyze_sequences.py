#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import dependencies and set starting alignment parameters
import pandas as pd


# In[ ]:


# set reference sequence to 602.2
refseq = 'MGESINFVSWGGSTQDAQKQAWADPFSKASGITVVQDGPTDYGKLKAMVESGNVQWDVVDVEADFALRAAAEGLLEPLDFSVIQRDKIDPRFVSDHGVGSFLFSFVLGYNEGKLGASKPQDWTALFDTKTYPGKRALYKWPSPGVLELALLADGVPADKLYPLDLDRAFKKLDTIKKDIVWWGGGAQSQQLLASGEVSMGQFWNGRIHALQEDGAPVGVSWKQNLVMADILVVPKGTKNKAAAMKFLASASSAKGQDDFSALTAYAPVNIDSVQRLDLAQVRITADKQKNGIMANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITLGMDELYKGGTGGSMSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKQHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNWNANLAPNLPTAYVKDQITLDFAYWAKNGPAIATRWNEWLVKGSHHHHHH*'


# In[ ]:


# read csv of dna sequences and generate translations (?) not yet implemented


# In[ ]:


# read the csv of PROTEIN sequences
prot_seq = pd.read_csv('20210819_igabasnfr_sequence_analysis_input.csv')


# In[ ]:


prot_seq


# In[ ]:


prot_seq.shape
print(prot_seq.shape)

numItems = prot_seq.shape[0]
print(numItems)


# In[ ]:


# Create length and mutations columns for all entries
prot_seq.loc[(prot_seq['Plate'] != ''), 'Length'] = ''
prot_seq.loc[(prot_seq['Plate'] != ''), 'Mutations'] = ''
prot_seq


# In[ ]:


# derived from /tsanga/code/find_mutations.py
# version 2021-08-18

# go through the sequences and compare each to 602.2. 
# create a column in the pandas table that shows the amino acid changes
# it's important to note that the residue numbering is specific to this analysis, it must be converted
# to Jonny's system for interpretation. 

for i in range(numItems):
    mutList = []
    
    # on each iteration, assign the entry sequence to seq
    seq = prot_seq.iloc[i]['Sequence']
    
    # find the length of the sequence
    prot_seq.loc[(prot_seq["Sequence"] == seq), 'Length'] = len(seq)
    
    # find the differences in letters
    for j in range(len(seq)):
        if seq[j] != refseq[j]:
            if seq[j] == '*':
                mutation = refseq[j] + str(j+1) + 'STOP'
            else:
                mutation = refseq[j] + str(j+1) + seq[j]
            mutList.append(mutation)
            
    # convert array to string
    mutString = str(mutList)
    mutString = mutString.replace("'","")
    mutString = mutString.replace("[","")
    mutString = mutString.replace("]","")
    
    # remove excess characters from mutString
    
            
    # assign the mutation list to the correct item by matching the sequence
    prot_seq.loc[(prot_seq["Sequence"] == seq), 'Mutations'] = mutString
    


# In[ ]:


prot_seq


# In[ ]:


prot_seq.to_csv('20210819_iGABASnFR_mutations_results.csv')

