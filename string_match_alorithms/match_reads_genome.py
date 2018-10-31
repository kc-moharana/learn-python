# match reads with genome


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


  
try:
 G = sys.argv[1]    
 R = sys.argv[2]    
 genome = read_genome_file(G)
# reads = read_read_fasta(R)
 reads = read_read_fastQ(R)
# print(reads)

except IndexError:
 exit(1)
 
 
matched_reads = 0
for r in reads:
 print(r,end='')
 if len(naive_exact(r, genome)) >1:
  matched_reads +=1
  print("\t match")
print("%d / %d reads matched exactly"%(matched_reads, len(reads)))




