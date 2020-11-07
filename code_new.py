#!/usr/bin/python3

import os
import subprocess as sp
import getpass


# docker , LVM
def MENU():
    print('Services - ')
    print('1. Docker')
    print('2. LVM')
    print('3. AWS')
    print('4. Hadoop')
    print('5. Webserver')
    print('Basic Commands-')
    print('6. Date')
    print('7. Cal')
    print('8. Open Firefox')
    print('9. Ifconfig')
    service = int(input('Enter here : '))
    if service == 1:
        dockerconf()
    #elif service == 2:
        #lvmconf()
    elif service == 3:
      	awsconf()
    #elif service == 4:
        #hadoopconf()
    elif service == 5:
        webser_conf()
    elif service == 6:
        x=sp.getoutput('date')
        print(x)
    elif service == 7 :
        x=sp.getoutput('cal')
        print(x)
    elif service == 8:
        x=sp.getoutput('firefox')
        print(x)
    elif service == 9:
        x=sp.getoutput('ifconfig')
        print(x)
    else :
        print('unsupported input')
        
    
def dockerconf():
    ec = sp.getoutput('docker --version | echo $?')
    if ec == 0 :
        print('docker is not installed')
        pass
    else :
        print("-----------DOCKER----------")
        print("1. Docker daemon start/stop/status")
        print("2. Show docker process")
        print("3. Show docker images")
        print("4. Search images on docker hub")
        print("5. Download docker image from docker hub")
        print("6. Run a docker image")
        print("7. Stop docker container")
        print("8. Delete docker image")
        print("9. Configure webserver(httpd) in docker container")
        command = input('\nEnter your choice - ')
        if command == 1:
            op = int(input('1.start  2.stop  3.status'))
            if op == 1: sp.getoutput('systemctl start docker')
            elif op == 2: sp.getoutput('sytemctl stop docker')
            elif op == 3: sp.getoutput('systemctl status docker')
            else: print('unsupported input')
        elif command == 2:
            op = int(input('1.Recent process  2.All process'))
            if op == 1: sp.getoutput('docker ps')
            elif op == 2: sp.getoutput('docker ps -a')
            else: print('unsupported input')
        elif command == 3: sp.getoutput('docker images')
        elif command == 4:
            im = input('image name - ')
            sp.getoutput('docker search {}'.format(im))
        elif command == 5:
            im = input('image name - ')
            sp.getoutput('docker pull {}'.format(im))
        elif command == 6:
            im = input('image name - ')
            sp.getoutput('docker run -it {} &'.format(im))
        elif command == 7:
            im = input('image name - ')
            sp.getoutput('docker stop {}'.format(im))
        elif command == 8:
            im = input('image name - ')
            sp.getoutput('docker rmi {}'.format(im))
        elif command == 9:
            httpdconf()
        else: print('Error')
        
def Menussh():
        print("Enter the ip address of remote host",end=": ")
        ip=input()
        print('Basic Commands-')
        print('1. Date')
        print('2. Cal')
        #print('3. Open Firefox')
        service = int(input('Enter here : '))
        if service == 1:
            sp.getoutput("ssh {} date".format(ip))
        elif service == 2:
            sp.getoutput("ssh {} cal".format(ip)) 
        #elif service == 3:
            #sp.getoutput("ssh {} firefox".format(ip))

		else :
            print('unsupported input')

#def lvmconf()
def awsconf():
        print('--Services--')
        print('EC2')
        print('EBS')
        print('S3 ')
        aws_ser = input('Enter here : ')
        if aws_ser == 'EC2' or aws_ser == 'ec2' :
        	ec2conf()
        elif aws_ser == 'EBS' or aws_ser == 'ebs':
                ebsconf()
        elif aws_ser == 'S3' or aws_ser == 's3':
                s3conf()
        else :
                print('unsupported input')

