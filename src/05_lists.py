# For the exercise, look up the methods and functions that are available for use
# with Python lists.

""" My  notes:
Lists in Python can be written as a list of comma-separated values (items)
  between square brackets. Important thing about a list is that items in a 
  list need not be of the same type

1. append()         - add a single element to the end of the list
2. extend()         - adds iterable elements to the end of the list
3. insert()         - insert an element to the list
4. remove()         - removes item from the list
5. index()          - returns the index of the element in the list
6. count()          - returns count of the element in the list
7. pop()            - removes element at the given index
8. reverse()        - reverses the list
9. sort()           - sortes elements of a list
10. copy()          - returns a shallow copy of the list
11. clear()         - removes all items from the list
12. any()           - checks if any Element of an Iterable is True
13. all()           - returns true when all elements in iterable is true
14. ascii()         - returns String Containing Printable Representation
15. bool()          - converts a value to Boolean
16. enumerate()     - returns an Enumerate Object
17. filter()        - constructs iterator from elements which are true
18. iter()          - returns an iterator
19. list()          - creates a list in Python
20. len()           - returns length of an Object
21. max()           - returns the largest item
22. min()           - returns the smallest value
23. map()           - applies function and returns a list
24. reversed()      - returns the reversed iterator of a sequence
25. slice()         - returns a slice object
26. sorted()        - returns a sorted list from the given iterable
27. sum()           - adds items of an iterable
28. zip()           - returns an iterator of tuples
"""

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print('Q1: ', x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

# x = x + y
# print(x)   or
for item in y:
    x.append(item)
print('Q2: ', x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.pop(4)
print('Q3: ', x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print('Q4: ',x)

# Print the length of list x
print('Q5: The length of list x is: ', (len(x)))

# Print all the values in x multiplied by 1000

newlist = []
for item in range(len(x)):
  newlist.append(x[item]*1000)
print('Q6: ', newlist)
