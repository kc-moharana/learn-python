'''
 Change group property of mp3 folder
  - all mp3 files inside a folder
  
-bulk rename
for %f in (.\*) do rename "%f" "%~nf".mp3
'''



from mp3_tagger import MP3File, VERSION_2	# VERSION_1, VERSION_BOTH
import re, sys,os
from os import listdir
from os.path import isfile, join, getsize
import unicodedata

def print_file_details(mp3_files,mp3_dir_path):
 print >> sys.stderr, "||%5s %70s %10s||"%(chr(177)*5, 'FILES',chr(177)*10)
 print >> sys.stderr, "||%5s %70s %10s||"%(chr(177)*5, chr(177)*70,chr(177)*10)
 count = 1
 for f in mp3_files:
  mp3_input = join(mp3_dir_path, f)
  mp3 = MP3File(mp3_input)
  mp3.set_version(VERSION_2) ## Better support longer names
  try: 
   print >> sys.stderr, "+[%3s] %35s %35s   %0.2f Mb"%(count,f,mp3.song,getsize(mp3_input)*0.000001 )
  except UnicodeError:
   print >> sys.stderr, 'Differnt Char. Encoding!!!'
   #print >> sys.stderr, 'Machine Encode: '+sys.stdout.encoding
   #print >> sys.stderr, ord(f[4]),chr(ord(f[4])) 		#f.encode('ascii','ignore')			#unicode(f, "utf8")
   #print >> sys.stderr,unicodedata.category(chr(ord(f[4])))
   #print >> sys.stderr, "+[%3s] %35s %35s   %0.2f Mb"%(count,unicode(f, "utf8"),unicode(mp3.song, "utf8"),getsize(mp3_input)*0.000001 )   
  count += 1
 print >> sys.stderr, ''
 print >> sys.stderr, "||%5s %70s %10s||"%(chr(177)*5, chr(177)*70,chr(177)*10)
 print >> sys.stderr, ''
 
def edit_songs(mp3_files,mp3_dir_path,noise_text,album_name):
 for f in mp3_files:
  mp3_inp = join(mp3_dir_path, f)
  # Create MP3File instance.
  mp3 = MP3File(mp3_inp)
  mp3.set_version(VERSION_2) ## Better support longer names 
  # Get all tags.
  #original_tags = mp3.get_tags()
  if len(noise_text) >1:
   mp3.song = re.sub(noise_text,'',mp3.song)
  if len(album_name) >1:
   mp3.album = album_name
  mp3.save()
  print>> sys.stderr, "%s done"%f

def clean_file_names(mp3_files,mp3_dir_path,noise_text):
 for f in mp3_files:
  mp3_inp = join(mp3_dir_path, f)
  new_file = re.sub(noise_text,'',f)
  cmd = "rename \"%s\" \"%s\".mp3"%(mp3_inp, new_file)
  print >> sys.stderr,cmd
  os.system(cmd)
  #print>> sys.stderr, "%s done"%f

try:
 mp3_dir_path = sys.argv[1]
except IndexError:
 print >> sys.stderr, "Usage:python %s FOLDER" %sys.argv[0]
 sys.exit(1) 

mp3_file_names = [f for f in listdir(mp3_dir_path) if isfile(join(mp3_dir_path, f))] 
#print >> sys.stderr, "# of .mp3 files found %d"%len(mp3_file_names)
#print mp3_file_names
print_file_details(mp3_file_names,mp3_dir_path)

confirm = raw_input('Want to clean Album/song? {Y/N}:').rstrip()
if confirm.upper() == 'Y':
 album_name = raw_input('Enter album name:(press Enter to leave unchanged) ').rstrip()
 noise_text = raw_input('Enter the noise text in title (removed automatically): ')
 noise_text = noise_text.rstrip()
 noise_text = r"\s*"+re.escape(noise_text)+"\s*"
 edit_songs(mp3_file_names,mp3_dir_path,noise_text,album_name)
 print_file_details(mp3_file_names,mp3_dir_path)

confirm = raw_input('Want to rename file? {Y/N}:').rstrip()
if confirm.upper() == 'Y':
 noise_text = raw_input('Enter the noise text in file name (removed automatically): ')
 noise_text = noise_text.rstrip()
 noise_text = r"\s*"+re.escape(noise_text)
 clean_file_names(mp3_file_names,mp3_dir_path,noise_text)
 


