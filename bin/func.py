import subprocess
import os

def pwd(*args):
    subprocess.call("pwd",shell=True)

def ifc(*args):

    if args[0] == "ifc":
        cmd = "ifc eth0"
    else:
        cmd = args[0]
    print cmd
    subprocess.call(cmd,shell=True)

def ls(*args):
    subprocess.call("ls",shell=True)

def cd(*args):
    os.chdir(*args[0])