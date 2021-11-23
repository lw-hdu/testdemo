import paramiko
import os.path
import csv
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='10.221.122.93', port=22, username='root', password='sihuahz')
root_path='/opt/hjcip/hjcip/webapps/hjcip/modules/'
#class_path='/home/class/path/path.txt'
rfile=open('path.txt','r')
read_file=rfile.readlines()
#print(read_file)
for spath in read_file:
#    print(spath)
    p,f=os.path.split(spath)
    dst_path=root_path+p
    org_file='/home/class/'+f
    print(dst_path)
    print(org_file)
    change_file='mkdir -p '+ dst_path +';' + 'cp ' +org_file +' '+dst_path
    stdin, stdout, stderr = ssh.exec_command(change_file)
rfile.close()
#print(stdout.readlines())
ssh.close()