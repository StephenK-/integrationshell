#!/usr/bin/python
import os
import pw


while True:
    userinput = raw_input(os.getcwd()+"$: ")

    userinputsplit = userinput.split()

    if (userinputsplit[0] == "pw"):
        pw.pwd(userinputsplit[1:])
    elif(userinputsplit[0] == "ls"):
        pw.ls(userinputsplit[1:])
    elif(userinputsplit[0] == "cd"):
        os.chdir(userinputsplit[1])
    else:
        print("Invalid command")