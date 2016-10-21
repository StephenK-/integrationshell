import subprocess

def pwd(*args):
    subprocess.call("pwd",shell=True)

def ls(*args):
    subprocess.call("ls",shell=True)