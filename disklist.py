#Bayu Ardhyanto
#Python,Raid,Network,Ubuntu Project
#diskList.py

import subprocess

def mydisklist():
   files = subprocess.Popen(["""lsblk -o 'NAME','type' | grep -i disk"""], shell=True, stdout=subprocess.PIPE).stdout
   hasil = files.read().splitlines()
   bersih = []
   for x in hasil:
      bersih.append((str(x,'utf-8')[0:3]))
#   print ("\033[1;33;40m" + "test" + "\n")
   print ( bersih )
   print (str(len(bersih)) + " Disk detected.")