#!/usr/bin/python
import os
import func


while True:
    userinput = raw_input(os.getcwd()+":$ ")

    userinputsplit = userinput.split()

    if userinputsplit[0] == "pw":
        func.pw(userinputsplit)

    elif userinputsplit[0] == "ls":
        func.ls(userinputsplit)

    elif userinputsplit[0] == "cd":
        func.cd(userinputsplit)

    elif userinputsplit[0] == "ifc":
        func.ifc(userinputsplit)

    elif userinputsplit[0] == "dt":
        func.dt(userinputsplit)

    elif userinputsplit[0] == "ud":
        func.ud(userinputsplit)

    elif userinputsplit[0] == "exit":
        break
    else:
        print("Invalid command")