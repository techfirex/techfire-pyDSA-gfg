# set in python
# distict elements
# unordered
# no indexing
# union, intersection, set difference etc are fast
# uses hashing internally

# =====================================
# s1 = {10,20,30}
# print(s1)

# s2 = set([20,30,40])
# print(s2)

# s3 = {} # create empty dict not set
# print(type(s3))

# s4 = set() # create empty set
# print(type(s4))
# print(s4)

# =========================================
# An example python program for set insertion operations
# s = {10,20}
# print(s)

# s.add(30)
# print(s)

# s.add(30)
# print(s)

# s.update([30,40])
# print(s)

# s.update({60,70},[80,90])
# print(s)

# ============================================
# An example python program for set deletion operations
# s = {10,20,30,40}
# s.discard(30) # remove item from set and does not raise error if item not present in set
# print(s)

# s.remove(20) # remove item from set and does raise error if item not present in set
# print(s)

# s.clear() # clear/empty the set
# print(s)

# s.add(50)
# del s # remove whole set object, so after this set is not empty it will completely removed so that we cannot access s set as well as cannot apply add, remove etc method
# # del statement also work same in list 


# ============================================
# An example python program for set other operations
# s = {10,20,30,40}
# print(len(s))

# print(20 in s)
# print(50 in s)

# ============================================
# operations on two sets
# s1 = {2,4,6,8}
# s2 = {3,6,9}
# print(s1 | s2) # union // u = s1.union(s2) // doest modify s1 and s2 and gives new union set
# print(s1 & s2) # intersection // i = s1.intersection(s2) 
# print(s1 - s2) # set difference // d = s1.difference(s2) // not that s1.difference(s2) and s2.difference(s1) is not same difference. s1.difference(s2) means items present in s1 but not in s2
# print(s1 ^ s2) # symmentric diffference // bitwise xor // present in s1 and s2 but not common elements of both  // s = s1.symmentric_difference(s2)

# s3 = {2,4,6,8}
# s4 = {4,8}
# print(s3.isdisjoint(s4)) # gives True if there is no common elements in two sets, otherwise gives False
# print(s3 <= s4) # subset // s3.issubset(s4)
# print(s3 < s4) # proper subset // tells s3 is proper subset of s4 or not
# print(s3 >= s4) # superset //  s3.issuperset(s4)
# print(s3 > s4) # proper superset 