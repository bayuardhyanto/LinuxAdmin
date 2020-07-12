#Detect ip if it manual or DHCP

import socket

mygetip = (socket.gethostbyname(socket.gethostname()))

if mygetip == "127.0.0.1" or mygetip == "127.0.1.1":
   print("Localhost: " + mygetip )
   print("No IP Define.")
else:
   print("Your IP is: " + mygetip )
   print("")
