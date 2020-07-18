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
        print ("SELECT RAID LEVEL.")
        spaceline(2)
        print ("Raid 0 (striping). Minimum drive = 2. Fault tolerance = none , read performance = high,  write performance = high ")
        print ("")
        mydisklist()
        break