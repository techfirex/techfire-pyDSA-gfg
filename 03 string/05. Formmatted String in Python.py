# 1. Using % (Like C Langauge)
name = "ABC"
course = "Python Course"

s = "Welcome, %s to the %s."%(name,course)
print(s)

# 2. Using format() function
name1 = "ABC"
course1 = "Python Course"

s1 = "Welcome, {0} to the {1}.".format(name,course)
print(s1)

# 3. Using f-string
name2 = "ABC"
course3 = "Python Course"

s2 = f"Welcome, {name2} to the {course3}."
print(s2)

# f-string examples
a = 10
b = 20
print(f"sum of {a} and {b} is {a+b}")
print(f"product of {a} and {b} is {a*b}")



s1 = "ABC"
s2 = "abc"
print(f"lower case of {s1} is {s1.lower()}")
print(f"upper case of {s2} is {s2.upper()}")