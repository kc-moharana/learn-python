# match reads.fq with genome


import sys, os, re


def naive_exact(p,t):
 #print(p)
 #print(t)
 occ = list()
 for i in range(len(t)-len(p)+1):
  match=True
  for j in range(len(p)):
   if p[j] != t[i+j]:
    match = False
    break
  if match:
   occ.append(i)
 return(occ)


def read_read_fasta(R):
 '''
  read a Reads.fasta file, return list of strings
 '''
 r = list()
 F = open(R,'r')
 for l in F:
  if not re.match(r'^>', l): # expect each > follows one short read as one line
   r.append(l.rstrip())
 F.close()
 return r


def read_read_fastQ(R):
 '''
  read a Reads.fastq file, return list of strings
 '''
 r = list()
 F = open(R,'r')
 while True:
  header = F.readline().rstrip()
  seq = F.readline().rstrip()
  F.readline()  # place holder + or Quality score identifier line (consisting only of a +)
  qual = F.readline().rstrip()
  if len(seq) == 0:
   break
  r.append(seq)
 F.close()
 return r 


def read_genome_file(G):
 genome_fasta = open(G, 'r')
 genome = ''
 for l in genome_fasta:
  if not re.match(r'^>',l):
   genome += l.rstrip()
 genome_fasta.close()
 return(genome)
 
def reverseComplement(s):
 complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
 t = ''
 for base in s:
  t = complement[base] + t  # appending at he end 
 return t

def naive_with_rc(p,t):
 occ = list()
 occ = naive_exact(p,t)
 rc_p = reverseComplement(p)
 if rc_p != p:
  occ.extend(naive_exact(rc_p,t))
 return occ
 

def naive_2mm(p,t):
 '''
  naive exact algo that allows up to 2 mismatches per occurrence
 '''
 occ =list()
 for i in range(len(t)-len(p)+1):
  match =True
  mm=0
  for j in range(len(p)):
   if p[j] != t[i+j]:
    mm +=1
   if mm >2:
    match =False
    break
  if match:
   occ.append(i)
 return occ


  
try:
 G = sys.argv[1]    
 R1 = sys.argv[2]
 R2 = sys.argv[3]        
 genome = read_genome_file(G)
# reads = read_read_fasta(R)
 reads_1 = read_read_fastQ(R1)
 reads_2 = read_read_fastQ(R2)
# print(reads)

except IndexError:
 print("Usage: python3 %s Genome.fa Read_1.fq Read_2.fq")
 exit(1)
 
 
matched_reads_1 = 0
for r in reads_1:
# print(r,end='')
 if len(naive_exact(r, genome)):
  matched_reads_1 +=1
  #print("\t match")
print("%d / %d reads_1 matched exactly"%(matched_reads_1, len(reads_1)))

matched_reads_2 = 0
for r in reads_2:
# print(r,end='')
 if len(naive_exact(reverseComplement(r), genome)):
  matched_reads_2 +=1
  #print("\t match")
print("%d / %d reads_2 matched exactly"%(matched_reads_2, len(reads_2)))






















