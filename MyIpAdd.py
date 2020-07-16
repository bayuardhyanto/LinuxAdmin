#Bayu Ardhyanto
#Python,Raid,Network,Ubuntu Project



#Detect ip if it manual or DHCP
# next todo
#1. Ask config network? Yes No
#2. Ask Manual or DHCP ? DHCP Default.
#3. Ask parameter. if manual.
#4. Flush Network
#5. Write Config
#6. Ask Appply new setting?
#7. Ask Enable,Disable,Restart Network Service. Default  nothing.


#https://www.osetc.com/en/how-to-start-stop-restart-network-service-on-ubuntu-or-debian-linux.html
#
#Starting Network Service in Ubuntu
#If your network service daemon is stopped, and you may be need to start it by using the following command:
#
#$ sudo systemctl start networking.service
#or
#$ sudo /etc/init.d/networking start
#
#Stop Network Service in Ubuntu
#If you wish to stop a network service in your Ubuntu or Debian Linux, and you can type the following comand:
#
#$ sudo systemctl stop networking.service
#or
#$ sudo /etc/init.d/networking stop
#
#Restart Network Service in Ubuntu
#If you modified networking configuration in your Ubuntu system, and you need to restart its service by using the following command:
#
#$ sudo systemctl restart networking.service
#or
#$ sudo /etc/init.d/networking restart
#
#Checking Status of Networking Service
#If you need to check the current status of networking service in your Ubuntu system, and you can issue the following command:
#
#$ sudo systemctl status networking.service
#Or
#$ sudo /etc/init.d/networking status
#
#
#Enabling Netowrk Service in Ubuntu
#If you want to enable your network service at system boot on your Ubuntu system, and you can run the following command:
#
#$ sudo systemctl enable networking.service
#
#Disabling Network Service in Ubuntu
#If you want to diable network service at system boot, just using the following command:
#
#$ sudo systemctl disable networking.service
#
#



#Manual IP Add
#https://ubuntu.com/server/docs/network-configuration
#
#ip addr flush eth0
#
#-Manual IP ADD-
#
#network:
#  version: 2
#  renderer: networkd
#  ethernets:
#    eth0:
#      addresses:
#        - 10.10.10.2/24
#      gateway4: 10.10.10.1
#      nameservers:
#          search: [mydomain, otherdomain]
#          addresses: [10.10.10.1, 1.1.1.1]







import socket

mygetip = (socket.gethostbyname(socket.gethostname()))

if mygetip == "127.0.0.1" or mygetip == "127.0.1.1":
   print("Localhost: " + mygetip )
   print("No IP Define.")
else:
   print("Your IP is: " + mygetip )
   print("")
