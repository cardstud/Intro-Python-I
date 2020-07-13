"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
""" This module provides access to some variables used or maintained by the
interpreter and to functions that interact strongly with the interpreter

The list of command line arguments passed to a Python script. argv[0] is the script name
If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'.
If no script name was passed to the Python interpreter, argv[0] is the empty string
"""
# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('------------------------------')
print("This is the name of the program:", sys.argv[0]) 
print("Argument List:", str(sys.argv))

print(sys.dllhandle)
print(sys.path)
print(sys.winver)

# Print out the OS platform you're using:

""" sys.windowsversion()
Return a named tuple describing the Windows version currently running. 
The elements are: major, minor, build, platform, service_pack, service_pack_minor,
service_pack_major, suite_mask, product_type, platform_version

product_type maybe:
1 (VER_NT_WORKSTATION)  - system is a workstation
2 (VER_NT_DOMAIN_CONTROLLER) - system is a domain controller
3 (VER_NT_SERVER) - system is a server, but not a domain controller

platform will be 2 (VER_PLATFORM_WIN32_NT)
platform_version returns the accurate major version, minor version and build
  number of the current OS
"""
# YOUR CODE HERE
print('------------------------------')
print('The OS platform I am using is: ', sys.getwindowsversion().platform_version)
print('------------------------------')

# Print out the version of Python you're using:
print('------------------------------')
print('The version of python is: ', sys.version_info)
print('------------------------------')
import os 
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

""" This module provides a portable way of using operating sysmte dependent 
functionality.
1. If you want to read or write a file, see open()
2. If you want to manipulate paths, see the os.path module
3. If you want to read all the lines in all the files on the command line,
     see the fileinput module
4. For creating temp files and directories, see the tempfile module
5. For high-level file and directory handling, see the shutil module
"""

# Print the current process ID
print('The current process ID is: ', os.getpid())

# Print the current working directory (cwd):
print('The current working directory is: ', os.getcwd())

# Print out your machine's login name
print(os.getlogin())
