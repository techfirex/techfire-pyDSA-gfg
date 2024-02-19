# Dictionary in Python
# Collection of key value pairs
# unordered
# all keys must be distict
# values may be repeated
# uses hashing internally

# ==================================
# d = {
#     110:"xyz",
#     101:"abc",
#     105:"bcd",
#     104:"abc"
# }

# ===================================
# program 1

# d = {110:"abc", 101:"xyz", 105:"pqr"}
# print(d)

# d = {}
# d["laptop"] = 40000 # d["key"] = value // assigning value to key
# d["mobile"] = 15000
# d["earphone"] = 1000
# print(d)
# print(d["mobile"]) # accessing value using keys

# ===================================
# program 2
# d = {110:"abc", 101:"xyz", 105:"pqr"}
# print(d.get(101)) # .get(key) gives value corresponding to that key
# print(d.get(125)) # not present then give None
# print(d.get(125, "NA")) # this is short cut for printing different specific value rather than None

# if 125 in d:
#     print(d[125]) # if we directly use like this then it will raise error so using get is good
# else:
#     print("NA")

# ===================================
# program 3
d = {110:"abc", 101:"xyz", 105:"pqr", 106:"bcd"}

d[101] = "wxy"
print(len(d))
print(d)

print(d.pop(105)) # .pop(key) gives value of key which is deleted
print(d)

del d[106] # del does not give value for deleted like pop method
print(d)

d[108] = "cde"
print(d.popitem()) # removes last inserted key:value pair