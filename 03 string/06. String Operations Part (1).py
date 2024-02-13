# Program 1 check for substring 
# ex: substring of "ABCD" are "", "A", "B", "C". "D", "AB", "ABC", "ABCD", "BC", "BCD", "CD"
s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s1)
print(s2 not in s1)


# Program 2 Concatenation
s3 = "geeks"
s4 = "forgeeks"
s5 = s3 + s4
s6 = "welcome to " + s5
print(s5)
print(s6)


# Finding a Position of Substring
s7 = "geeksforgeeks"
s8 = "geeks"

print(s7.index(s8)) # gives index of first position of substring
print(s7.rindex(s8)) # gives last index of substring
print(s7.index(s8,0,13))
print(s7.index(s8,1,13)) # search start from 1 and end at 13-1


# If substring is not present in main string then it will give error
# ValueError