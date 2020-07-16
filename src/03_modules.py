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
for x in sys.argv:
  print(x)

# Print out the OS platform you're using:
print()
print('The oS platform being used is: ', sys.platform)
print('The OS platform I am using is: ', sys.getwindowsversion().platform_version)
print()


# Print out the version of Python you're using:
print('The version of python being used is: ', sys.version)
print('and...')
print('The version of python is: ', sys.version_info)

print()

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
