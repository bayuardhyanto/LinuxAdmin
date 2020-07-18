#Bayu Ardhyanto
#Python,Raid,Network,Ubuntu Project
#raid.py

from disklist import *
from misc import *


while True:

    print ("Create Raid? [Y],[N]")
    tanya = input()
    if tanya == "N":
    	break
    elif tanya == "Y":
    	#print(chr(27) + "[2J")
        clear()
        spaceline(1)
        print ("===================")
        print (" SELECT RAID LEVEL")
        print ("===================")
        spaceline(2)
        print ("Raid 0 (Strip). Min Drive = 2.")
        print ("Raid 1 (Mirror). Min Drive = 2.")
        print ("Raid 4. NOT ACTIVATED")
        print ("Raid 5 (Striping with distributed parity). Min Drive = 3")
        print ("RAID 6. NOT ACTIVATED")
        print ("Raid 10 (Strip + Mirror). Min Drive = 4")
        spaceline(1)
        mydisklist()
        spaceline(2)


        break