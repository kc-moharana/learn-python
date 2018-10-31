# generate artificial reads using DNA seq of a given genome

import sys, os, re
import random


try:
 genome_fasta = open(sys.argv[1], 'r')
 genome = ''
 for l in genome_fasta:
  if not re.match(r'^>',l):
   genome += l.rstrip()
 genome_fasta.close()
 
except IndexError:
 print('Usage: python3 %s genome.fa'%sys.argv[0])
 exit(1)



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
 
generate_reads(genome, 100, 51)
