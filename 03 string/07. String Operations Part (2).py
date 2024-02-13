s1 = "geeks"
print(len(s1))

s2 = s1.upper()
print(s2)

s3 = s2.lower()
print(s3)

print(s1.islower())
print(s2.isupper())


# .startswith and .endswith Methods
s = "GeeksforGeeks Python Course"

print(s.startswith("Geeks"))
print(s.endswith("Course"))
print(s.startswith("Geeks",1)) # Starting index 1
print(s.startswith("Geeks",8,len(s))) # start index 8 and end index 27-1


# .split() and .join() Methods
s11 = "geeks for geeks"
print(s11.split())

s12 = "geeks, for, geeks"
print(s12.split(","))

l11 = ["geeksforgeeks", "python", "course"]
print(" ".join(l11))
print(",".join(l11))


# .strip() Method
sss = "--geeksforgeeks---"
print(sss.strip("-"))
print(sss.lstrip("-"))
print(sss.rstrip("-"))


# .find() Method # same like index func but it will not give error. if nothing is found (get -1 instead of error)
ss1 = "geeks for geeks"
ss2 = "geeks"

print(ss1.find(ss2)) # return index at where the string match
print(ss1.find("gfg")) # give -1, if it will not find that string

n = len(ss1)
print(ss1.find(ss2,1,n))