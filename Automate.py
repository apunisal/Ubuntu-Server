import os # To use Linux Commands in Python
import sys # To take command line input

#Take Username from user
print("-----WELCOME-------")

#Username and Password are same.
username = sys.argv[1]
print("Please note that username and password will be same.")

#Enter into Vagrant Folder
os.system("cd Ubuntu-18.04.1-Server")

#Boot up All servers
os.system("vagrant up")

#Add User to all Servers 
ansi = "ansible servers -a 'useradd "+username+" -shell /bin/bash -p "+username+"'"
returned_value = os.system(ansi) 

#Results of ansible
print("returned value:" + returned_value +" ")

#///////////////////////////////////////////////////////////////Optional Content/////////////////////////////////////////
#Choose you Servers where you want to work.
print("Please Choose you SERVER")
print("Use Command : #ssh username@ip")
print("Eg : tom@192.168.2.5")
serverList = os.system(tail -n 5 /etc/ansible/hosts)
print(serverList)

print()
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
