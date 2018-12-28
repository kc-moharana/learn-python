'''
 Mp3_tagger
 Allowed tags:

    - artist;
    - album;
    - song;
    - track;
    - comment;
    - year;
    - genre;
    - band (version 2.x);
    - composer (version 2.x);
    - copyright (version 2.x);
    - url (version 2.x);
    - publisher (version 2.x).

# By default selected tags in both versions.
mp3.set_version(VERSION_BOTH)

# Change to 2.x version.
mp3.set_version(VERSION_2)

# For 1.x version
mp3.set_version(VERSION_1)

# After the tags are edited, you must call the save method.
mp3.save()
''' 

def print_tags(tag_dict,tag_list):
 print >> sys.stderr, "||%15s %50s||"%(chr(177)*10,chr(177)*50)
 for tag in tag_list:
  print >> sys.stderr, "+[%12s] : %s"%(tag, tag_dict[tag])
 print >> sys.stderr, ''
 print >> sys.stderr, "||%10s %50s||"%(chr(177)*10,chr(177)*50)
 print >> sys.stderr, ''

def edit_a_tag(noise_text,tag_dict,tag_list,reponse):
 print >> sys.stderr, "\tEditing: %s: %s"%(tag_list[reponse],tag_dict[tag_list[reponse]])  
 new_text = raw_input("\tEnter new text: ").rstrip() 
 if len(new_text) <2:
  confirm = raw_input('Want to change tag [Y/N]: ').rstrip()
  if confirm.upper() == 'Y':
   tag_dict[tag_list[reponse]] = new_text  
 else:
  tag_dict[tag_list[reponse]] = new_text  
 return(tag_dict)
 
def compare_two_tag_dict(tag_dict1,tag_dict2,title1,title2):
 print >> sys.stderr, "||%15s %50s %50s||"%(chr(177)*10,chr(177)*50,chr(177)*50)
 print >> sys.stderr, "||%15s %50s %50s||"%('TAGs',title1,title2)
 for tag in tag_list:
  print >> sys.stderr, "+[%12s] : %50s %50s"%(tag, tag_dict1[tag],tag_dict2[tag])
 print >> sys.stderr, ''
 print >> sys.stderr, "||%15s %50s %50s||"%(chr(177)*10,chr(177)*50,chr(177)*50)
 print >> sys.stderr, ''

def save_tags(mp3_obj, tag_dict,original_tags):
 if 'artist' in tag_dict:
  mp3_obj.artist = tag_dict['artist']
 if 'album' in tag_dict:
  mp3_obj.album = tag_dict['album']
 if 'comment' in tag_dict:
  mp3_obj.comment = tag_dict['comment']
 if 'track' in tag_dict:
  mp3_obj.track = tag_dict['track']
 if 'song' in tag_dict:
  mp3_obj.song = tag_dict['song']
 if 'genre' in tag_dict:
  mp3_obj.genre = tag_dict['genre']
 if 'year' in tag_dict:
  mp3_obj.year = tag_dict['year']
 if 'copyright' in tag_dict:
  mp3_obj.copyright = tag_dict['copyright']
 if 'band' in tag_dict:
  mp3_obj.band = tag_dict['band']
 if 'composer' in tag_dict:
  mp3_obj.composer = tag_dict['composer']
 if 'url' in tag_dict:
  mp3_obj.url = tag_dict['url']
 if 'publisher' in tag_dict:
  mp3_obj.publisher = tag_dict['publisher'] 
 compare_two_tag_dict(original_tags,tag_dict,'Original','Edited')
 confirm = raw_input('Confirm Save changes?(y/n)').rstrip()
 if confirm.upper() == 'Y':
  mp3_obj.save()
  print >>sys.stderr, 'Changes saved!! - OK -'
  return(1)
 else:
  print >>sys.stderr, 'Changes NOT saved!!'
  return(0)
  
 
from mp3_tagger import MP3File, VERSION_2	# VERSION_1, VERSION_BOTH
import os, re, sys
try:
 mp3_inp = sys.argv[1]
except IndexError:
 print >> sys.stderr, "Usage:python %s song.mp3" %sys.argv[0]
 sys.exit(1) 


# Create MP3File instance.
mp3 = MP3File(mp3_inp)
mp3.set_version(VERSION_2) ## Better support longer names 
# Get all tags.
original_tags = mp3.get_tags()
new_tags = {k:v for k,v in original_tags.items()} 
tag_list = sorted(original_tags.keys())
print_tags(original_tags,tag_list)

noise_text = raw_input('Enter the noise text (removed automatically): ')
noise_text = noise_text.rstrip()
noise_text = r"\s*"+re.escape(noise_text)
print >> sys.stderr, noise_text
for tag in tag_list:
 if new_tags[tag] == None:
  continue
 if re.search(str(noise_text), new_tags[tag]):
  new_tags[tag] = re.sub(str(noise_text),'',new_tags[tag])

while 1:
 os.system('cls')
 print >> sys.stderr, "%15s %20s %25s"%(chr(176)*15, 'CURRENT FILE',chr(176)*15)
 print >> sys.stderr, "\t%s"%(os.path.basename(mp3_inp))
 print_tags(new_tags,tag_list)
 print >> sys.stderr, "%15s %20s %25s"%(chr(176)*15, 'MENU',chr(176)*15)
 print >> sys.stderr, '[ x:Exit\tc:Close_Editing\ts:Save]'
 print >> sys.stderr, ''
 print >> sys.stderr, "%15s %20s %25s"%(chr(176)*15, 'EDIT TAGS',chr(176)*15)
 for i in xrange(len(tag_list)):
  print >> sys.stderr,"[ %2d]:%s\t"%(i,tag_list[i]),
  if (i+1)%4==0 and i>0:
   print >> sys.stderr,''
   print >> sys.stderr, ''
 print >> sys.stderr, ''
 print >> sys.stderr, ''
 response = raw_input('Enter choice:').rstrip()
 if response == 'x' or response == 'c' or response == 's':
  if response == 'x':
   sys.exit(1)
  elif response == 'c':
   break
  elif response == 's':
   os.system('cls')
   confirm = save_tags(mp3,new_tags,original_tags)
   if confirm:
    print >> sys.stderr, 'Tag changes saved'
   else:
    print >> sys.stderr, 'Error: Tag changes FAILED to save!!'
   
 else:
  response = int(response)
  new_tags = edit_a_tag(noise_text,new_tags,tag_list,response)

new_file = raw_input('Want to rename file? {Y/N}:').rstrip()
if new_file.upper() == 'Y':
 new_file = raw_input("\tNew file name::").rstrip()
 file_path = os.path.normpath(mp3_inp)
 file_base = os.path.basename(mp3_inp)
 cmd = "rename \"%s\" \"%s\" "%(mp3_inp, new_file)
 print >> sys.stderr,cmd
 os.system(cmd)