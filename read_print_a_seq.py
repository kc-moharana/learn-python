
#Thu Oct 29 11:42:58 IST 2015
#This script will read and print a FASTA sequence





from sys import argv

script, seq_file =argv
print """#Script:%s
#Usage: python %s <input_seq_file>
#To see the stats of a input FASTA sequence""" %script %script

S_file =  open(seq_file,r)
	


