s1 = "geeksforgeeks"
s2 = "ide"

print(s1 < s2)
print(s1 <= s2)
print(s1 > s2)
print(s1 >= s2)
print(s1 == s2)
print(s1 != s2)

# compare character by character
# g < i 
# so its give True

# ord func to print unicode values of char // ASCII (old) and Unicode (new) values are same
print(ord("g"))
print(ord("i"))

# More examples
"abcd" > "abc"
"ZAB" > "ABC"
"abc" > "ABC"
"x" > "abcd"