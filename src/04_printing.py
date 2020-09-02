"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.

% is an operator which requires a string on the left-hand side and a value
  or a tuple of values or a mapping object (like 'dict') on the right hand
  side

d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %2d, y is %3.2f, z is %1s" % (10, 2.25, "I like turtles!"))

# Use the 'format' string method to print the same thing
#print("x is {x:2d}, y is {y:2F}, z is {z:1s}".format(x=10, y=2.25, z="I like turtles!"))
print("x is {}, y is {}, z is {}".format(10, 2.25,"I like turtles!"))

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {round(y,2)}, z is {z}')