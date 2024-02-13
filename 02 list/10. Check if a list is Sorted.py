l1 = [10,20,30]
l2 = [10,20,20,30]
l3 = [10,5,2]
l4 = [10]
l5 = []
l6 = [10,5,30]
l7 = [10,20,30,15,40]

# Method 1: Using Loop // more efficient
def isSorted(l):
    i = 1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i = i + 1
    return True

# driver code
l = [10,20,30,15,40]
if isSorted(l):
    print("yes")
else:
    print("No")


# Method 2: Using Sorted()
def isSorted2(l):
    sl = sorted(l)
    if sl == l:
        return True
    else:
        return False

lx = [10,20,5,30]
if isSorted(l):
    print("yes")
else:
    print("No")

# l.sort() // sort original list 
# sorted(l) // give new sorted list

# // same as above
# l.reverse 
# reversed(l)