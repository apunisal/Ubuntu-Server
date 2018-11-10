import os

print("-----WELCOME-------")
username = raw_input("Enter the Username : ")
print("Please note that username and password will be same.")
os.system("cd Ubuntu-18.04.1-Server")
os.system("vagrant up")
ansi = "ansible servers -a 'useradd "+username+" -shell /bin/bash -p "+username+"'"
returned_value = os.system(ansi) 
print('returned value:', returned_value)
print("Please Choose any one Server from 1 to 5")
ch = raw_input("Server no : ")
if ch=="1" : 
    os.system("ssh "+ username +"@192.168.2.5")
elif ch=="2":
    os.system("ssh "+ username +"@192.168.2.6")
elif ch=="3":
    os.system("ssh "+ username +"@192.168.2.7")
elif ch=="4":
    os.system("ssh "+ username +"@192.168.2.8")
elif ch=="5":
    os.system("ssh "+ username +"@192.168.2.9")
else:
    print("Enter Valid Number")
