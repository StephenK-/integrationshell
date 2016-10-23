Installation
-------------
Log into the linux VM of your choice.

If connected to the internet, pull the repo from GitHub (https://github.com/StephenK-/integrationshell)
Once you have the up-to-date integrationshell folder on the vm, open the permissions for intergrationshell/bin/shell.py (the easiest way is to use chmod 777)
Set a user to use the shell automatically, sudo chsh -s intergrationshell/bin/shell.py (YOURUSERNAMEHERE)

To start the shell, simply switch user to the user used in the previous command.

Functionality
--------------
The shell comes with the following usable commands.

pw: Prints the current working directory
ls: Prints the contents of the current working directory
cd: Changes the current directory to that of an argument
ifc: Prints the configuration settings of a specified interface. Default eth0
dt: Prints the current date in the form %Y%m%d%H%M%S
ud: Prints the details of the currently logged in user
Exit: Closes the shell and logs out the current user.