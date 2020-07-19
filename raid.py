#Bayu Ardhyanto
#Python,Raid,Network,Ubuntu Project
#raid.py

from disklist import *
from misc import *


while True:
    print ("Create Raid? [Y],[N]")
    myinputkey = input()
    if myinputkey == "N" or myinputkey =="n":
        spaceline(2)
        print ("Canceled")
        spaceline(2)
        exit() #exit
    elif myinputkey == "Y" or myinputkey == "y":
    	#print(chr(27) + "[2J")
        #two times asking [0][hda,hdb] or
        #one time asking [0,hda,hdb]
        #two times asking or more better than one time asking
        #filer raid by available disk detected? or just show all and deny when minimum hdisk req not available
        #check for dulpicate add disk by invalid input 
        while True:
            clear()
            spaceline(1)
            print ("===================")
            print (" SELECT RAID LEVEL")
            print ("===================")
            spaceline(2)
            print ("[  0 ]  Raid 0 (Strip). Min Drive = 2.")
            print ("[  1 ]  Raid 1 (Mirror). Min Drive = 2.")
            print ("        Raid 4. NOT ACTIVATED")
            print ("[  5 ]  Raid 5 (Striping with distributed parity). Min Drive = 3")
            print ("        RAID 6. NOT ACTIVATED")
            print ("[ 10 ]  Raid 10 (Strip + Mirror). Min Drive = 4")
            print ("[  C ]  Cancel create RAID")
            spaceline(1)
            mydisklist()
            spaceline(2)
            myinputkey = "" #Reset value and reuse Variable
            myinputkey = input()
            if myinputkey == 0:
                #hh
            elif myinputkey == 1:
                #dfdsf
            elif myinputkey == 5:
                #dfdgdsg
            elif myinputkey ==10:
                #djbfd
            elif myinputkey == "C" or myinputkey == "c":
                exit()