def ec2conf():
    print("-----------EC2----------")
    print("1. Create/Delete Key Pair")
    print("2. Create/Delete Security group")
    print("3. EC2 instance start/stop/terminate")
    print("4. Show all instances ")
    print("5. Create new Instance")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        kp = int(input('1.Create  2.Delete '))
        if kp == 1:
            key_name = input("Enter key name : ")
            sp.getoutput('aws ec2 create-key-pair --key-name {0}'.format(key_name))
        elif kp == 2:
            key_name = input("Enter key name : ")
            sp.getoutput('aws ec2 delete-key-pair --key-name {0}'.format(key_name))
        else :
            print('unsupported input')
    elif command ==2:
        sg = int(input('1.Create  2.Delete '))
        if sg == 1:
            se_group_name = input("Enter name for security group : ")
            se_disc = input("Enter description for security group : ")
            sp.getoutput('aws ec2 create-security-group --group-name {0} --description {1}'.format(se_group_name, se_disc))
        elif sg == 2:
            se_grp_id = input("Enter id of security group :")
            sp.getoutput('aws ec2 delete-security-group --group-id{0}'.format(se_grp_id))
        else : 
            print('unsupported input')
    elif command == 3:
        ins_id = input(" Enter Instance ID : ")
        op = int(input('1.start  2.stop  3.terminate'))
        if op == 1: 
            sp.getoutput('aws ec2 start-instances --instance-ids {0}'.format(ins_id))
        elif op == 2: 
            sp.getoutput('aws ec2 stop-instances --instance-ids {0}'.format(ins_id))
        elif op == 3: 
            sp.getoutput('aws ec2 terminate-instances --instance-ids {0}'.format(ins_id))
        else: 
            print('unsupported input')
    elif command == 4:
        l= sp.getoutput('aws ec2 describe-instances')
        print(l)
    elif command == 5:
        img_id = input("Enter image id : ")
        img_type = input("Enter image type : ")
        subnet_id = input("Enter subnetId : ")
        se_id = input("Enter security group id : ")
        key_name = input("Enter created  key name : ")
        sp.getoutput('aws ec2 run-instances --image-id {0} --instance-type {1} --subnet-id {2} --security-group-id {3} --key-name {4}'.format(
                img_id, img_type, subnet_id, se_id, key_name))
    else : 
        print('unsupported input')

def ebsconf():
    print("-----------EBS----------")
    print("1. Create EBS volume")
    print("2. Attach EBS volume to EC2 instance")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        vt = input("Enter the type of volume : ")
        size = input("Enter the size of volume :")
        zone = input("Enter the name of avaiability zone :")
        sp.getoutput('aws ec2 create-volume --volume-type {0} --size {1}  --availability-zone {2}'.format(vt, size, zone))
    elif command ==2:
        vol_id = input("Enter volume id: ")
        instance_id = input("Enter instance id : ")
        dev_name = input("Enter device name or drive name : ")
        sp.getoutput('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}'.format(vol_id, instance_id, dev_name))
    else : 
        print('unsupported input')
            
            
def s3conf():
    print("-----------S3----------")
    print("1. Create Bucket")
    print("2. List buckets and objects")
    print("3. Create Object")
    print("4. Delete Bucket")
    print("5. Delete Object")
    command = int(input('\nEnter your choice - '))
    if command ==1:
        buck_name = input("Enter unique bucket name : ")
        region_name = input("Enter region name :")
        s = sp.getoutput('aws s3 mb s3://{0} --region {1}'.format(buck_name,region_name))
        print(s)
    elif command ==2 :
        s = sp.getoutput('aws s3 ls')
        print(s)
    elif command ==3 :
        s = sp.getoutput('aws s3 sync')
        print(s)
    elif command ==4 :
        buck_name = input("Enter bucket name : ")
        s = sp.getoutput('aws s3 rb s3://{}'.format(buck_name))
        print(s)
    elif command ==5 :
        buck_name = input("Enter bucket name : ")
        obj_name = input("Enter object name : ")
        s = sp.getoutput('aws s3 rm s3://{0}/{1}'.format(buck_name,obj_name))
        print(s)
#def hadoopconf()
def webser_conf():
    os.system("tput setaf 7")
    print("\t\t\t==============================================")
    os.system("tput setaf 2")
    print("\t\t\t| YOU CAN CONFIGURE WEBSERVER EASILY USING MY TUI |")
    os.system("tput setaf 7")
    print("\t\t\t==============================================")
    print("\t\t\tTo configure webserver following steps are must")
    print("\t\t\t install httpd ")
    print("\t\t\t start the service of httpd")
    print("\t\t\t===============================================")
                                        
    name=input("Enter install to install the httpd :")
    q = os.system("yum install httpd".format(name))
    print(q)
    os.system("tput setaf 2")
    print("Done.")
    print("\t\t\t===============================================")
    os.system("tput setaf 7")
    state = input("Enter start to start the service:")
    r = os.system("systemctl {0} httpd".format(state))
    print("Configuration done !")
    
os.system("clear")


os.system("tput setaf 7")
print("\t\t\t==============================================")
os.system("tput setaf 2")
print("\t\t\t|Hey Welcome to my TUI that makes life simple|")
os.system("tput setaf 7")
print("\t\t\t==============================================")


passwd=getpass.getpass("Enter the password: ")

apass="redhat"

if passwd != apass:
	print("Sorry! You've entered the wrong password..")
	exit()

	
while(True):
    system = input('Do you want to use local or remote(l/r) - \n')
    if system == 'l' or system == 'L':
        MENU()
    elif system == 'r' or system == 'R':
        Menussh()
    else:
        print('unsupported input\n')
    x=input('Do you want to exit (y/n) - \n')
    if x == 'y' or x == 'Y':
        exit()
    else:
        continue

