#!/usr/bin/python
import os
import func


while True:
    userinput = raw_input(os.getcwd()+":$ ")

    userinputsplit = userinput.split()

    if userinputsplit[0] == "pw":
        func.pwd(userinputsplit[1:])

    elif userinputsplit[0] == "ls":
        func.ls(userinputsplit[1:])

    elif userinputsplit[0] == "cd":
        func.cd(userinputsplit[1:])

    elif userinputsplit[0] == "ifc":
        func.ifc(userinputsplit[1:])

    else:
        print("Invalid command")