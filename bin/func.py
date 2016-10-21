import subprocess
import os

def pwd(*args):
    subprocess.call("pwd",shell=True)

def ls(*args):
    subprocess.call("ls",shell=True)

def cd(*args):
    print(args)
    os.chdir(*args[0])