import subprocess, os, time, getpass, grp, pwd
import os
import time
import getpass

def pw(*args):
    subprocess.call("pwd",shell=True)

def ifc(*args):
    cmd = "ifconfig"
    if args[1] == []:
        cmd += " eth0"
    else:
        cmd += " "+str(*args[1])
    subprocess.call(cmd,shell=True)
def dt(*args):
    print time.strftime('%Y%m%d%H%M%S')
def ud(*args):
    name = getpass.getuser()
    user = pwd.getpwnam(name)
    print str(user.pw_uid)+","+str(user.pw_gid)+","+name+","+str(grp.getgrgid(user.pw_gid))+","+str(os.stat(os.getenv('HOME')).st_ino)
def ls(*args):
    subprocess.call("ls",shell=True)

def cd(*args):
    os.chdir(*args[0])