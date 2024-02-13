l1 = []
for x in range(11):
    if x % 2 == 0:
        l1.append(x)

l3 = [x for x in range(11) if x % 2 == 0]
print(l1)
print(l3)

l2 = []
for x in range(11):
    if x % 2 != 0:
        l2.append(x)

l4 = [x for x in range(11) if x % 2 != 0]
print(l2)
print(l4)

# ----------------------------------------------
# function to get a list that contains
# all those items of l that are smaller than x

def getsmaller(l,x):
    return [i for i in l if i < x]

lx = [0, 2, 4, 6, 8, 10]
x = 8
print(getsmaller(lx,x))

# --------------------------------------
# Returns two lists. the first list contains 
# all even elements of l and second contains odd

def separate_comp(l):
    even = [i for i in l if i % 2 == 0]
    odd = [i for i in l if i % 2 != 0]
    return even, odd

ly = [10,41,30,15,80]
even,odd = separate_comp(ly)
print(even)
print(odd)

# -----------------------------------
s = "geekforgeeks"
lz = [x for x in s if x in "aeiou"]
print(lz)

l10 = ["geeks", "ide", "courses", "gfg"]
l11 = [x for x in l10 if x.startswith("g")]
print(l11)

l15 = [x*2 for x in range(6)]
print(l15)


l20 = ["geeks", "for", "ide", "courses", "gfg"]
l21 = [x.upper() for x in l20 if x.startswith("g")]
print(l21)


# ------------------------------------------
# set comprehensions

l22 = [10,20,3,4,10,20,7,3]

set5 = {i for i in l22 if i % 2 == 0}
set6 = {i for i in l22 if i % 2 != 0}
print(set5)
print(set6)


# ------------------------------------------
# dict comprehensions

l25 = [1,3,4,2,5]
d1 = {i:i**3 for i in l25}
print(d1)

d2 = {i:f"ID{i}" for i in range(5)}
print(d2)

l26 = [101,103,102]
l27 =  ["gfg", "ide", "coursers"]
d3 = {l26[i]:l27[i] for i in range(len(l27))}
print(d3)

# a better way for mapping two list into dict using zip function
d4 = dict(zip(l26,l27))
print(d4)

# -------------------------------------------
# inverting a dictionary 
# key becomes values
# values becomes key

d6 = {
    101:'gfg',
    103: 'ide',
    102: 'coursers'
}

d7 = {v:k for (k,v) in d6.items()}
print(d7)