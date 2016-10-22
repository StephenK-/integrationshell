import subprocess
import os

def pwd(*args):
    subprocess.call("pwd",shell=True)

def ifc(*args):
    cmd = "ifc"
    if args[0] == "":
        cmd += "eth0"
    else:
        cmd += str(args)
    subprocess.call("ifc",(args[0]),shell=True)

def ls(*args):
    subprocess.call("ls",shell=True)

def cd(*args):
    os.chdir(*args[0])