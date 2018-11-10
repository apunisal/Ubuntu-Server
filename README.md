# Ubuntu-Server

# Set-ups

Tools We Need: 

1) Virtual Box
2) Vagrant   
3) Ansible
4) Wetty
5) Ngrok

# Step 1) Vagrant Setup

Create a directory for Vagrant

 #mkdir Ubuntu-18.04.1-Server
 
 #cd Ubuntu-18.04.1-Server

Copy Name from : 
https://app.vagrantup.com/peru/boxes/ubuntu-18.04-server-amd64

 #vagrant init peru/boxes/ubuntu-18.04-server-amd64

Add server detais in Vagrant File

 #vim Vagrantfile

config.vm.define "server1" do |server1|
          server1.vm.hostname="server1"
end

config.vm.define "server2" do |server2|
          server2.vm.hostname="server2"
  end

config.vm.define "server3" do |server3|
          server3.vm.hostname="server3"
  end

config.vm.define "server4" do |server4|
          server4.vm.hostname="server4"
  end

config.vm.define "server5" do |server5|
          server5.vm.hostname="server5"
  end
end  

 #vagrant up

# Step 2)Virtual Box settings to bring all systems in one network

Goto Settings for every server
Change Network Setting from NAT to Bridge Adapter,Name: wlp19s0
Now all the Machines are accesible with base machine(ip: 192.168.2.3)
- Login to each system Usename : Vagrant Password : Vagrant
- Use # sudo -i to login to root set password to root
- Uncomment below lines from /etc/ssh/sshd_conf

    1. HostKey /etc/ssh/ssh_host_rsa_key
    2. HostKey /etc/ssh/ssh_host_ecdsa_key
    3. HostKey /etc/ssh/ssh_host_ed25519_key
    4. PermitRootLogin yes
    5. AuthorizedKeysFile      .ssh/authorized_keys
    6. PasswordAuthentication yes

- Restart Service : #service ssh restart
- Provide keygen of Central Machine to all servers  
- Change ip of all 5 systems using command eg : 
    
    #ifconfig eth0 192.168.2.5 netmask 255.255.255.0 
    192.168.2.5 for server1, 192.168.2.6 for server2 and So on..

# Step 3) Ansible Setup on Central Machine 
- Install Ansible Using :   
     #yum install ansilble
- Adding Server entry in ansible/hosts
 
     #cat >> /etc/ansile/hosts
 
      [servers]
      root@192.168.2.5
      root@192.168.2.6
      root@192.168.2.7
      root@192.168.2.8
      root@192.168.2.9

# Step 4) wetty

https://www.tecmint.com/access-linux-server-terminal-in-web-browser-using-wetty/

Step 5) Ngrok 

https://ngrok.com/download
(You can move ngrok in /usr/bin to use it as command)

# 6) From Central Machine

- To run Terminal from Web browser 

     #cd wetty
     #node app.js -p 8080
     #firefox https://localhost:8080     
     
- For Remote Access
    
     #ngrok authtoken https://localhost:8080
     
- Log In From webrowser to Central Machine
- Run Script "Automate.py" Enter User Which You want To create User of Your choice

     
  
  
