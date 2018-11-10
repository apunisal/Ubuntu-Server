import os

#Take Username from user
print("-----WELCOME-------")

#Username and Password are same.
username = raw_input("Enter the Username : ")
print("Please note that username and password will be same.")

#Enter into Vagrant Folder
os.system("cd Ubuntu-18.04.1-Server")

#Boot up All servers
os.system("vagrant up")

#Add User to all Servers 
ansi = "ansible servers -a 'useradd "+username+" -shell /bin/bash -p "+username+"'"
returned_value = os.system(ansi) 

#Results of ansible
print('returned value:', returned_value)

#Choose you Servers where you want to work.
print("Please Choose any one Server from 1 to 5")
ch = raw_input("Server no : ")
if ch=="1" : 
    os.system("ssh "+ username +"@server1.example.com")
elif ch=="2":
    os.system("ssh "+ username +"@server2.example.com")
elif ch=="3":
    os.system("ssh "+ username +"@server3.example.com")
elif ch=="4":
    os.system("ssh "+ username +"@server4.example.com")
elif ch=="5":
    os.system("ssh "+ username +"@server5.example.com")
else:
    print("Enter Valid Number")
