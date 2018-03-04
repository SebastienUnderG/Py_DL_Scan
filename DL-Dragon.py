import urllib2,cookielib
from shutil import copyfile
import time
from tqdm import tqdm
import os
cwd = os.getcwd()


def downloadit(ntome,npage):
   #ntome = 4
   #npage = 001
   cwd = os.getcwd()
   site= "http://cd151.d836pbl.club/lel/Dragon-Ball/Scan-Dragon-Ball-Tome-"
   file_url = site+str(ntome)+'-VF/'+str(npage).zfill(3)+'.jpg'

   if ntome == 6:
       file_url = site+str(ntome)+'-VF/0'+str(npage+1).zfill(3)+'%2520'+str(npage).zfill(3)+'%2520%255BMangas-Fuki.com%255D.jpg'
   if ntome > 6:
       file_url = site+str(ntome)+'-VF/'+str(npage).zfill(4)+'.jpg'

   #print file_url

   dossier = cwd+'/Dragon-Ball-Tome-'+str(ntome)+'-VF/Dragon-Ball-Tome-'+str(ntome)+'-VF-'+str(npage).zfill(3)+'.jpg'


   hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}

   req = urllib2.Request(file_url, headers=hdr)
   try:
       page = urllib2.urlopen(req)
   except urllib2.HTTPError, e:
       #print e.fp.read()
       if e.code == 404:
           if npage == 2:
               copyfile(cwd+'/blank.jpg', dossier)
           return False

   content = page.read()

   with open(dossier, 'wb') as f:
       f.write(content)
   return;


i = 0

ntome = 13


newpath = cwd+'/Dragon-Ball-Tome-'+str(ntome)+'-VF/'
if not os.path.exists(newpath):
    os.makedirs(newpath)

print 'Tome :'+str(ntome)
for i in tqdm(range(250)):
    time.sleep(0.01)
    downloadit(ntome,i)
    i += 1
