

import sys, os, re

def read_read_fasta(R):
 '''
  read a Reads.fasta file, return list of strings
  @param: <read_file_name>
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
  @param: <read_file_name>
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
 '''
  Read a multi-line Fasta file and return DNA seq as one string 
 '''
 genome_fasta = open(G, 'r')
 genome = ''
 for l in genome_fasta:
  if not re.match(r'^>',l):
   genome += l.rstrip()
 genome_fasta.close()
 return(genome)

def generate_reads(G,N,l):
 '''
  Given a genome seq (G), generate N number of reads of length l.
 '''
 reads =  open('reads.fasta','w')
 for i in range(N):
  k = random.randint(0,len(G)-l+1)
  print(">read_%d\t%d:%d"%(i+1,k,k+l), file=reads)
  print(G[k:k+l], file=reads)
 reads.close()
 print('reads.fasta exported!!', file=sys.stderr)

 
def reverseComplement(s):
 complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
 t = ''
 for base in s:
  t = complement[base] + t  # appending at he end 
 return t

def naive_exact(p,t):
 '''
# This intenets to implement naive exact matching algo.
# find sub-string p in string t
# @params p: pattern
# @params t: text
# returns -1 if p is longer than t 

# Worst case analysis
# x=|p| and y=|t|
# No. of possible alignments: y-x+1
# Max. possible charcter comparisons: x(y-x+1)
#  e.g: p= aaa, t= aaaaaaaaaaaa
# Min. possible charcter comparisons: y-x+1
#  e.g p=abc, t=mnxxvlkm, only the first character per alignemnt 
# Special cases: few letters from p match with some letters in t
#  Most character matches occur nearly equal to min no of char. matching

# How many character comparisons occur when matching P = `AAA` to T = `AAATAA`?
# Ans: 9
# The outer loop of the naive exact matching algorithm iterates over__________
# Alignments. 

 '''
 if len(p) > len(t):
  print('Sub sequence p should be longer than t!!')
  return([-1])
 occurances = list()
 for i in range(len(t)-len(p)+1):
  match = True  # flag 
  for j in range(len(p)):
    if p[j] != t[i+j]:
     match = False
     break
  if match:
   occurances.append(i) # return with 0 index 
 return(occurances)



def naive_with_rc(p,t):
 '''
  Naive exact match with reverse complement
 '''
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


def findGCByPos(reads):
 '''
  Find GC% per postions, return a dict, (pos => gc%)
  @reads: list of read_seqs
 '''
 tot = dict()
 gc = dict()
 p_gc = dict()
 for r in reads:
  for i in range(len(r)):
   if i not in tot:
    tot[i] = 0 
    gc[i] = 0
   tot[i]+=1
   if r[i].upper() == 'G' or r[i].upper() == 'C':
    gc[i] += 1
 for p in tot:
  p_gc[p] =100*gc[p]/tot[p]
 return p_gc
 
 
 

