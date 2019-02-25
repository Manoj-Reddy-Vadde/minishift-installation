import os
import commands
print("""PREREQUISITES : 
1. Ubuntu-16.04 and higher
2. virtualBox-5.1.12 and higher\n
if your system have this requirements then you can processed
press\n1 to processed\n2 to cancel
""")

confirmation = raw_input()
if (confirmation == 2) : 
	exit(0)

OS_MIN_V = '16.04'
VB_MIN_V = '5.1.12'
def verification() :
	OS_C_V = commands.getoutput("lsb_release -r")[-5:]
	VB_C_V = commands.getoutput("vboxmanage --version")[0:6]
	if (OS_C_V < OS_MIN_V) :
		print("""Your ubuntu Version is not greater than 16.04""")
		exit(0)
	if(VB_C_V < VB_MIN_V) :
		print("""your virtual box version is not greater then 5.1.12""")
		exit(0)

verification		

os.chdir("/home/$(whoami)/Dektop")
os.system("sudo apt install libvirt-bin qemu-kvm tar")
os.system("sudo useradd libvirtd")
os.system("sudo usermod -a -G libvirtd $(whoami)")
os.system("newgrp libvirtd")
os.system("sudo apt install curl")
os.system("curl -L https://github.com/dhiltgen/docker-machine-kvm/releases/download/v0.10.0/docker-machine-driver-kvm-ubuntu16.04 -o /usr/local/bin/docker-machine-driver-kvm")
os.system("chmod +x /usr/local/bin/docker-machine-driver-kvm")
os.system("sudo systemctl start libvirtd")
os.system("sudo virsh net-start default")
os.system("sudo virsh net-autostart default")
os.system("sudo virsh net-list --all")
os.system("mkdir minishift-download")
os.chdir("minishift-download")
os.system("wget https://github.com/minishift/minishift/releases/download/v1.31.0/minishift-1.31.0-linux-amd64.tgz")
os.system("tar -xf minishift-*")
os.chdir("minishift-1.31.0-linux-amd64")
os.system("mv minishift /usr/local/bin")
os.chdir("../..")
os.system("minishift config set vm-driver virtualbox")

Disk_size = raw_input("Enter Disk Size (eg: 20GB)")
Memory = raw_input("Enter Memory Size (eg: 4GB)")
Cpu_cores = raw_input("Enter cpu cores (eg: 2)")

# starting minishift

cmd="minishift start --disk-size "+Disk_size+" --memory "+Memory+" --cpu "+Cpu_cores+" --show-libmachine-logs"
os.system(cmd)
