import os
import subprocess

myDisk = {} #Disk name Dict

output = os.system ("""lsblk -o 'NAME','type' | grep -i disk""")

for line in output.check.split('\n'):
    line = line.strip 


hasil={mydisk}

guna= str(mydisk)
print (guna[0])
