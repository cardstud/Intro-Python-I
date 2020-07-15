"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# foo = open('C:/Users/Todd/Desktop/cs_lambda/Intro-Python-I/src/foo.txt', 'r')
# read_data = foo.read()
# print(read_data)

print('1')

foo = open(r'C:\Users\Todd\Desktop\cs_lambda\Intro-Python-I\src\foo.txt')
print(foo.read())
foo.closed

print()
print('2')
with open('C:/Users/Todd/Desktop/cs_lambda/Intro-Python-I/src/foo.txt') as foo:
    read_data = foo.read()
    print(read_data)

foo.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open('bar.txt', 'w')
bar.write('My name is puddingtame')
bar.write('Ask me again and...')
bar.write("I'll tell you the same\n What now?\n Who knows")
bar.close

print()

bar = open('bar.txt', 'r')
print(bar.read())
