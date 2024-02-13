# sequence of characters
# used to store text data, like data read from a file
# typically small set of characters
# characters "A" to "Z" are stored as values from 65 to 90
# characters "a" to "z" are stored as values from 97 to 122


# Program 1
print(ord("a"))
print(ord("A"))

print(chr(97))
print(chr(65))

# Program 2
s = "geek"
print(s)
print(s[0])
print(s[-1])
print(s[1])
print(s[-2])

# Program 3 # Strings are Immutable so its give error
s1 = "geeks"
# s1[0] = "e"
# print(s1)
# TypeError: 'str' object does not support item assignment


# Program 4 # Multi line Strings
s4 = """
This is a python course.
Hope you enjoying it.
"""
print(s4)


