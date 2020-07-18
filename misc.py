#Misc file




import os

#Clear Screen
def clear():
	os.system("cls" if os.name=="nt" else "clear")

#new empty line
def spaceline(x):
	for i in range (x):
		print ("")



