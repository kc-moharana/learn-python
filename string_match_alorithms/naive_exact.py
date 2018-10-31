
import os, sys, re

try:
 p = sys.argv[1].rstrip()
 t = sys.argv[2].rstrip()
 print("p: %s\nt: %s"%(p,t))
except IndexError:
 print("No input!!\nUsage: python3 %s p_string t_string"%sys.argv[0], file=sys.stderr)
 exit(1)

def naive_exact(p,t):
 '''
# This intenets to implement naive exact matching algo.
# find sub-string p in string t
# returns -1 if error 

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
#------------------------------------------------------

print("matches found "+" ".join([str(k) for k in naive_exact(p,t)]))







