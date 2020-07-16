#https://netplan.io/examples
#Bayu Ardhyanto
#Python,Raid,Network,Ubuntu Project



import os
import yaml

print ("Type your Ethernet:")
apaini = (os.system("ls /sys/class/net"))

#ename = input()
#print (ename)




myvalue = {'network' : {'version': 2, 'renderer' : 'networkd', 'ethernets':{'enp0s3': {'dhcp4' :'true'}} }}


with open("/etc/netplan/69_config.yaml", "w") as WriteFile:
   yaml.dump(myvalue, WriteFile, default_flow_style=False, default_style=None)
