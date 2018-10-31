## Find GC per position



import sys, os, re
import all_functions as mg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def main():
 print('==')
 R = mg.read_read_fastQ(sys.argv[1])
 gc = mg.findGCByPos(R)
 #print(gc)
 '''
 # Terminal plot
 for i in range(0,101,10):
  print("%10d"%i,end='')
 print()
 for i in range(0,101,10):
  print("%10s"%'|',end='')
 print()
 for p in gc:
   print("%10d-"%p,end='')
   print('*'.rjust(int(gc[p]),'='))   
 '''
 plt.plot(range(0,len(gc)),[gc[i] for i in range(0,len(gc))], label='GC%')
 plt.xlabel('Position on read')
 plt.ylabel('%GC')
 plt.title("Percentage of GC per Position")
 #plt.show()
 pp = PdfPages('perc_GC.pdf')
 plt.savefig(pp, format='pdf')
 pp.close()
main()
