#!/usr/bin/python3

import os
import sp as sp

# docker , LVM


system = input('Do you want to use local or remote(l/r) - \n')
if system == 'l':
	menu()
elif system == 'r':
	menussh()
else:
	print('unsupported input\n')

def menu():
    print('Services - ')
    print('1. Docker')
    print('2. LVM')
    print('3. AWS')
    print('4. Hadoop')
    service = input('Enter here : ')
    if service == 'Docker' or 'docker' :
        dockerconf()
    elif service == 'lvm' or 'LVM':
        lvmconf()
    elif service == 'aws' or 'AWS':
        awsconf()
    elif service == 'hadoop' or 'Hadoop':
        hadoopconf()
    else : 
        print('unsupported input')
        

def dockerconf():
    ec = sp.getoutput('docker --version | echo $?')
    if ec != 0 :
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
            op = input('1.start  2.stop  3.status')
            if op == 1: sp.getoutput('systemctl start docker')
            elif op == 2: sp.getoutput('sytemctl stop docker')
            elif op == 3: sp.getoutput('systemctl status docker')
            else: print('unsupported input')
        elif command == 2:
            op = input('1.Recent process  2.All process')
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



            
        
def httpdconf()        
def menussh()
def lvmconf()
def awsconf()
def hadoopconf()