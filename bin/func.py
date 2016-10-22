import subprocess
import os

def pwd(*args):
    subprocess.call("pwd",shell=True)

def ifc(*args):
    cmd = "ifconfig"
    print(args)
    if args[0] == []:
        cmd += " eth0"
    else:
        cmd += " "+str(*args[0])
    print(cmd)
    subprocess.call(cmd,shell=True)

def ls(*args):
    subprocess.call("ls",shell=True)

def cd(*args):
    os.chdir(*args[0])